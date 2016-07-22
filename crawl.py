#!/usr/bin/python

#from time import sleep
import WebsiteParsing
import urllib.request
from bs4 import BeautifulSoup
from collections import deque


# unvisited urls
unvisited = deque([]) 

# visited urls
visited = []
result = []

numstartingsites = int(input("How many urls to start with? >> "))
maxsites = 100

for k in range(0,numstartingsites):
    unvisited.append("http://www." + input(" Type Starting Address >> http://www."))
try:
    while len(unvisited) > 0 and len(visited) < maxsites:
        result_index = len(result)
        this_url = unvisited.popleft()

        if(this_url is None):
            break

        #check if we have visited this link, skip if necessary
        if this_url in visited:
            continue
           
        this_domain = WebsiteParsing.urlToDomain(this_url)

        print("url: " + this_url)
        print("domain: " + this_domain)

        soup = 0

        #check if we have visited this domain,
        # else add a new website object to the result list if necessary, and fill its fields
        if this_domain in visited:
            for k in range(0,len(result)):
                if(result[k].domain == this_domain):
                    result_index = k
        else:
            result.append(WebsiteParsing.Website(this_domain))
            with urllib.request.urlopen(this_domain) as domain_site:
                soup = BeautifulSoup(domain_site.read(), "html.parser")
            result[-1].title = soup.title.string
            visited.append(this_domain)

        
        print(visited)
     
        # add the current url to the proper Website object's pages list
        result[result_index].pages.append(this_url)

        #only fetch the site again if you arent looking for a domain
        if(this_domain != this_url):
            with urllib.request.urlopen(this_url) as current_site:
                soup = BeautifulSoup(current_site.read(), "html.parser")

        for link in soup.find_all('a', href=True):
            #no javascript links allowed
            href = link['href']
            if not 'javascript:' in href:
                #if its still on this domain, add the domain to the link
                if href.startswith('/'):
                   href = this_domain + href 

                unvisited.append(href)

        print(unvisited)
        print("end cycle")
except:
   k = 0 #do nothing
    

# print the results
for website in result:
    website.export()


