from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

# initialize the Chrome driver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# create an instance of Faker
fake = Faker()

# open the target website
driver.get("yourlink")

# locate the fields and submit button once, outside the loop
name_field = driver.find_element(By.NAME, "login")
nip_field = driver.find_element(By.ID, "password")
email_field = driver.find_element(By.ID, "emai")
submit_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.btn-block.js-sign-in-button")

# loop
for _ in range(1000000):
    # Generate new set of 5 random words
    random_name = " ".join(fake.words(5))
    random_nip = " ".join(fake.words(5))
    random_email = " ".join(fake.words(5))
    
    # Clear the fields before entering new data
    name_field.clear()
    nip_field.clear()
    email_field.clear()
    
    # Fill the form fields
    name_field.send_keys(random_name)
    nip_field.send_keys(random_nip)
    email_field.send_keys(random_email)
    
    # Submit the form
    submit_button.click()
    
    # Reopen the target website after submission to reset the form
    driver.get("yourlink")

# # Add a 5-second delay before quitting
# time.sleep(5)

# Close the browser
driver.quit()