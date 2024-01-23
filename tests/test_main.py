
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.auth_page import Auth_page
from pages.root_page import Root_page
from pages.catalog1_page import Catalog1_page
from pages.catalog2_page import Catalog2_page
from pages.catalog3_page import Catalog3_page
from pages.order_page import Order_page
from utilities.utils import Util

#BP1 = бизнес процесс покупки игры eldenring на сайте https://playgames.ru/ (Навигация по разделам магазина, переход в раздел про игры, установка фильтров, помещение товара в корзину. Самой покупки не предусмотрено
'''Инициация теста'''
def test_BP1():
    '''Передаем драйвер и класс утилиты'''
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('..\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    ut = Util(driver)


    print('Start test') #df

    '''Авторизация'''
    print('Start auth...')
    ap = Auth_page(driver)
    ap.auth() #Авторизуемся
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print('Auth is OK')
    print ('----------------')

    '''Инициация корневой страницы и переход в каталог 1 (Каталог всего про PS)'''
    print ('In Root page - go to catalog 1...')
    rp = Root_page(driver)
    rp.go_to_catalog1() #Идем в каталог 1
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print('In catalog 1 - OK')
    print ('----------------')

    '''Переход в каталог 2 (Каталог всего про PS5)'''
    print ('In catalog 1 - go to catalog 2...')
    cp1 = Catalog1_page(driver)
    cp1.go_to_catalog2() #Идем в каталог 2
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print('In catalog 2 - OK')
    print ('----------------')

    '''Переход в каталог 3 (Каталог игр для PS5)'''
    print('In catalog 2 - go to catalog 3...')
    cp2 = Catalog2_page(driver)
    cp2.go_to_catalog3() #Идем в каталог 3
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print('In catalog 3 - OK')
    print ('----------------')

    '''Начинаем выбор игры'''
    print('In catalog 3 - start choosing a game...')
    cp3 = Catalog3_page(driver)
    cp3.set_filters() #Устанавливаем 7 фильтров
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    cp3_price = cp3.get_price_cp3() #Сохраняем в переменную цену игры из каталога игр
    cp3.get_item() #Предмет в корзину
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print('Game successfully selected. Went to the order page - OK')
    print ('----------------')

    '''На странице заказа'''
    print('In order page - beginning to fill in the fields...')
    op = Order_page(driver)
    op_price = op.get_price_op() #Сохраняем в переменную цену игры из страницы заказа
    assert cp3_price == op_price #Проверяем цены на соответствие
    print('Price is OK')
    op.set_order_fields() #Заполняем данные по доставке на странице ордера
    time.sleep(1) #Для скриншота
    ut.get_screenshot()
    print ('----------------')

    print ('Finish test')
