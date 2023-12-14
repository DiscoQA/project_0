
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Страница авторизации'''

class Auth_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Creds
    start_url = 'https://playgames.ru/'
    user_mail = 'bf4disco@gmail.com'
    user_pass = 'qwerty123'
    auth_page_url = 'https://playgames.ru/login/'
    profile_url = 'https://playgames.ru/my/profile/'
    user_credo = 'Andrew_1'

    # Locators
    auth_button_loc = '/html/body/header[1]/div[1]/div/div/div[4]/div/a'
    login_field_loc = '//*[@name="login"]'
    password_field_loc = '//*[@name="password"]'
    rememberme_button_loc = '//*[@class="in-checkbox__element"]'
    login_button_loc = '//*[@class="wa-login-submit"]'
    profile_button_loc = '//*[@href="/my/profile/"]'
    profile_name_in_sys_loc = '/html/body/main/div/div[2]/div/div[2]/div[2]'

    # Elements
    def auth_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.auth_button_loc)))
    def login_field_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_field_loc)))
    def password_field_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field_loc)))
    def rememberme_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rememberme_button_loc)))
    def login_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_loc)))
    def profile_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_button_loc)))
    def profile_name_in_sys_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_name_in_sys_loc)))

    #Actions
    def press_auth_button(self):
        self.auth_button_elem().click()
        print ('Auth button clicked')
    def enter_user_name(self):
        self.login_field_elem().send_keys(self.user_mail)
        print('User Name entered')
    def enter_user_pass(self):
        self.password_field_elem().send_keys(self.user_pass)
        print('User password entered')
    def declick_remember_me_button(self):
        self.rememberme_button_elem().click()
        print('Remember me button is off')
    def press_login_button(self):
        self.login_button_elem().click()
        print('Login button clicked')
    def press_profile_button(self):
        self.profile_button_elem().click()
        print('Profile button clicked')

    # Methods
    def auth (self):
        self.driver.get(self.start_url)
        self.driver.maximize_window()
        self.assert_url(self.start_url) #Проверяем соответствие текущей url заданной стартовой url
        self.press_auth_button()
        self.assert_url(self.auth_page_url) #Проверяем соответствие текущей url заданной auth_page_url.
        self.enter_user_name()
        self.enter_user_pass()
        self.declick_remember_me_button()
        self.press_login_button()
        self.get_current_url()
        self.press_profile_button()
        self.assert_url(self.profile_url) #Проверяем соответствие текущей url заданной profile_url.
        self.assert_word(self.profile_name_in_sys_elem(), self.user_credo) #Проверяем отображаемое имя в системе и заданное имя на соответствие
        self.driver.back()
        self.assert_url(self.start_url) #Проверяем, что вернулись на начальную страницу после авторизации
