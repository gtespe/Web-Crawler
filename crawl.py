#!/usr/bin/python

import WebsiteParsing
import urllib.request
from bs4 import BeautifulSoup
from collections import deque

# unvisited urls
unvisited = deque([]) 

# visited urls
visited = []
result = []

numstartingsites = input("How many urls to start with? >> ")
maxsites = 100

for k in range(1,numstartingsites):
    unvisited.append("www." + input("    Type Starting Address >> www."))

while len(unvisited) > 0 and len(visited) < maxsites:
    result_index = len(result)
    this_url = unvisited.popLeft()

    #check if we have visited this link, skip if necessary
    if(visited.contains(this_url)):
        continue

    this_domain = WebsiteParsing.urlToDomain(this_url)

    #check if we have visited this domain,
    # add a new website object to the result list if necessary, and fill its fields
    if(visited.contains(this_domain)):
        result_index = result.index(this_domain)
    else:
        result.append(WebsiteParsing.Website(this_domain))
        domain_site = urllib.request.urlopen(this_url)
        soup = BeautifulSoup(domain_site.read(), "html_parser")
        result[-1].title = soup.title.string
        visited.append(this_domain)

    # add the current url to the proper Website object's pages list
    result[result_index].pages.append(this_url)
    current_site = urllib.request.urlopen(this_url)
    soup = BeautifulSoup(current_site.read(), "html.parser")

    for link in soup.find_all('a'):
        unvisited.append(link)
        
# print the results
for website in result:
    website.export()

