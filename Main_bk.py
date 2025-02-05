import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from excel_details import iterate_excel_rows

from datetime import datetime

def setup_logger():
    log_filename = f"C:\\Users\\satya\\OneDrive\\Desktop\\govreg\\log\\app__{datetime.now().strftime('%Y-%m-%d____%H-%M-%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()

def startup():
    phone_list_Found=False
    # Initialize the logger
    
    logger = setup_logger()
    logger.info("Logger is set up and ready to use.")
    

    # Log the start of the automation process
    logger.info("Starting the automation process...")

    # Set up Chrome options to handle microphone permissions
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Automatically allow microphone access

    # Initialize the WebDriver
    try:
        service = Service(ChromeDriverManager().install())  # Automatically manage chromedriver
        driver = webdriver.Chrome(service=service, options=chrome_options)  # Use Chrome options for custom behavior
        logger.info("Driver initialized successfully.")

        # Open the target URL
        driver.get("https://work.8x8.com/contacts/company")
        driver.maximize_window()
        logger.info("Navigated to the 8x8 login page.")

        # Wait for the username field to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginId")))

        # Fill in the username
        username_field = driver.find_element(By.ID, "loginId")
        username_field.clear()
        username_field.send_keys("FaraonIndustries.liza.smith")  # Replace with actual username
        username_field.send_keys(Keys.RETURN)
        logger.info("Username entered successfully.")

        # Wait for the password field to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

        # Fill in the password
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("Copy@123456")  # Replace with actual password
        password_field.send_keys(Keys.RETURN)
        logger.info("Password entered and form submitted.")
        
        time.sleep(10)
        
####################Working fine but need to check#######################

        # try:
        #     # Wait for the element to be clickable
        #     element = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.CLASS_NAME, "sc-bdfBQB.essscW.sc-kfvAZH.kHsTnb"))
        #     )
            
        #     # Click using ActionChains to avoid interception
        #     ActionChains(driver).move_to_element(element).click().perform()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}")
            
            
###########################Issue part of the code ##################################    
#1       
        # try:
        #     button = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[1]/div[2]/div/div/button[2]")

        #     # Click the button
        #     button.click()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}") 
            
        # try:
        #     button = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[1]/div[3]/button[2]")

        #     # Click the button
        #     button.click()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}")    
        # try:
        #     button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[3]/button[2]")

        #     # Click the button
        #     button.click()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}")    
        # try:
        #     button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/button")

        #     # Click the button
        #     button.click()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}")   
        # try:
        #     button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div/div[1]/button")

        #     # Click the button
        #     button.click()
            
        #     print("Clicked on the element successfully.")
        
        # except Exception as e:
        #     print(f"Error: {e}")                
            
#################################Issue part of the code ############################      
        time.sleep(10)
        try:    
            phone_list = iterate_excel_rows("company_data.xlsx")
            if phone_list:phone_list_Found=True
        except:
             pass   
        page_source = driver.page_source

        # Check if the specific element text exists in the page source
        if 'Make a call' in page_source and phone_list_Found:
             
            field = driver.find_element(By.ID, "keypad-input-phone-number")
            field.clear()
            for phone_lists in phone_list:
                field.clear()
                field.send_keys(phone_lists) 
                print("Element found: Make a call")




        # Wait for the post-login page to load
        logger.info("Successfully logged in and the post-login page has loaded.")

    except Exception as e:
        # Log any exceptions
        logger.error(f"An error occurred during the automation process: {e}")

    finally:
        # Clean up and close the browser
        # if 'driver' in locals():
        #     driver.quit()
        logger.info("Browser closed and resources cleaned up.")

# Call the startup function
startup()
