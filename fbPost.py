account = "urAccount"
password = "urPassword"

def getSettings():
    
    postingPath = {}
    postingPath["私人"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[6]/div/div/div[2]/div[1]/div/div"
    postingPath["朋友"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/span"
    postingPath["所有人"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]"
    settings = {}
    settings["account"] = account
    settings["password"] = password
    settings["postingSettings"] = postingPath["私人"]
    settings["postingMessage"] = "Hello, this is a test message."
    return settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
settings = getSettings()
driver = webdriver.Chrome()
options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

elementPath = ["/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span"
               ,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div/span/div/div/div/span"
               ,settings["postingSettings"]
               ,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/span/span"
               ]

loginElement = driver.find_element(By.ID, "email")
loginElement.send_keys(account)
loginElement = driver.find_element(By.ID, "pass")
loginElement.send_keys(password)
loginElement = driver.find_element(By.NAME, "login")
loginElement.click()

for i in elementPath:
    postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, i))
    postingElement.click()

postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]"))
postingElement.send_keys(settings["postingMessage"])


time.sleep(3)

postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span"))
postingElement.click()

