from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import requests


#TODO 2: Data Entry Automation using Selenium
class DataEntry:

    def __init__(self):
        self.submit_btn = None
        self.another_response = None
        self.form_address = None
        self.form_price = None
        self.form_link = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://forms.gle/d5uMmCfGnT1PorF87")


    def find_element(self):
        self.form_address = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea")
        self.form_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.form_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')


    def submit_response(self):
        self.find_element()
        self.form_link.send_keys(link)
        self.form_price.send_keys(price)
        self.form_address.send_keys(address)
        self.submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        self.submit_btn.click()
        time.sleep(1)
        self.another_response = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.another_response.click()
        time.sleep(2)



#TODO 1: Web Scraping using Bs4
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/", headers=header)
chart_html = response.text

soup = BeautifulSoup(chart_html, "html.parser")


# get all listings of the houses including prices,links and address
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

all_prices_elements = soup.select(".PropertyCardWrapper span")
all_prices = [prices.get_text().split("+")[0].split("/")[0] for prices in all_prices_elements]

all_addr_element = soup.select(".StyledPropertyCardDataWrapper a address")
all_address = [address.get_text().strip('\n | ') for address in all_addr_element]


data_entry = DataEntry()

#create a loop that will loop a list, get a particular price and the index
#for the relating element
for i in range(len(all_prices)):
    price = all_prices[i]
    link = all_links[i]
    address = all_address[i]
    time.sleep(1)
    data_entry.submit_response()
    if i == len(all_prices) - 1:
        print(f"A total of {len(all_address)} houses was listed and responses has been submitted")









