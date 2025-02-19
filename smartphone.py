from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random



# Path to ChromeDriver
driver_path = Service('/Users/ddhanushnaik/Documents/career/ML/python 2/project/adv webscraping/chromedriver')

# Set Chrome options
chrome_options = Options()
# chrome_options.add_argument("--incognito")  # Open in Incognito mode
chrome_options.add_experimental_option("detach", True)  # Keeps Chrome open
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("start-maximized")

# Rotate User-Agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# Define the driver and open the browser
driver = webdriver.Chrome(service=driver_path, options=chrome_options)

# Hide Selenium from detection
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get('https://www.ajio.com/s/men-watches-3991-40341?query=%3Arelevance%3Averticalsizegroupformat%3AFS&curated=true&curatedid=men-watches-3991-40341&gridColumns=3')
old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source

with open('watches.html','w' , encoding='utf-8') as f:
    f.write(html)