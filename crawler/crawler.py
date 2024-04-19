from bs4 import BeautifulSoup
from requests import get

response = get("https://scrapeme.live/shop/")

soup = BeautifulSoup(response.content, "html.parser")

pages = soup.select(".page-numbers li a")

num = 0
last_num = int(pages[-2].text)

while num < last_num:
  page_response = get(f"https://scrapeme.live/shop/page/{num}/")
  page_soup = BeautifulSoup(page_response.content, "html.parser")

  products = page_soup.select(".product a h2")

  for product in products:
    print(product.text)

  num += 1



