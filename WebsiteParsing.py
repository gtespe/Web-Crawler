
def urlToDomain(url):
    #if there isnt a slash at the end, add one (makes parsing easier)
    if(url[-1] != '/'):
        url += '/'

    numSlashes = 0

    #cycle through the string and find the third '/' i.e. http://www.example.com/fdsafdsa/
    for k in range(0, len(url) - 1):
        if(url[k] == '/'):
            numSlashes += 1
            if(numSlashes == 3):
                return url[:k+1]

class Website:
    pages = []
    title = ""
    domain = ""

    def __init__(self, d):
        self.domain = d
        

    def export(self):
        target = open(self.domain + ".txt", 'w')
        for page in self.pages:
            target.write(page.export())


    def add(self, newpage):
        self.pages.append(newpage)


    
class Page:

    def __init__(self, u, b):
       self.url = u
       self.blurb = b

    def export(self):
        return self.url + '\n' + "        " + self.blurb + "\n\n"
