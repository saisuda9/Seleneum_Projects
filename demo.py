from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://docs.djangoproject.com/')
print(browser.title)

try:
    assert 'facebook' == browser.title
except AssertionError:
    print(f"page title not matching with original title,actual title is {browser.title} expeted title is {'facebook'}")

    browser.maximize_window()
    time.sleep(5)
    browser.minimize_window()
    time.sleep(5)
    browser.maximize_window()
    time.sleep(5)
    browser.close()
