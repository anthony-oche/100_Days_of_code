import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

#=========================== web scraping price =================================

static_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url=live_url, headers=header)
amz_html = response.text

soup = BeautifulSoup(amz_html, "html.parser")

price = soup.find(class_="aok-offscreen").get_text()
price_without_currency = float(price.split("$")[1])

#=============================== Sending mail ======================================

MY_EMAIL = os.getenv("EMAIL_ADDRESS")
password = os.getenv("PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")

#Get product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_without_currency < BUY_PRICE:
    message = f"{title} is on sale for {price}"

    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ocheanthony48@gmail.com",
            msg=f"Subject: Amazon price\n\n{message}\n{live_url}".encode("utf-8")
        )