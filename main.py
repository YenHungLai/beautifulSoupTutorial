import requests                # Include HTTP Requests module
import pprint
import urllib.request
import os
import webbrowser
import csv
from bs4 import BeautifulSoup  # Include BS web scraping module

# pprint config
pp = pprint.PrettyPrinter(indent=4)

url = "https://www.gettyimages.com/photos/lily-collins?family=editorial&sort=mostpopular&phrase=lily%20collins&page=1&recency=anydate&suppressfamilycorrection=true"  # Website / URL we will contact
r = requests.get(url)           # Sends HTTP GET Request
print(r.status_code)            # ---> Print HTML status code <---
soup = BeautifulSoup(r.text, "html.parser")  # Parses HTTP Response
# print(soup.prettify())          # Prints user-friendly results

# # Find the first section with id='home'
# print(soup.find('section', id='home').prettify())

# # returns the first div on the page
# soup.find('div')

# # finds the respective HTML tag element
# soup.title
# soup.h1
# soup.body.div

# pp.pprint(soup.find_all('a'))      # finds all <a> elements and store them in an array

# for link in soup.find_all('a'):  # iterate over every <a> tag
#     print(link.get_text())       # print inner text to the screen

# # Get all links
# for link in soup.find_all('a'):
#     print(link.get('href'))

# CSS selectors

# # Find tags
# print(soup.select('section')[0].prettify())

# # Tags beneath other tags
# print(soup.select('figure img')[0]['src'])

# # Tags directly beneath other tags  ???
# print(soup.select("head > title")[0].prettify())

# # class
# print(soup.select(".links")[0].prettify())

# # id
# print(soup.select("#projects")[0].prettify())

# # Download imgs
# links = soup.select('figure img')
# number = 1
# for link in links:
#     # Access tag attribute
#     url = link['src']
#     r = requests.get(url)
#     with open(f'C:/Users/Jacob/Desktop/Python/beautifulSoupTutorial/imgs/lily{number}.jpg', 'wb') as f:
#         f.write(r.content)
#     number = number + 1

# Parse local html
# htmlFile = open('sample.html')
# soup = BeautifulSoup(htmlFile, 'html.parser')
# print(soup.prettify())
# print(soup.title.text)
# print(soup.body.button.text)
# print(soup.find('button', class_='damn'))


# # Download files
# url = 'http://www.media2.hw-static.com/media/2017/01/2017-01-23-lily-collins-wenn-1024x683.jpg'
# r = requests.get(url)

# with open('/Users/Jacob/Desktop/git-repo/beautifulSoupTutorial/img.jpg', 'wb') as f:
#     f.write(r.content)

# Open website in a new tab
# webbrowser.open_new('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')

# Output to CSV
with open('sample.csv', 'w') as csvFile: 
    csvWriter = csv.writer(csvFile)
    for i in range(0, 9):
        csvWriter.writerow('Amber needs to speak when...\n')