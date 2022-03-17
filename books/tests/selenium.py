# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(scope="module")
# def firefox_browser_instance(request):
#     """
#         Provide a selenium webdriver instance
#     """
#     options = Options()
#     options.headless = False
#     browser = webdriver.Firefox(
#         service=Service(GeckoDriverManager().install()),
#         options=options,
#     )
#     yield browser
#     browser.close()

import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
        provivde a selenium webdriver instance
    """

    options = Options()
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()