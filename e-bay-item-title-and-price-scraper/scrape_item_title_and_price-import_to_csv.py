from bs4 import BeautifulSoup
import requests 
import csv


#OPEN A NEW CSV FILE. IT CAN BE CALLED ANYTHING
file = open('title_price.csv', 'w')
#CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

#CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Title', 'Price'])



page_to_scrape = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=laptop&_sacat=0")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

title = soup.findAll('span', attrs={'role':'heading'})

price = soup.findAll('span', attrs={"class":"s-item__price"})
for title, price in zip(title, price):
    #print(title.text + "-" + price.text)
    writer.writerow([title.text, price.text])
#CLOSE THE CSV FILE
file.close()

print('Done')