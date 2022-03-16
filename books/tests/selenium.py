import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

@pytest.fixture(scope="module")
def firefox_browser_instance(request):
    """
        Provide a selenium webdriver instance
    """
    # binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\firefox.exe')
    options = Options()
    # options.binary_location = FirefoxBinary(firefox_path='C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    options.headless = False
    browser = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        # firefox_binary=binary,
        options=options,
    )
    yield browser
    browser.quit()