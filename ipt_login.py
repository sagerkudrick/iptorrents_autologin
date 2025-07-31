import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import sys
import shutil
import os
import time

# Optional: clear undetected_chromedriver cache (comment if you want to keep)
cache_dir = os.path.expandvars(r'%APPDATA%\undetected_chromedriver\undetected')
if os.path.exists(cache_dir):
    print(f"Clearing cache at {cache_dir}...")
    shutil.rmtree(cache_dir)

# Get directory of the executable or script
if getattr(sys, 'frozen', False):
    basedir = os.path.dirname(sys.executable)
else:
    basedir = os.path.dirname(__file__)

with open(os.path.join(basedir, 'config.json')) as f:
    config = json.load(f)

username = config['username']
password = config['password']


def wait_for_login_or_cloudflare(driver):
    wait = WebDriverWait(driver, 5)
    print("Waiting indefinitely for login form or Cloudflare challenge...")

    while True:
        try:
            wait.until(EC.presence_of_element_located((By.NAME, "username")))
            print("Login form detected.")
            return True
        except TimeoutException:
            pass

        try:
            cf_challenge = driver.find_element(By.CSS_SELECTOR, "div#challenge-form, div.cf-browser-verification")
            if cf_challenge.is_displayed():
                print("Cloudflare challenge detected. Please solve it manually in the browser.")
                time.sleep(5)
                continue
        except Exception:
            pass

        time.sleep(2)


def main():
    options = uc.ChromeOptions()
    # Add any options you want here, e.g., disable devtools auto-open:
    # options.add_argument("--disable-blink-features=AutomationControlled")

    print("Launching Chrome browser...")
    driver = uc.Chrome(options=options, headless=False, use_subprocess=True)

    print("Loading iptorrents.com ...")
    driver.get('https://iptorrents.com/')

    # Wait until login form available or Cloudflare challenge solved
    wait_for_login_or_cloudflare(driver)

    # Now proceed with login
    print("Entering credentials...")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    print("Submitting login form...")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    print("Waiting for page load after login (up to 20 seconds)...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    driver.save_screenshot('loggedin.png')
    print("Screenshot saved as loggedin.png")

    print("Login complete. Browser will stay open for 20 seconds, then close automatically.")
    try:
        time.sleep(20)  # 20 minutes
    except KeyboardInterrupt:
        print("Interrupted by user.")

    print("Closing browser...")
    driver.quit()


if __name__ == '__main__':
    main()
