
# https://playgames.ru/  <- Объект тестирования

'''Set Base class'''
class Base():
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url = {get_url}')

    '''Method - check for word. Принимает элемент и проверяемое слово'''
    def assert_word(self, elem, target_word):
        assert elem.text == target_word
        print(f'Name is OK = {elem.text}')

    '''Method current url check. Проверяет соответствует ли текущая url той, которая должна быть'''
    def assert_url(self, target_url):
        get_url = self.driver.current_url
        assert get_url == target_url
        print(f'Target url is OK = {target_url}')
