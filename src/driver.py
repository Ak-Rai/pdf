# import time
# from decouple import config
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
#
#
#
# def init():
#     try:
#         chrome_options = Options()
#         # chrome_options.add_argument("--headless")
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         driver.get("https://smallseotools.com/plagiarism-checker/")
#         time.sleep(1)
#
#         time.sleep(1)
#         driver.quit()
#     except:
#         print('Error')
#
#
#
# # init()