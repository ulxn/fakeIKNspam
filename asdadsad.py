from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
# import time

# Initialize the Chrome driver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Create an instance of Faker
fake = Faker()

# Loop to perform the sequence 5 times
for j in range(1000000):

    # Open the website
    driver.get("yourlink")

    # Generate new set of 5 random words
    random_name_words = [fake.word() for _ in range(5)]
    random_nip_words = [fake.word() for _ in range(5)]
    random_email_words = [fake.word() for _ in range(5)]

    # Fill and submit form
    name_field = driver.find_element(By.NAME, "login")
    nip_field = driver.find_element(By.ID, "password")
    email_field = driver.find_element(By.ID, "emai")

    name_field.send_keys(" ".join(random_name_words))
    nip_field.send_keys(" ".join(random_nip_words))
    email_field.send_keys(" ".join(random_email_words))

    submit_button_new_tab = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-block.js-sign-in-button")
    submit_button_new_tab.click()

# # Add a 5-second delay before quitting
# time.sleep(5)

# Close the browser
driver.quit()