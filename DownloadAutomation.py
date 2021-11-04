import time
from random import uniform
from selenium import webdriver

# "%D9%84%DB%8C%D9%88%D8%B1%D9%BE%D9%88%D9%84"

PATH = "C:\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.minimize_window()

def download_game():
    # time.sleep(uniform(60, 61))
    driver.get("https://video.varzesh3.com/tag/927733/%D8%AE%D9%84%D8%A7%D8%B5%D9%87-%D8%A8%D8%A7%D8%B2%DB%8C")
    time.sleep(uniform(4, 5))
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        link = elem.get_attribute("href")
        if "%D9%84%DB%8C%D9%88%D8%B1%D9%BE%D9%88%D9%84" in link:
            driver.get(link)
            break
    dl = driver.find_element_by_id('dropdownMenuButton')
    dl.click()
    time.sleep(uniform(1, 1.5))
    driver.find_element_by_xpath('//*[@id="page"]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/a[3]').click()
    time.sleep(uniform(1, 2))


download_game()
