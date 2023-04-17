import requests
from bs4 import BeautifulSoup

soup = None
def requestResponse():
    response = requests.get("https://books.toscrape.com/")
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup.title)
    #print(soup.prettify())
    #print(soup.text)
    return soup

def parseTree(soup):
    print(list(soup.ul))
    
def getPrice(soup):
    print(soup.find_all("p", attrs={"class":"price_color"}))
    precos = soup.find_all("p", attrs={"class":"price_color"})
    for preco in precos:
        print(preco.get_text())

def exercicio1():
    response = requests.get("https://books.toscrape.com/")
    soup = BeautifulSoup(response.content, "html.parser")
    star = soup.find_all("p", attrs={"class=\"col-xs-6 col-sm-4 col-md-3 col-lg-3\""})
    precos = soup.find_all("p", attrs={"class":"price_color"})
    print(star)
    
    
if __name__ == "__main__":
    #soup = requestResponse()
    #parseTree(soup)
    #getPrice(soup)
    exercicio1()
