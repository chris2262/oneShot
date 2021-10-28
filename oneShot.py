from sys import flags
import tkinter
from tkinter import ttk
from tkinter import font

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
import time


# root = tkinter.Tk()
# root.title("One Shot Reservation")
# root.geometry("400x600")
# frame = tkinter.Labelframe(root,text="계정 정보",fg="red")
# frame.pack(side="left")
# label1 = ttk.Label(frame, text="One Shot Reservation",padding=10)
# label1.pack()
# button1 = ttk.Button(frame, text="Exit", command=root.destroy)
# button1.pack()
# root.mainloop()

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# path  = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(path, chrome_options=chrome_options)

# driver.get("https://www.dgolfclub.com/")
# action_chains = ActionChains(driver)
# time.sleep(1)
# driver.find_element_by_id("cyberId").send_keys("na9038")
# driver.find_element_by_id("cyberPass").send_keys("dbrrkq12")
# driver.find_element_by_css_selector(".fr").click()
# time.sleep(3)
# driver.find_element_by_css_selector('[alt="골프예약"]').click()
# time.sleep(1)
# driver.find_element_by_css_selector('[alt="델피노CC"]').click()
# time.sleep(1)
# while True:
#     try:
#      driver.find_element_by_css_selector('[day="2021.10.3r0"]').click()
#      time.sleep(1)
#      action_chains.key_down("ENTER").perform()
#      break
#     except:
#         print("예약날짜 없음")
#         driver.find_element_by_css_selector('[alt="새로고침"]').click()
#         time.sleep(1)
# #driver.send_keys(Keys.ENTER)