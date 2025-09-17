# conftest.py
"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://qa.shalomtv.tv")
    request.cls.driver = driver
    yield driver
    driver.quit()
    """
    
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os


@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.get("https://qa.shalomtv.tv")
    request.cls.driver = driver

    yield driver

    # Take screenshot at the end of the test
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")

    driver.save_screenshot(file_path)
    print(f"\n Screenshot saved to: {file_path}")
    
    time.sleep(10) 
    driver.quit()

