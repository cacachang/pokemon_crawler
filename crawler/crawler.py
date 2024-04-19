from bs4 import BeautifulSoup
from requests import get
from csv import writer

response = get("https://scrapeme.live/shop/")

soup = BeautifulSoup(response.content, "html.parser")

pages = soup.select(".page-numbers li a")

num = 0
last_num = int(pages[-2].text)
products = []

while num < last_num:
  page_response = get(f"https://scrapeme.live/shop/page/{num}/")
  page_soup = BeautifulSoup(page_response.content, "html.parser")

  elements = page_soup.select(".product")

  for element in elements:
    product = {}
    product["title"] = element.h2.text
    product["url"] = element.a['href']
    product["price"] = element.span.span.text
    products.append(product)

  num += 1

print(products)

with open('product.csv', 'w') as csv_file:
  file_writer = writer(csv_file)
  file_writer.writerow(['標題', '購買連結', '價錢'])

  for product in products:
    file_writer.writerow(product.values())




