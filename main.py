import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define XPaths and Locators
locators = {
    'login_button': '//*[@id="account-types"]/a[2]/div/button',
    'email_input': 'email',
    'password_input': 'password',
    'signin_button': '/html/body/div[1]/div/section/div/div[2]/div/div/form/div[3]/button'
}

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load account information from file
accounts = {}
with open("accounts.txt") as accounts_file:
    account_information = accounts_file.read().strip().split("\n")

for i in range(0, len(account_information) - 1, 2):
    accounts[account_information[i]] = account_information[i + 1]

for username, password in accounts.items():
    logger.info(f"Logging into account {username}")
    
    driver.get("https://app.junilearning.com/teacher/my_clubs")

    # Click instructor to login
    driver.find_element(by=By.XPATH, value=locators['login_button']).click()

    # Enter username/password
    driver.find_element(by=By.NAME, value=locators['email_input']).send_keys(username)
    driver.find_element(by=By.NAME, value=locators['password_input']).send_keys(password)

    # Click sign in button
    driver.find_element(by=By.XPATH, value=locators['signin_button']).click()

    logger.info("Logged in successfully")
   
    # You can add additional actions here

    input("Press Enter to continue...")  # Optional pause for user interaction

    # Logout
    driver.get("https://app.junilearning.com/logout")

logger.info("All done. Thank you for keeping our community safe :)")

# Close the WebDriver session
driver.quit()
