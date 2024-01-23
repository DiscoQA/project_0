
import time
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


'''Каталог игр для PS5 / Установка фильтров + Выбор товара + Переход в корзину. https://playgames.ru/category/videoigry/playstation/playstation-5/igry-ps5/ ---> https://playgames.ru/order/'''

class Catalog3_page(Base):


    # Creds
    catalog_ps5_games_url = 'https://playgames.ru/category/videoigry/playstation/playstation-5/igry-ps5/'
    price_1 = '4000'
    price_2 = '6000'
    order_url = 'https://playgames.ru/order/'

    # Locators
    filter_1_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[1]/div[2]/div/label[4]'
    filter_2_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[2]/div[2]/div/label[2]'
    filter_3_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[5]/div[1]'
    filter_4_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[5]/div[2]/div/label[8]'
    filter_5_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[6]/div[1]'
    filter_6_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[6]/div[2]/input[1]'
    filter_7_loc = '/html/body/main/section/div[3]/div[1]/div[4]/div/div/form/div[6]/div[2]/input[2]'
    elden_ring_ps5_add_to_cart_loc = '/html/body/main/section/div[3]/div[2]/div/div[3]/div/div/div/form/div[2]/div/button'
    go_to_cart_button_loc = '/html/body/div[2]/div/div/div[2]/div[3]/a'
    item_price_loc = 'products__price-new'

    # Elements
    def filter_1_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_1_loc)))
    def filter_2_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_2_loc)))
    def filter_3_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_3_loc)))
    def filter_4_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_4_loc)))
    def filter_5_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_5_loc)))
    def filter_6_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_6_loc)))
    def filter_7_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_7_loc)))
    def elden_ring_ps5_add_to_cart_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.elden_ring_ps5_add_to_cart_loc)))
    def go_to_cart_button_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button_loc)))

    #Actions
    def set_filter_1(self):
        self.filter_1_elem().click()
        print ('Filter 1 is ok')
    def set_filter_2(self):
        self.filter_2_elem().click()
        print ('Filter 2 is ok')
    def set_filter_3(self):
        self.filter_3_elem().click()
        print ('Filter 3 is ok')
    def set_filter_4(self):
        self.filter_4_elem().click()
        print ('Filter 4 is ok')
    def set_filter_5(self):
        self.filter_5_elem().click()
        print ('Filter 5 is ok')
    def set_filter_6(self):
        self.filter_6_elem().send_keys(self.price_1)
        print ('Filter 6 is ok')
    def set_filter_7(self):
        self.filter_7_elem().send_keys(self.price_2)
        for x in range(len(self.price_2)): # тут походу минорный баг. Не удается отправить в поле 6000, тк при клике оно автоматически заполняется максимальным значением, а потом добавляется 6000 к концу
            self.filter_7_elem().send_keys(Keys.ARROW_LEFT)
        for x in range(5):
            self.filter_7_elem().send_keys(Keys.BACKSPACE)
        print ('Filter 7 is ok')
    def press_elden_ring_ps5_add_to_cart(self):
        self.elden_ring_ps5_add_to_cart_elem().click()
        print ('Item added to cart')
    def press_go_to_cart_button(self):
        self.go_to_cart_button_elem().click()
        print ('Go to cart button clicked')

    # Methods
    def set_filters(self): #Устанавливаем 7 фильтров
        self.assert_url(self.catalog_ps5_games_url) #Проверяем, что находимся к каталоге игр для PS5
        self.set_filter_1()
        self.set_filter_2()
        self.set_filter_3()
        self.set_filter_4()
        self.set_filter_5()
        self.set_filter_6()
        self.set_filter_7()
        print('Подождем пока применятся фильтры')
        time.sleep(7) # Система в 30% случаев не успевает отреагировать на изменение фильтров из-за чего в выборку иногда попадает ошибочный товар. Задержка помогает
    def get_item(self): #Предмет в корзину
        self.press_elden_ring_ps5_add_to_cart()
        self.press_go_to_cart_button()
        self.assert_url(self.order_url) #Проверяем, что попали на страницу заказа после выбора товара
    def get_price_cp3(self): #Метод понадобится при сравнении цены товара с текущей страницы (страницы каталога игр) и страницы заказа
         price_cp3 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.item_price_loc)))
         return price_cp3.text
