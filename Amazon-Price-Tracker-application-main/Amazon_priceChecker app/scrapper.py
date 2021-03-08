import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.in/Sony-ILCE5100L-24-3MP-Digital-16-50mm/dp/B00MHPAFAG/ref=sr_1_2?dchild=1&keywords=Sony+Alpha&qid=1610119129&s=electronics&sr=1-2'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nickynandini21@gmail.com', 'uuinojixvvhkcvzt')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Sony-ILCE5100L-24-3MP-Digital-16-50mm/dp/B00MHPAFAG/ref=sr_1_2?dchild=1&keywords=Sony+Alpha&qid=1610119129&s=electronics&sr=1-2'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nickynandini21@gmail.com',
        'rituojha30@gmail.com',
        msg
    )

    print('Email has been sent!!!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)


    



 



