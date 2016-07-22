
def urlToDomain(url):
    #if there isnt a slash at the end, add one (makes parsing easier)
    if not url.endswith('/'):
        url += '/'

    numSlashes = 0

    #cycle through the string and find the third '/' i.e. http://www.example.com/fdsafdsa/
    for k in range(0, len(url)):
        if(url[k] == '/'):
            numSlashes += 1
            if(numSlashes == 3):
                return url[:k]

class Website:
    pages = []
    title = ""
    domain = ""

    def __init__(self, d):
        self.domain = d
        

    def export(self):
        target = open(self.domain[11:len(self.domain)-1] + ".txt", 'w')
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
