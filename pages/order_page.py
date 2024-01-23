
import time
from base.base_set import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Страница заказа (корзина) https://playgames.ru/order/'''

class Order_page(Base):


    # Creds
    order_page_url = 'https://playgames.ru/order/'
    item_name = 'Elden Ring [PS5]' #название будем проверять по совпаданию, а цену по значению из предыдущей страницы (страницы каталога игр)
    last_name = 'Test001'
    phone = '89855555555'
    city = 'Акша'
    adress = 'д.123'
    zip_id = '121346'

    # Locators
    last_name_loc = '//*[@id="wa-step-auth-section"]/div/form/div/div[2]/input'
    phone_loc = '//*[@id="wa-step-auth-section"]/div/form/div/div[3]/input'
    region_loc = '//*[@id="wa-step-region-section"]/div/form/div[2]/div[2]/div/select/option[14]'
    city_loc = '//*[@id="wa-step-region-section"]/div/form/div[2]/div[3]/input'
    adress_loc = '//*[@id="wa-step-details-section"]/div/form/div[3]/div/div[1]/input'
    zip_loc = '//*[@id="wa-step-details-section"]/div/form/div[3]/div/div[2]/input'
    price_loc = 'wa-price'
    item_name_loc = 'wa-name'

    # Elements
    def last_name_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_loc)))
    def phone_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_loc)))
    def region_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region_loc)))
    def city_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_loc)))
    def adress_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_loc)))
    def zip_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_loc)))
    def item_name_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.item_name_loc)))

    #Actions
    def enter_last_name(self):
        self.last_name_elem().send_keys(self.last_name)
        print ('Last name entered')
    def enter_phone(self):
        self.phone_elem().send_keys(self.phone)
        print ('Phone entered')
    def enter_region(self):
        self.region_elem().click()
        print ('Region entered')
    def enter_city(self):
        self.city_elem().send_keys(self.city)
        print ('City entered')
    def enter_adress(self):
        self.adress_elem().send_keys(self.adress)
        print ('Adress entered')
    def enter_zip(self):
        self.zip_elem().send_keys(self.zip_id)
        print ('ZIP entered')

    # Methods
    def set_order_fields(self): #Заполняем данные по доставке
        self.assert_url(self.order_page_url) #Проверяем, что находится на странице заказа
        self.assert_word(self.item_name_elem(), self.item_name)
        self.enter_last_name()
        self.enter_phone()
        self.enter_region()
        self.enter_city()
        time.sleep(5) #Системе нужно обработать информацию, после чего она отобразит доп.поля
        self.enter_adress() #Заполняем их
        self.enter_zip()
        # По задумке тут завершается бизнес-процесс. Я не буду взаимодействовать с кнопкой "Подтвердить заказ"

    def get_price_op(self): #Метод понадобится при сравнении цены товара с текущей страницы (страницы заказа) и предыдущей страницы (страницы каталога игр)
         price_op = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.price_loc)))
         return price_op.text
