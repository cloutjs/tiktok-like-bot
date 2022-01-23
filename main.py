from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options 
import os
from os import system
import sys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    browser.get("https://zefoy.com")
    browser.set_window_size(1920, 1080)
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button"))
    )
    browser.set_window_position(-10000, 0)
    likes()

def likes():
    while True:
        system("title " + "TikTok Liker // Botting // by clout")
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        time.sleep(1)
        print("[+] Loaded Zefoy")
        browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(url)
        print("[+] Link checked")
        time.sleep(1)
        try:
            print("[+] Checking Timer")
            time.sleep(1.3)
            browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
            time.sleep(1.5)
            browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
            print("[+] Likes succesfully sent")
            browser.refresh()
            cls()
            seconds = 900
            while (1 < seconds):
                system("title " + "TikTok Liker // Botting // by clout")
                print("{} seconds cooldown left.".format(seconds))
                time.sleep(1)
                seconds = seconds - 1
                cls()
        except:
            cls()
            print("You are still on cooldown! Try again in a few minutes.")
            browser.quit()
            input("\nPress any key to quit")
            sys.exit()

system("title " + "TikTok Liker // by clout")
url = input("Link? ")
if not "tiktok" in url:
    cls()
    system("title " + "TikTok Liker // Error // by clout")
    print("Invalid URL. Please restart the bot.")
    time.sleep(5)
    sys.exit()
time.sleep(1)
cls()
system("title " + "TikTok Liker // Captcha // by clout")
print("please solve the captcha")
time.sleep(2)
browser = webdriver.Chrome(options=options)
menu()