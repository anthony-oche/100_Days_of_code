from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

#how easy it is to get hold of price from amazon using selenium
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(f"{price_dollar}.{price_cent}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.size)

#================================ events dictionary ========================



event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
upcoming_events = {}
print(event_times)

for n in range(len(event_times)):
    upcoming_events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }


print(upcoming_events)

#driver.close() #closes a single tab
driver.quit()
#quits the entire browser
