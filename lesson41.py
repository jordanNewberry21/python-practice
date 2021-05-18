# Controlling the Browser with the Selenium Module

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.amazon.com/')

# element = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)')

# element.click()

searchElem = browser.find_element_by_css_selector('#twotabsearchtextbox')

searchElem.send_keys('Marky Mark and the funky bunch')
searchElem.submit()

browser.back()

browser.forward()
browser.refresh()
browser.quit()