"""Browser automation utilities using Selenium."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os

def setup_driver():
    """Initialize and configure Chrome WebDriver."""
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Set up Chrome service
        service = Service()
        
        # Create driver
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except WebDriverException as e:
        print(f"Error setting up Chrome WebDriver: {str(e)}")
        print("Please make sure Chrome browser is installed on your system.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during driver setup: {str(e)}")
        sys.exit(1)

def navigate_gfg_problem():
    """Navigate to GFG problem solving page."""
    driver = None
    try:
        # Initialize driver
        driver = setup_driver()
        if not driver:
            return
            
        # Navigate to GFG
        print("Navigating to GeeksforGeeks Problem of the Day...")
        driver.get("https://practice.geeksforgeeks.org/problem-of-the-day")
        
        # Wait for page to load
        time.sleep(2)
        
        # Press Tab 5 times
        active_element = driver.switch_to.active_element
        for i in range(10):
            print(f"Tab press {i+1}/10...")
            active_element.send_keys(Keys.TAB)
            time.sleep(0.5)
        
        # Find and click the Solve Problem button
        print("Looking for 'Solve Problem' button...")
        solve_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Solve Problem')]"))
        )
        solve_button.click()
        print("Successfully navigated to problem page!")
        
        # Keep the browser open
        input("\nPress Enter to close the browser...")
        
    except WebDriverException as e:
        print(f"Browser automation error: {str(e)}")
        print("Please make sure Chrome is installed and up to date.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass