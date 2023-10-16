from bs4 import BeautifulSoup as bs
from dynamic_pattern_list import glock_moonrise, wvgalil, p250_Nevermore, glock_highbeam
import random
import time
import os
import pickle
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



url_list = ['https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Factory%20New%29']

our_seeds = []


for link in url_list:
    if link == 'https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Minimal%20Wear%29':
        our_seeds = glock_moonrise
        print('Glock-18 Moonrise MW')
    elif link == 'https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Factory%20New%29':
        our_seeds = glock_moonrise
        print('Glock-18 Moonrise FN')
    elif link == 'https://steamcommunity.com/market/listings/730/Galil%20AR%20%7C%20Sandstorm%20(Field-Tested)':
        our_seeds = wvgalil
        print('Galil Sandstorm FT')
    elif link == 'https://steamcommunity.com/market/listings/730/StatTrak™%20P250%20%7C%20Nevermore%20%28Factory%20New%29':
        our_seeds = p250_Nevermore
        print('p250 Nevermore')
    elif link == 'https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20High%20Beam%20%28Factory%20New%29':
        our_seeds = glock_highbeam
        print('Glock 18 High Beam')
    else:
        print('zalupa, link does not exist')
    




    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension('C:/Users/chernov/Desktop/pattern/item-hunter.cs/sih.crx')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1900, 1000)
    ac = ActionChains(driver)



    

    time.sleep(3)
    
    driver.get(url=link)
    time.sleep(2)
    for cookie in pickle.load(open('cookies','rb')):
        driver.add_cookie(cookie)
    driver.refresh()
    driver.find_element(By.XPATH, '//*[@id="listings"]/div[5]/div[1]/div[1]/div[1]/div[2]/label/span[1]').click()
    ac.scroll_by_amount(0, 1000).perform()
   
    time.sleep(3)
    buy_status = ''
    while buy_status == '':
        time.sleep(8)
        
        buttons = driver.find_elements(By.XPATH, "//*[contains(text(),'Купить')]")
        page = driver.page_source
        soup = bs(page, "html.parser")
        all_seed = soup.find_all('div', class_ = 'itemseed')
        seed_list = []
        market_items =soup.find_all('div', class_= 'market_listing_row')
        index_seed_list = []



        for seed in all_seed:
            changed = seed.text
            changed = changed.split(': ')[1]
            seed_list.append(changed)

        print (seed_list)
        for seed in seed_list:
            for glock_seed in our_seeds:
                if seed == glock_seed:  
                    index_seed_list.append(seed_list.index(seed))
                else: 
                    pass
                
        print(index_seed_list)
        time.sleep(5)
        if index_seed_list == []:

            print(f'gg not fund {datetime.now().time()}')
            driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[4]/div[1]/div[3]/div[4]/div/form/div/a').click()
            time.sleep(4)
            print('return')
            #main1()
        else:
            print(f'\033[2;31;43m --//--{index_seed_list}--//--  {datetime.now().time()} \033[0;0m') 
            for index_s in index_seed_list: ##это почти работает
                if index_s == 0:
                    time.sleep(3)
                    buttons[0].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 1:
                    time.sleep(3)
                    buttons[1].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 2:
                    time.sleep(3)
                    buttons[2].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 3:
                    time.sleep(3)
                    buttons[3].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 4:
                    time.sleep(3)
                    buttons[4].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 5:
                    time.sleep(3)
                    buttons[5].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 6:
                    time.sleep(3)
                    buttons[6].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 7:
                    time.sleep(3)
                    buttons[7].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 8:
                    time.sleep(3)
                    buttons[8].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    
                elif index_s == 9:
                    time.sleep(3)
                    buttons[9].click()
                    driver.current_window_handle
                    driver.find_element(By.ID, 'market_buynow_dialog_accept_ssa').click()
                    driver.current_window_handle
                    time.sleep(2)
                    driver.find_element(By.ID, 'market_buynow_dialog_purchase').click()
                    time.sleep(5)
                    driver.refresh()    



                else:
                    print('smth was wrong')
                    
                    time.sleep(5)

                    

                #print(market_items[index_s].text)



