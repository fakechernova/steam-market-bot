
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pickle



chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('C:/Users/chernov/Desktop/pattern/item-hunter.cs/sih.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1900, 1000)
ac = ActionChains(driver)
driver.get(url='https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Minimal%20Wear%29')
time.sleep(5)
print('Wait for login')

time.sleep(13)
driver.refresh()
pickle.dump(driver.get_cookies(), open("cookies", "wb"))

time.sleep(3)

