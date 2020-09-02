import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Nestle-Pure-Life-Natural-Spring/dp/B07PVPHN5P/ref=sr_1_6?dchild=1&keywords=Nestle+water&qid=1599013150&sr=8-6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    
    converted_price = float(price[5:8])

    if(converted_price < 35.0):
        send_mail()
    
    print(title.strip())
    print(converted_price)


    if(converted_price < 35.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('markanthonyantao@gmail.com', 'spzwcxeycqulrlwr')

    subject = 'Price Fell Down'
    body = 'Check the Amazon link. The price fell down. https://www.amazon.ca/Nestle-Pure-Life-Natural-Spring/dp/B07PVPHN5P/ref=sr_1_6?dchild=1&keywords=Nestle+water&qid=1599013150&sr=8-6'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'markanthonyantao@gmail.com',
        'markanthonyantao@gmail.com',
        msg
    )

    print('Email has been sent!')
    server.quit()

check_price()