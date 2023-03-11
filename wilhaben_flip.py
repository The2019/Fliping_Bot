import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up Safari webdriver
driver = webdriver.Safari()

# Navigate to willhaben.com
driver.get('https://www.willhaben.at/iad/kaufen-und-verkaufen')
time.sleep(2)


cookis = driver.find_element(By.ID, "didomi-notice-agree-button")
cookis.click()
time.sleep(1)

# Find the search bar and enter the city name
search_bar = driver.find_element(By.ID, 'keyword')
search_bar.send_keys('PlayStation 5')
search_bar.send_keys(Keys.ENTER)
time.sleep(1)

# Find all the listings on the page
listings = driver.find_elements(By.ID,'skip-to-resultlist')

# Create a new file to save the data
with open('willhaben_data.txt', 'w') as file:

    # Iterate over the listings and extract the data
    for listing in listings:
        title = listing.find_element(By.CLASS_NAME, "Text-sc-10o2fdq-0 bsRRaI").text
        price = listing.find_element_by_class_name('search-result-price').text
        location = listing.find_element_by_class_name('search-result-loc').text

        # Write the data to the file
        file.write(f'{title}, {price}, {location}\n')

# Quit the webdriver
driver.quit()