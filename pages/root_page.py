
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Корневая страница - страница предназначена для перенаправления в каталог всего что касается PS '''

class Root_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Creds
    start_url = 'https://playgames.ru/'
    catalog_ps_all_url = 'https://playgames.ru/category/videoigry/playstation/'

    # Locators
    catalog_button_loc = '//*[@class="b-catalog"]'
    ps_logo_loc = '//*[@alt="PlayStation"]'

    # Elements
    def catalog_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button_loc)))
    def ps_logo_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ps_logo_loc)))

    #Actions
    def press_catalog_button(self):
        self.catalog_button_elem().click()
        print ('Catalog button clicked')
    def press_ps_logo(self):
        self.ps_logo_elem().click()
        print('PS Logo clicked')

    # Methods
    def go_to_catalog1 (self):
        self.assert_url(self.start_url) #Проверяем, что находимся на стартовой url
        self.press_catalog_button()
        self.press_ps_logo()
        self.assert_url(self.catalog_ps_all_url) #Проверяем, что перешли в каталог №1 - каталог всего что касается PS
