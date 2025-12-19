# Problem 1: Fetch a Web Page Title
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string
print("Page Title:", title)

# Problem 2: Extract All Links
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))

# Problem 3: Extract Table Rows
from bs4 import BeautifulSoup

html = """
<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Alice</td><td>25</td></tr>
<tr><td>Bob</td><td>36</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")

for row in rows:
    cols = [col.get_text() for col in row.find_all(["th", "td"])]
    print(cols)

# Problem 4: Automate Google Search with Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # or Firefox()
driver.get("https://www.google.com")

search = driver.find_element("name", "q")
search.send_keys("Python Web Scraping")
search.send_keys(Keys.RETURN)

time.sleep(2)  # wait for results to load
print(driver.title)

driver.quit()

# Problem 5: Save Scraped Data to CSV
from bs4 import BeautifulSoup
import csv

html = """
<ul>
<li>Apple</li>
<li>Banana</li>
<li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
fruits = [li.get_text() for li in soup.find_all("li")]

with open("fruits.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit'])
    for fruit in fruits:
        writer.writerow([fruit])

print("Saved to fruits.csv")