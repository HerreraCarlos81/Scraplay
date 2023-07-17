import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# Set the path for the Chrome WebDriver
PATH = Service("src/assets/chromedriver.exe")

# Create a new Chrome browser driver
driver = webdriver.Chrome(service=PATH)

# Open the Google search results page for "dentists near me"
driver.get("https://www.google.com/search?q=dentists+near+me")

# Find all the search results
results = driver.find_elements(by=By.CLASS_NAME,value="dbg0pd")

# Iterate over the search results
for result in results:

    # Get the dentist's name
    name = result.text
    print(name)

    # Save the dentist's data in a CSV file
    with open("dentists.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name])

driver.save_screenshot('images/screenshot.png')

# Close the browser driver
driver.quit()