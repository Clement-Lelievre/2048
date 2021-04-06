#import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

'''This script does the following:
-opens firefox
-goes to a 2048 page
-enlarges the page and removes a banner
-plays games until its best score is over the inputted number
-once the best score reaches input, it closes the browser
-finally, script writes its best score and indicates the game number (this is also the last game number)
'''
target = input('What minimum score do you want to reach?\n')
driver = webdriver.Firefox() 
driver.get("https://play2048.co/")

time.sleep(2)
driver.maximize_window()

try:
    cookie = driver.find_element_by_class_name('ezmob-footer-close')
    # cookie = driver.find_element_by_class_name('cc_btn cc_btn_accept_all')
    cookie.click()
except:
    pass



elem = driver.find_element_by_tag_name('html')
gamenumber = 0

def newgame():
    status = driver.find_element_by_class_name('game-container')
    status = str(status.text)
    
    while "Game over!" not in status:      
        elem.send_keys(Keys.UP)
        status = driver.find_element_by_class_name('game-container')
        status = str(status.text)
        elem.send_keys(Keys.RIGHT)
        status = driver.find_element_by_class_name('game-container')
        status = str(status.text)
        elem.send_keys(Keys.DOWN)
        status = driver.find_element_by_class_name('game-container')
        status = str(status.text)
        elem.send_keys(Keys.LEFT)
        status = driver.find_element_by_class_name('game-container')
        status = str(status.text)
       
    bestscore = str(driver.find_element_by_class_name('best-container').text)
    if int(bestscore) <= int(target): 
        newgame = driver.find_element_by_class_name('restart-button') 
        newgame.click()
        
    else:
        print('My best score during this playing session is',bestscore,', achieved during game number',gamenumber+1,'!')
        time.sleep(2)
        driver.quit()
        quit()
    
    pass

while True:
    newgame()
    gamenumber += 1




