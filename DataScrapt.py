from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

driver_path = r"C:\Users\mihir\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


url = "https://www.flipkart.com/search?q=watches+for+man+under+2000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.availability%255B%255D%3DInclude%2BOut%2Bof%2BStock"
driver.get(url)
time.sleep(2)


brandnames = []
names = []
prices = []
availabilities = []

products = driver.find_elements(By.CLASS_NAME, "_1sdMkc.LFEi7Z")



for product in products:
    try:
        brandname = product.find_element(By.CLASS_NAME, "syl9yP").text
        name = product.find_element(By.CLASS_NAME, "WKTcLC").text
        price = product.find_element(By.CLASS_NAME, "Nx9bqj").text
        availability = "Out of Stock" if "Out of stock" in product.text else "Available"

        price = int(price.replace("₹","").replace(",", "").strip())

        if price <= 2000:

            brandnames.append(brandname)
            names.append(name)
            prices.append(price)
            availabilities.append(availability)
    except:
        continue

df = pd.DataFrame({
    "Brand": brandnames,
    "Product Name": names,
    "Price": prices,
    "Availability": availabilities
})
df.to_excel("watches.xlsx", index=False)


driver.quit()

print("Excel file watches.xlsx created successfully!")
