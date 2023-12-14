
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Каталог всего про PS / Страница перенаправления в каталог всего про PS5'''

class Catalog1_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Creds
    catalog_ps_all_url = 'https://playgames.ru/category/videoigry/playstation/'
    catalog_ps5_all_url = 'https://playgames.ru/category/videoigry/playstation/playstation-5/'

    # Locators
    ps5_logo_loc = '//*[@alt="PlayStation 5"]'

    # Elements
    def ps5_logo_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ps5_logo_loc)))

    #Actions
    def press_ps5_logo(self):
        self.ps5_logo_elem().click()
        print ('PS5 logo clicked')

    # Methods
    def go_to_catalog2 (self):
        self.assert_url(self.catalog_ps_all_url) #Проверяем, что находимся в каталоге всего про PS
        self.press_ps5_logo()
        self.assert_url(self.catalog_ps5_all_url) #Проверяем, что перешли в каталог №2 - каталог всего что касается PS5
