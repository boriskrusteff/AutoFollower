from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as Ec

class AutoFollower:
    def __init__(self):
        self.option = Options()
        self.option.set_preference("dom.webnotifications.enabled", False)

        self.service = Service('./geckodriver')

        self.browser = Firefox(service=self.service, options=self.option)

        self.browser.get("https://www.instagram.com")
    
        accept_cookies = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div/div/button[2]')
            )
        )
        accept_cookies.click()

    def login(self, email, password_c):
        username = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
            )
        )
        username.send_keys(email)

        password = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
            )
        )
        password.send_keys(password_c)

        login_button = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
            )
        )
        self.browser.execute_script('arguments[0].click()', login_button)

        not_save = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
            )
        )
        not_save.click()
        return 'Login successful'

    def search(self, username):
        search_bar = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
            )
        )
        search_bar.send_keys(username)
        
        get_user = WebDriverWait(self.browser, 10).until(
            Ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div')
            )
        )
        get_user.click()
        
        try:
            follow = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button/div')
                )
            )
            follow.click()
            self.browser.quit()
            return username + "is followed"
        except TimeoutException:
            follow = WebDriverWait(self.browser, 10).until(
                Ec.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div')
                )
            )
            follow.click()
            self.browser.quit()
            return username + " is followed back"



auto_follower = AutoFollower()
print(
    auto_follower.login('baronabobi@gmail.com', 'hash1312')
)
print(
    auto_follower.search('therock')
)