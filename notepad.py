import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
TEST_FOLDER = os.path.join(DESKTOP_PATH, "Test Files")
TEST_FILE_PATH = os.path.join(TEST_FOLDER, "test_document.txt")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:

    os.system("start notepad")
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys("This is a test document.").perform()
    time.sleep(1)

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    actions.send_keys(TEST_FOLDER).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    actions.send_keys("test_document.txt").send_keys(Keys.ENTER).perform()
    time.sleep(2)

    os.system(f"start explorer {TEST_FOLDER}")
    time.sleep(3)

    print("Verifying file existence...")
    assert os.path.exists(TEST_FILE_PATH), "test_document.txt not found in Test Files folder."

    os.system(f"start {TEST_FILE_PATH}")
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys("This document is used for testing.").perform()
    time.sleep(1)

    actions.key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    actions = ActionChains(driver)
    actions.key_down(Keys.ALT).send_keys(Keys.F4).key_up(Keys.ALT).perform()
    time.sleep(2)

    os.system(f"start {TEST_FILE_PATH}")
    time.sleep(3)

    os.remove(TEST_FILE_PATH)
    time.sleep(1)
    os.system("start shell:RecycleBinFolder")
    time.sleep(3)
    driver.quit()
finally:
    driver.quit()

print("Test completed.")
