from bs4 import BeautifulSoup as bs
import requests

url_va = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
#get the contents from the website
req_va = requests.get(url_va)
html_va = req_va.content
soup = bs(html_va, 'html.parser') #making it a soup object so you can manipulate in python

#As we find in the web source, 'tr' tags with class 'election_item because these contain the ID of every election
tags = soup.find_all('tr','election_item')

#we create a new list, in which I put all the codes of the election, that are the five last digits of the text in election_item
ELECTION_ID=[]
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    i=[year, year_id]
    ELECTION_ID.append(i)
    print(year, year_id)

with open('ELECTION_ID','w') as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + ' ' + line[1])= "\n")
        print(line[0],line[1])
