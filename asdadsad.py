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

# Loop
for j in range(1000000):

    # Open the website
    driver.get("yourlink")

    # Generate set of 5 random words
    random_name = " ".join(fake.words(6))
    random_nip = " ".join(fake.words(6))
    random_email = " ".join(fake.words(6))

    # Find the field element
    name_field = driver.find_element(By.NAME, "login")
    nip_field = driver.find_element(By.ID, "password")
    email_field = driver.find_element(By.ID, "emai")
    submit_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-block.js-sign-in-button")

    # Fill the form
    name_field.send_keys(random_name)
    nip_field.send_keys(random_nip)
    email_field.send_keys(random_email)

    # Submit the form
    submit_button.click()

# # Add a 5-second delay before quitting
# time.sleep(5)

# Close the browser
driver.quit()