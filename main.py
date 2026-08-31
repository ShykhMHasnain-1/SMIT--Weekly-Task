from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

web_url = "https://www.daraz.pk/all-products/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(web_url)
driver.implicitly_wait(8)

all_product_links = []

# Open CSV files once
with open("All_links.csv", "w", newline='') as links_file, \
     open("All_Products_Detail.csv", "w", newline='') as details_file:
    links_writer = csv.writer(links_file)
    details_writer = csv.writer(details_file)

    # Write headers for product details
    details_writer.writerow(["Title", "Price", "Description", "Specification"])

    for i in range(1,20):
        print(f"-------Page{i}-------")
        try:
            # Wait for product links to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='RfADt']//a"))
            )
            all_products = driver.find_elements(By.XPATH, "//div[@class='RfADt']//a")
            for p in all_products:
                link = p.get_attribute("href")
                if link not in all_product_links:
                    all_product_links.append(link)
                    links_writer.writerow([link])
        except TimeoutException:
            print("No product links found or page took too long to load.")
            break

        # Check for next page button
        try:
            next_button = driver.find_element(By.XPATH, "//li[@title='Next Page']//button")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)  # Wait for page to load
        except NoSuchElementException:
            print("No more pages.")
            break

    # Now visit each product link
    for link in all_product_links:
        driver.get(link)
        try:
            # Wait for product info to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1"))
            )
            title = driver.find_element(By.XPATH, "//h1[@class='pdp-mod-product-badge-title']").text
            price = driver.find_element(By.XPATH, "//div[@class='pdp-product-price']").text
            description = driver.find_element(By.XPATH, "//div[@class='html-content pdp-product-highlights']").text
            specification = driver.find_element(By.XPATH, "//li[@class='key-li']").text

            details_writer.writerow([title,price,description,specification])

        except NoSuchElementException:
            print(f"Failed to load details for {link}")
        time.sleep(2)  # Be polite

driver.quit()