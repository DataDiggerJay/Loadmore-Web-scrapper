import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------------------

# Define file paths for storing scraped data
CSV_BACKUP_PATH = "scraped_articles_backup.csv"  # Temporary CSV backup
EXCEL_FILE_PATH = "scraped_articles.xlsx"  # Final storage in Excel format

# Website URL to scrape (Change this if you want to scrape another site)
TARGET_URL = "https://izea.com/blog"  # Change this to the target blog or website

# Limit to prevent infinite loops while clicking 'Load More'
MAX_CLICKS = 200  

# ----------------------------------------------------------------------------------
# SETUP SELENIUM WEBDRIVER
# ----------------------------------------------------------------------------------

# Configure Selenium WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-blink-features=AutomationControlled")  
options.add_argument("start-maximized")  # Maximize browser window

# Initialize WebDriver
print("[INFO] Launching WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the target URL
print(f"[INFO] Accessing {TARGET_URL}")
driver.get(TARGET_URL)

# Set up an explicit wait object
wait = WebDriverWait(driver, 10)

# ----------------------------------------------------------------------------------
# SCRAPING PROCESS
# ----------------------------------------------------------------------------------

# List to store article data
article_data = []

print("[INFO] Checking for 'Load More' button...")

load_more_count = 0  # Track number of times 'Load More' is clicked

while load_more_count < MAX_CLICKS:
    try:
        # Locate and click 'Load More' button
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'load-more')]")))
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)  # Scroll to button
        time.sleep(1)  # Short delay before clicking
        driver.execute_script("arguments[0].click();", load_more_button)

        load_more_count += 1
        print(f"[INFO] Clicked 'Load More' {load_more_count} times...")

        # ----------------------------------------------------------------------------------
        # DATA EXTRACTION - Modify here to scrape different elements if needed
        # ----------------------------------------------------------------------------------
        
        # Get page source and parse it using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Locate all articles (Modify the class if scraping another site)
        articles = soup.find_all("a", class_="nectar-post-grid-link")

        # Extract article data
        for article in articles:
            title = article.find("span", class_="screen-reader-text").text.strip() if article.find("span", class_="screen-reader-text") else "No Title"
            href = article.get("href", "No Link")
            original_href = article.get("data-uw-original-href", "No Original Link")

            # Avoid duplicate entries
            if {"Title": title, "href": href, "data-uw-original-href": original_href} not in article_data:
                article_data.append({"Title": title, "href": href, "data-uw-original-href": original_href})

        # ----------------------------------------------------------------------------------
        # BACKUP DATA EVERY 5 CLICKS - Prevent data loss in case of errors
        # ----------------------------------------------------------------------------------

        if load_more_count % 5 == 0:
            pd.DataFrame(article_data).to_csv(CSV_BACKUP_PATH, index=False, encoding="utf-8")
            print(f"[INFO] Backup saved to {CSV_BACKUP_PATH}")

        # Allow time for content to load before next loop
        time.sleep(3)
    
    except:
        print("[INFO] No more 'Load More' button found OR click limit reached. Exiting loop.")
        break  # Exit loop when 'Load More' disappears or reaches limit

# ----------------------------------------------------------------------------------
# CLOSE BROWSER SESSION
# ----------------------------------------------------------------------------------

driver.quit()
print("[INFO] WebDriver session closed.")

# ----------------------------------------------------------------------------------
# SAVE FINAL DATA
# ----------------------------------------------------------------------------------

# Convert scraped data to a Pandas DataFrame
df = pd.DataFrame(article_data)

# Save to Excel file
df.to_excel(EXCEL_FILE_PATH, index=False)
print(f"[INFO] Data successfully saved to {EXCEL_FILE_PATH}")

# ----------------------------------------------------------------------------------
# DELETE BACKUP FILE AFTER SUCCESSFUL SAVE
# ----------------------------------------------------------------------------------

if os.path.exists(CSV_BACKUP_PATH):
    os.remove(CSV_BACKUP_PATH)
    print(f"[INFO] Temporary backup CSV deleted.")

print("[INFO] Scraping process completed successfully.")
