from multiprocessing import Pool
from bs4 import BeautifulSoup as bs
from dynamic_pattern_list import glock_moonrise, wvgalil, p250_Nevermore, glock_highbeam
import random
import time
import os
from datetime import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def parsing(url):
    our_seeds = glock_moonrise
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension('C:/Users/chernov/Desktop/pattern/item-hunter.cs/sih.crx')
    #chrome_options.add_extension('C:/Users/chernov/Desktop/pattern/item-hunter.cs/gmp.crx')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1900, 1000)
    ac = ActionChains(driver)

    time.sleep(3)
     #ТуТ НУЖНО ЗАКРЫТЬ ВКЛАДКУ GMP
    driver.get(url)
    time.sleep(2)
    for cookie in pickle.load(open('cookies','rb')):
        driver.add_cookie(cookie)
    driver.refresh()
    driver.find_element(By.XPATH, '//*[@id="listings"]/div[5]/div[1]/div[1]/div[1]/div[2]/label/span[1]').click()
    ac.scroll_by_amount(0, 1000).perform()
    #ac.move_by_offset(1340, 80).click().perform() # с помощью этой штуки сделать кнопки гг
    time.sleep(3)
    buy_status = ''
    while buy_status == '':
        time.sleep(8) #тут вся уйя
        #ac.scroll_by_amount(0, 500).perform()
        
        #driver.execute_script("window.scrollBy(0,2000)","")
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
        sleep = random.randint(10, 60)        
        print(index_seed_list)
        time.sleep(5)
        if index_seed_list == []:
            if url == 'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Glock-18%20%7C%20Moonrise%20%28Factory%20New%29':
                process_num = '1'
                name = 'StatTrak Glock-18 Moonrise (FN)'
            elif url == 'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Glock-18%20%7C%20Moonrise%20%28Minimal%20Wear%29':
                process_num = '2'
                name = 'StatTrak Glock-18 Moonrise (MW)'
            elif url == 'https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Factory%20New%29':
                process_num = '3'
                name = 'Glock-18 Moonrise (FN)'
            else:
                pass
            print(f'gg not fund {process_num} {datetime.now().time()}')
            print(f'process {process_num} will be return in {sleep}')
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[4]/div[1]/div[3]/div[4]/div/form/div/a').click()
            
            
            #time.sleep(sleep)
            #main1()
        else:
            print(f'\033[2;31;43m --//--{index_seed_list + name}--//--  {datetime.now().time()}\033[0;0m') 
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
                    print('ИДИ НАХУЙ')
                    
                    time.sleep(5)
    #driver = webdriver.Chrome()
    #
    #driver.get(url)
    #text = driver.page_source
    #time.sleep(15)
    #driver.close()
    #
    #print(text)


if __name__ == '__main__':
    url_list = ['https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Glock-18%20%7C%20Moonrise%20%28Factory%20New%29',
                'https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Glock-18%20%7C%20Moonrise%20%28Minimal%20Wear%29', 
                'https://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Moonrise%20%28Factory%20New%29'] # Перенес
    pool = Pool(processes=3)
    pool.map(parsing, url_list)
    
    


   