from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

# driver.maximize_window()
#============================= wikipedia ==================
# driver.get("")
# number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# number_of_articles.click()

#find element by link text
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

#===========================find the "search" <input> by name

#if the page isn't maximize the search input is hidden, in order to open it you first click on it before sending keys
# search = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
# search.click()
# search_p = driver.find_element(By.NAME, "search")
# search_p.send_keys("python", Keys.ENTER)

#=========================== Fill out form ===================
# driver.get("https://secure-retreat-92358.herokuapp.com/")

# f_name = driver.find_element(By.NAME, "fName")
# f_name.send_keys("Anthony")
#
# l_name = driver.find_element(By.NAME, "lName")
# l_name.send_keys("Rochi")
#
# e_name = driver.find_element(By.NAME, "email")
# e_name.send_keys("rochi.switch@gmail.com")


#=============================== Cookie clicker  ==========================

driver.get("https://ozh.github.io/cookieclicker/")

#wait time
wait = WebDriverWait(driver, 2)

#ensuring the game fully loads and open
sleep(8)
driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()

#wait for everything to settle
sleep(3)

#find the big cookie to click
cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

# Get all store items (products 0-17)
# item_ids = [f"product{i}" for i in range(18)]

#check the current time/start time
wait_time = 10
time_out = time() + wait_time
five_min = time() + 60 * 1

is_game_on = True
while is_game_on:
    cookie.click()

    #we keep checking the current time without stopping the clicking, we subtract,
    # if that difference is 5secs or more we check for the most expensive
    if time() > time_out:
        try:
            cookie_str = driver.find_element(By.CSS_SELECTOR, "div #cookies").text
            cookie_text = cookie_str.split(" ")[0]
            cookie_count = int(cookie_text)

            #find all available products in the store
            products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

            #find the most expensive item we can afford
            best_item = None
            for product in reversed(products):
                #check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    print(type(best_item))
                    break

            #Buy the best item if found
            if best_item:
                try:
                    cookie_btn = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
                    cookie_btn.click()
                except NoSuchElementException:
                    best_item.click()
                    print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        #reset timer
        timeout = time() + wait_time

    #stop after 5min
    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break


# driver.quit()