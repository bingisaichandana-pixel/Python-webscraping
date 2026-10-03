# This app scraped product data from amozon webiste 

#BeautifulSoup4
#requests
#lxml

from bs4 import BeautifulSoup
import requests 
import csv

url = "https://www.amazon.in/Sony-WH-1000XM6-Headphones-Microphones-Studio-Quality-Platinum/dp/B0F3QJLD3B/ref=sr_1_1_sspa?crid=2FPB80KC0B4VE&dib=eyJ2IjoiMSJ9.wu0ni9HnlSTqdD_JfXfqVFf4PD2CIZcvAtTT48fsb50WttcRCCCn5rlG1BKlpZZO3GHF0OKveTWuA6Vr4dEGZUi9Xmw6D3VsdEQ46bONdLdi6Nm8qwnAidVeO8M_SwnCWIWy_F3K4964s6cgDRPh0Pd-Ct3W7dhJYW43MBAek8T8EIREzUXqOQs2vDPQsqa1W1Gt7xN2p72946YDDJ_jbQ.Qsx441RvR2JIlrXZ6yRGPJ_mrPAxwN_FTBcmkjcB4F4&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax%2Bunder%2B60k&nsdOptOutParam=true&qid=1791012991&sprefix=%2Caps%2C6&sr=8-1-spons&aref=Ldr3xkEALJ&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    #print(response.status_code)
    html_content = response.text
else:
    print("fetching error",response.status_code) 

soup = BeautifulSoup(html_content,'lxml')
print(soup)

 #print(soup.prettify())

product_title = soup.find("span",id="productTitle").text.strip()
product_price = soup.find("span",class_="a-price-whole").text.strip()
product_rating = soup.find("span", class_="a-icon-alt").text.strip()
product_bp = soup.find("span", class_="a-list-item").text.strip()
product_details = soup.find("div",id="prodDetails").text.strip()

reviews = soup.find("div",id = "localTopReviews").text.strip()

print(reviews)

#saving this file data

with open ("amozon_airpod pro max.csv", mode ='w',newline='',encoding='utf-8')as file:
    writer =csv.writer(file)
    writer.writerow(["product_title","product_price","product_rating","product_bp","product_details","reviews"])

    writer.writerow([product_title,product_price,product_rating,product_bp,product_details,reviews])
    
print("data saved!")



#webscraping  lo python autmatic ga  collects data from websites 
# Beautifulsoup ante = webpages lo unna html nuchi manaki kavalisina info teskodhaniki use cheskuney python library 
# preittfy is used for organizing the code in terminal 