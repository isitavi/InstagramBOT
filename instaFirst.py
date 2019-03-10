from selenium import webdriver
from time import sleep


class Instagram:
    def __init__(self, userName="trollmonst3r", usrPwd="m6nrUfwC9yEfzrR", targetUser="trollfootballhq", dwnldPath="/ home/null_byt3/Desktop/instagram"):
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
        loginBtn = self.driver.find_element_by_xpath(
            "//button[contains(.,'Log in')]")
        usernameField = self.driver.find_element_by_xpath(
            "//input[@name='username'][@type='text']")
        usernameField.send_keys(self.username)
        passwordField = self.driver.find_element_by_xpath(
            "//input[@name='password'][@type='password']")
        passwordField.send_keys(self.userpassword)
        loginBtn.click()

    def popupNotify(self):
        try:
            sleep(2)
            notnowBtn = self.driver.find_element_by_xpath(
                "//button[contains(.,'Not Now')]")
            # HoLwm
            notnowBtn.click()
            sleep(2)
        except Exception:
            pass

    def searchTarget(self):
        searchBox = self.driver.find_element_by_xpath(
            "//input[@placeholder='Search']")
        searchBox.send_keys(self.targetuser)
        targetUserURL = self.baseURL+self.targetuser+'/'
        self.driver.get(targetUserURL)
        sleep(3)

    def scrollToInsta(self):
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


if __name__ == "__main__":
    Instagram()
