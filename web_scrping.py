import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python-requests"
response = requests.get(url)

parser = BeautifulSoup(response.text, 'html.parser')

questions = parser.find_all("div",{"class":"s-post-summary"})
for q in questions:
    #print(q)

    title = q.find('h3',{"class":"s-post-summary--content-title"})
    print(title.text.strip())
    content = q.find('div',{"class":"s-post-summary--content--excerpt"})
    print(content)
    print("-------------")


