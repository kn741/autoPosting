from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class twitterLoginModule:
    def __init__(self,account,password,postingSettings,postingMessage,verificationAccount):
        self.settings = self.getSettings(account,password,postingSettings,postingMessage,verificationAccount)
        
    def getSettings(self,account,password,postingSettings,postingMessage,verificationAccount):
        postingPath = {}
        postingPath["所有人"] = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]"
        postingPath["你跟隨的帳戶"] = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]"
        postingPath["已認證的帳戶"] = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[3]"
        settings = {}
        settings["account"] = account
        settings["password"] = password
        settings["postingSettings"] = postingPath[postingSettings]
        settings["postingMessage"] =  postingMessage
        settings["verificationAccount"] = verificationAccount
        return settings

    def login(self):
        settings = self.settings
        driver = webdriver.Chrome()
        options = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://twitter.com/")

        elementPath = [
                "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div"
                ,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div"
                ,settings["postingSettings"]
                ]

        loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div"))) 
        loginElement.click()
        loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
        loginElement.send_keys(settings["account"])
        loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")))
        loginElement.click()
        try:
            loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")))
            loginElement.send_keys(settings["verificationAccount"])
            loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")))
            loginElement.click()
        except:
            print("No varification page found.")
        loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
        loginElement.send_keys(settings["password"])
        loginElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")))
        loginElement.click()
        
        try:
            for i in elementPath:
                postingElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, i)))
                postingElement.click()
        except:
            print("exception occurred.")
            driver.quit()
            return False
        postingElement = WebDriverWait(driver, 60).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"))
        postingElement.send_keys(settings["postingMessage"])
        time.sleep(3)
        postingElement = WebDriverWait(driver, 60).until(lambda d: d.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]"))
        postingElement.click()
        
if __name__ == "__main__":
        module = twitterLoginModule("uraccount","urpassword","所有人","Hello World!","urverify")
        module.login()