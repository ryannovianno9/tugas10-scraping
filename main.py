import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.halodoc.com/obat-dan-vitamin/search/Vitamin%20&%20Suplemen"
response = requests.get(url)
html = BeautifulSoup(response.content,"html.parser")

vitamin = []

for nama in html.find_all("div",class_ = "hd-base-product-search-card"):
    x = nama.find("p",class_ = "hd-base-product-search-card__title")
    x = x.text
    vitamin.append(x)

print(vitamin)

with open(r'D:\OneDrive - UGM 365\MBKM\Cakap\Scraping and Crawling\amazon-scraping\daftar_vitamin.csv','w',newline='') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Nama Vitamin'] # buat nama kolom
  csv_writer.writerow(headers) # buat nama kolom csv

  for item in vitamin:
    item = item.replace("\n","")
    csv_writer.writerow([item]) # buat baris baru pada csv