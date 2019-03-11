import os
from selenium import webdriver
from time import sleep


class Instagram:
    def __init__(self, userName="trollmonst3r", usrPwd="m6nrUfwC9yEfzrR", targetUser="trollfootballhq", dwnldPath="/home/null_byt3/Desktop/instagram"):
        self.error = False
        if self.error is False:
            if os.path.exists(dwnldPath):
                print('Download path already exists!!')
            else:
                os.mkdir(dwnldPath)
        else:
            print('Something wrong plese debug your code!!')

        self.username = userName
        self.userpassword = usrPwd
        self.targetuser = targetUser
        self.downloadpath = dwnldPath
        self.driver = webdriver.Chrome("./chromedriver")
        self.loginurl = "https://www.instagram.com/accounts/login/"
        self.baseURL = "https://www.instagram.com/"
        self.driver.get(self.loginurl)
        self.logIn()
        self.popupNotify()
        self.searchTarget()
        self.scrollToInsta()
        input('stop')
        self.driver.close()

    def logIn(self):
        try:
            loginBtn = self.driver.find_element_by_xpath(
                "//button[contains(.,'Log in')]")
            try:
                usernameField = self.driver.find_element_by_xpath(
                    "//input[@name='username'][@type='text']")
                usernameField.send_keys(self.username)
                passwordField = self.driver.find_element_by_xpath(
                    "//input[@name='password'][@type='password']")
                passwordField.send_keys(self.userpassword)
                loginBtn.click()
            except Exception:
                print('Something wrong while inserting username and password')
        except Exception:
            self.error = True
            print('Something wrong')

    def popupNotify(self):
        try:
            sleep(2)
            notnowBtn = self.driver.find_element_by_xpath(
                "//button[contains(.,'Not Now')]")
            notnowBtn.click()
            sleep(2)
        except Exception:
            pass

    def searchTarget(self):
        try:
            searchBox = self.driver.find_element_by_xpath(
                "//input[@placeholder='Search']")
            searchBox.send_keys(self.targetuser)
            targetUserURL = self.baseURL+self.targetuser+'/'
            self.driver.get(targetUserURL)
            sleep(3)
        except Exception:
            self.error = True
            print('Something wrong while finding username')

    def scrollToInsta(self):
        try:
            numberofPosts = self.driver.find_element_by_xpath(
                "//span[@class='g47SY ']")
            numberofPosts = str(numberofPosts.text)
            self.numberofPosts = int(numberofPosts)

            if self.numberofPosts > 24:
                noOfScrolls = int(self.numberofPosts/24) + 3

                for allScrolls in range(noOfScrolls):
                    print(allScrolls)
                    self.driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")
                    sleep(1)
        except Exception:
            self.error = True
            print('Something wrong happend while scrolling all posts')


if __name__ == "__main__":
    Instagram()
