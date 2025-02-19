from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open Google
driver.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove&page=10")

counter = 1

while True:
    print(f"Page {counter}")
    counter += 1

    try:
        # ✅ Scroll to bottom to load all products
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Give time to load

        # ✅ Find and click "Next" button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div[26]/div/div/nav/a[11]"))
        )
        next_button.click()
        time.sleep(5)  # Give time to load next page

    except:
        print("No more pages. Stopping.")
        break

html = driver.page_source

with open('phone.html' , 'w',encoding='utf-8') as f:
    f.write(html)
