from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class threadsLoginModule:
    def __init__(self,account,password,postingSettings,postingMessage):
        self.settings = self.getSettings(account,password,postingSettings,postingMessage)
        
    def getSettings(self,account,password,postingSettings,postingMessage):
        postingPath = {}
        postingPath["所有人"] = "/html/body/div[4]/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div[1]"
        postingPath["追蹤的個人檔案"] = "/html/body/div[4]/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div[2]"
        settings = {}
        settings["account"] = account
        settings["password"] = password
        settings["postingSettings"] = postingPath[postingSettings]  
        settings["postingMessage"] =  postingMessage
        return settings

    def login(self):
        settings = self.settings
        driver = webdriver.Chrome()
        options = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.threads.net/")

        elementPath = ["/html/body/div[2]/div/div/header/div[2]/nav/div[3]/div/div[1]/div[2]"
                ,"postingSettingsClick"
                ,settings["postingSettings"]
                ]
        
        loginElement = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div[3]/a")
        loginElement.click()
        loginElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[1]/input")))
        loginElement.send_keys(settings["account"])
        loginElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[2]/input")))
        loginElement.send_keys(settings["password"])
        loginElement = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[3]")
        loginElement.click()
        
        for i in elementPath:
            if i != "postingSettingsClick":
                postingElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, i)))
                postingElement.click()
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div")))
                script = "document.getElementsByClassName('x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz xp7jhwk x1y1aw1k x1sxyh0 xwib8y2 xurb0ha x1citr7e')[0].click()"
                driver.execute_script(script)

        
        
        postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div[1]/div[1]"))
        postingElement.send_keys(settings["postingMessage"])
        time.sleep(3)
        postingElement = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div"))
        # postingElement.click()
        
if __name__ == "__main__":
        module = threadsLoginModule("uraccount","urpassword","追蹤的個人檔案","Hello World!")
        module.login()
