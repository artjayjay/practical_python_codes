from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'path/to/chromedriver' with the path to your downloaded ChromeDriver executable
chrome_driver_path = 'C:/Users/yourname/Desktop/chromedriver/chromedriver.exe'

# Replace 'your_username' and 'your_password' with your actual login credentials
username = 'your username'
password = 'your password'

login_url = 'https://yourwebsite.com/'  # Replace with the login page URL

# Set up ChromeOptions and add the executable path
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

# Create a ChromeDriver instance with the ChromeOptions
driver = webdriver.Chrome(service=service, options=options)

try:
    # Log in to the website
    driver.get(login_url)

    # Wait for the username input field to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'input-1'))).send_keys(username)

    # Wait for the password input field to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'input-2'))).send_keys(password)

    # Find the login form and submit it
    login_form_locator = 'form[data-v-771317a2]'  # CSS selector to locate the form by its data-v attribute
    login_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_form_locator)))
    login_form.submit()

    # Wait for the login process to complete (you may need to adjust the wait time as needed)
    WebDriverWait(driver, 30).until(EC.url_contains(login_url))

    # Now, get the page source after login
    page_source = driver.page_source

    # Print the HTML content
    print(page_source)

    # Save the HTML content to a file (optional)
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(page_source)

finally:
    # Finally, close the browser window
    driver.quit()
