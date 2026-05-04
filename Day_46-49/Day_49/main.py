import os
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

ACCOUNT_MAIL = "switch@test.com"
PASSWORD = "pass12345"
GYM_URL = "https://appbrewery.github.io/gym/"

#==================== configure selenium ================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#================= give selenium it's own user profile ============

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(chrome_options)
wait = WebDriverWait(driver, 2)
driver.get(url=GYM_URL)



def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)
    return None


def login():
    # ==================== Automate Login ================

    login_btn = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_btn.click()

    # fill out login form
    email_field = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_field.send_keys(ACCOUNT_MAIL)

    pass_field = driver.find_element(By.NAME, "password")
    pass_field.send_keys(PASSWORD)

    submit_btn = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
    submit_btn.click()


def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")
    # ========================= Booking a class ===================

retry(login, description="login")

booked_classes = 0
waitlists_joined = 0
already_booked = 0
processed_class = []

class_cards = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id^="class-card-"]')))
for card in class_cards:
    day_group = card.find_element(By.XPATH,  "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.CSS_SELECTOR, "h2").text

    #check if it's tuesday
    if "Tue" in day_title or "Fri" in day_title:
        #check 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^=class-time-]").text
        if "6:00 PM" in time_text:
            #get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.TAG_NAME, "button")

            class_info = f"{class_name} on {day_title}"

            #click the book button
            if "Booked" == button.text:
                already_booked += 1
                print(f"✓ Already booked:{class_info }")
                processed_class.append(f"[Booked] {class_info}")

            elif button.text == "Waitlisted":
                waitlists_joined +=1
                print(f"✓ Already on waitlist: {class_info}")
                processed_class.append(f"[Waitlisted] {class_info}")

            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Booking")
                waitlists_joined += 1
                print(f"✓ Joined waitlist for: {class_info}")
                processed_class.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

            elif button.text == "Book Class":
                retry(lambda: book_class(button), description="Booking")
                booked_classes += 1
                print(f"✓Booked: {class_info}")
                processed_class.append(f"[New Booking] {class_info}")
                time.sleep(0.5)

total_classes = booked_classes + waitlists_joined + already_booked
print("\n---VERIFYING ON MY BOOKINGS PAGE---")

def get_bookings():
    #==================== Verifying Bookings ======================
    bookings_page = driver.find_element(By.LINK_TEXT, "My Bookings")
    bookings_page.click()
    time.sleep(3)
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

all_cards = retry(get_bookings, description="Get my bookings")

verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Fri" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_classes} bookings")
print(f"Found: {verified_count} bookings")
if total_classes == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_classes - verified_count} bookings")


















# #======================= Booking summary(not used) ===================

    # # print("--- Booking Summary ---\n"
    # #       f"Classes Booked: {booked_classes}\n"
    # #       f"Waitlists Joined: {waitlists_joined}\n"
    # #       f"Already booked/waitlisted: {already_booked}\n")
    # print(f"Total Tuesday 6pm classes processed: {total_classes}")
    #
    # print("\n--- DETAILED CLASS LIST ---")
    # for class_detail in processed_class:
    #     print(f"{class_detail}")