
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Каталог всего про PS5 / Страница перенаправления в каталог игр для PS5/ https://playgames.ru/category/videoigry/playstation/playstation-5/ ---> https://playgames.ru/category/videoigry/playstation/playstation-5/igry-ps5/'''

class Catalog2_page(Base):


    # Creds
    catalog_ps5_all_url = 'https://playgames.ru/category/videoigry/playstation/playstation-5/'
    catalog_ps5_games_url = 'https://playgames.ru/category/videoigry/playstation/playstation-5/igry-ps5/'

    # Locators
    game_logo_loc = '/html/body/main/section/div[3]/div[2]/div[1]/div/div/div[2]/a/span[2]'

    # Elements
    def game_logo_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_logo_loc)))

    #Actions
    def press_game_logo(self):
        self.game_logo_elem().click()
        print ('Game logo clicked')

    # Methods
    def go_to_catalog3 (self): #Навигация по магазину
        self.assert_url(self.catalog_ps5_all_url) #Проверяем, что находися в каталоге всего про PS5
        self.press_game_logo()
        self.assert_url(self.catalog_ps5_games_url) #Проверяем, что перешли в каталог №3 - каталог игр для PS5
