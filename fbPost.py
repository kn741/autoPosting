
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class fbLoginModule:
    def __init__(self,account,password,postingSettings):
        self.settings = self.getSettings(account,password,postingSettings)
        
    def getSettings(self,account,password,postingSettings):
        postingPath = {}
        postingPath["私人"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div/span"
        postingPath["朋友"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/span"
        postingPath["公開"] = "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]"
        settings = {}
        settings["account"] = account
        settings["password"] = password
        settings["postingSettings"] = postingPath[postingSettings]
        settings["postingMessage"] = "Hello, this is a test message."
        return settings

    def login(self):
        settings = self.settings
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
        loginElement.send_keys(settings["account"])
        loginElement = driver.find_element(By.ID, "pass")
        loginElement.send_keys(settings["password"])
        loginElement = driver.find_element(By.NAME, "login")
        loginElement.click()
        
        try:
            for i in elementPath:
                postingElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, i)))
                postingElement.click()
        except:
            print("exception occurred.")
            driver.quit()
            return False
        postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]"))
        postingElement.send_keys(settings["postingMessage"])
        time.sleep(3)
        postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span"))
        # postingElement.click()
