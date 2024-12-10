from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set up the Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')  # Disable sandboxing
options.add_argument('--disable-dev-shm-usage')  # Disable shared memory usage
options.add_argument('--disable-gpu')  # Disable GPU acceleration


def scrape_to_html(url='https://www.who.int/emergencies/disease-outbreak-news'):
    # Create a new Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to the ProMED website
    driver.get(url)

    # Wait for the element with class "hubfiltering" to load
    wait = WebDriverWait(driver, 10)
    try:
        hub_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hubfiltering")))

        # Get the outer HTML of the hubfiltering class
        outer_html = hub_div.get_attribute("outerHTML")

        # Save the outer HTML to a file
        with open("res.html", "w", encoding="utf-8") as f:
            f.write(outer_html)

        print("Outer HTML saved to res.html.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()



# date2.send_keys("11/21/2024")
# sleep(7)
# submit_btns = driver.find_elements(By.NAME, "submit")
# Execute JavaScript to click the desired button
# driver.execute_script("arguments[0].click();", submit_btns[1])
