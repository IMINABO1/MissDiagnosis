from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def scrape_disease_outbreak_news(output_file="res.html"):
    """
    Scrapes the outer HTML of the 'hubfiltering' class from the WHO emergencies page 
    and saves it to a specified output file.

    Args:
        output_file (str): The name of the file to save the scraped HTML.
    
    Returns:
        bool: True if scraping was successful, False otherwise.
    """
    # Set up the Chrome options
    options = Options()
    # Uncomment this line to run in headless mode
    options.add_argument('--headless')
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')  # Disable sandboxing
    options.add_argument('--disable-dev-shm-usage')  # Disable shared memory usage
    options.add_argument('--disable-gpu')  # Disable GPU acceleration

    # Create a new Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Navigate to the ProMED website
        driver.get('https://www.who.int/emergencies/disease-outbreak-news')

        # Wait for the element with class "hubfiltering" to load
        wait = WebDriverWait(driver, 10)
        hub_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hubfiltering")))

        # Get the outer HTML of the hubfiltering class
        outer_html = hub_div.get_attribute("outerHTML")

        # Save the outer HTML to a file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(outer_html)

        print(f"Outer HTML saved to {output_file}.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the browser
        driver.quit()

# Example usage
if __name__ == "__main__":
    scrape_disease_outbreak_news("res.html")
