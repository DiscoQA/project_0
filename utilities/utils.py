
from base.base_set import Base
import datetime

'''Utils'''
class Util(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Screenmaker'''
    def get_screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_scr = f'Screen_{current_date}.png'
        self.driver.save_screenshot('.\\screen\\' + name_scr)
