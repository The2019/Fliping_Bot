import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up Safari webdriver
driver = webdriver.Safari()


driver.get('https://www.willhaben.at/iad/gebrauchtwagen/auto/')
time.sleep(2)

cookis = driver.find_element(By.ID, "didomi-notice-agree-button")
cookis.click()
time.sleep(1)

search_bar = driver.find_element(By.NAME, 'areaId')
search_bar.send_keys('Wien')
time.sleep(1)

search_button = driver.find_element(By.CLASS_NAME,'btn-search')
search_button.click()
time.sleep(1)

# Find all the listings on the page
listings = driver.find_element(By.CLASS_NAME,'search-result-entry')

# Create a new file to save the data
with open('willhaben_data.txt', 'w') as file:

    # Iterate over the listings and extract the data
    for listing in listings:
        title = listing.find_element_by_class_name('search-result-title').text
        price = listing.find_element_by_class_name('search-result-price').text
        location = listing.find_element_by_class_name('search-result-loc').text

        # Write the data to the file
        file.write(f'{title}, {price}, {location}\n')

# Quit the webdriver
driver.quit()
