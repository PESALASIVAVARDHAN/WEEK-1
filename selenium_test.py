import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver (this automatically installs the driver using webdriver_manager)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the Flask app's URL (make sure the Flask app is running at this address)
driver.get("http://127.0.0.1:5000/")

# Wait for the page to load
time.sleep(2)

# Find input fields and enter test data
driver.find_element(By.ID, "Open").send_keys("50.0")
driver.find_element(By.ID, "High").send_keys("52.0")
driver.find_element(By.ID, "Low").send_keys("48.0")
driver.find_element(By.ID, "Close").send_keys("49.5")
driver.find_element(By.ID, "Adj Close").send_keys("49.5")
driver.find_element(By.ID, "Volume").send_keys("1000000")

# Submit the form
driver.find_element(By.TAG_NAME, "button").click()

# Wait for the prediction result to appear
time.sleep(2)

# Capture and print the prediction result text
result = driver.find_element(By.TAG_NAME, "h3").text
print("Prediction Result:", result)

# Close the browser
driver.quit()
