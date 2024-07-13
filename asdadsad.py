from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker  # Import Faker library
import time

# Initialize the Chrome driver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Create an instance of Faker
fake = Faker()

# Loop to perform the sequence 5 times
for j in range(1000000):
    
    # Open a new tab with the same website
    driver.execute_script("window.open('about:blank', 'new_tab');")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("yourlink")

    # Generate new set of 5 random words for the new tab
    random_name_words_new_tab = [fake.word() for _ in range(5)]
    random_nip_words_new_tab = [fake.word() for _ in range(5)]
    random_email_words_new_tab = [fake.word() for _ in range(5)]

    # Fill and submit form in the new tab
    name_field_new_tab = driver.find_element(By.NAME, "login")
    nip_field_new_tab = driver.find_element(By.ID, "password")
    email_field_new_tab = driver.find_element(By.ID, "emai")

    name_field_new_tab.send_keys(" ".join(random_name_words_new_tab))
    nip_field_new_tab.send_keys(" ".join(random_nip_words_new_tab))
    email_field_new_tab.send_keys(" ".join(random_email_words_new_tab))

    submit_button_new_tab = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-block.js-sign-in-button")
    submit_button_new_tab.click()

# Close the new tab and switch back to the original tab
driver.close()
driver.switch_to.window(driver.window_handles[0])

# # Add a 5-second delay before quitting
# time.sleep(5)

# Close the browser
driver.quit()
