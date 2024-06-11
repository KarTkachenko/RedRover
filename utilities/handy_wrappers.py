import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.logger as lg


class HandyWrappers:
    log = lg.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info('Locator type ' + locator_type + ' not correct/supported')
        return False

    # def is_element_present(self, locator, by_type):
    #     try:
    #         element = self.driver.find_element(by_type, locator)
    #         if element is not None:
    #             self.log.info('The element is present')
    #             return True
    #         else:
    #             return False
    #     except:
    #         self.log.info('The element is NOT present')
    #         return False
    #
    # def element_presence_check(self, locator, by_type):
    #     try:
    #         element = self.driver.find_elements(by_type, locator)
    #         if len(element) > 0:
    #             self.log.infot('The element is found')
    #             return True
    #         else:
    #             return False
    #     except:
    #         self.log.info('The element is NOT found')
    #         return False

    def wait_for_element(self,  locatorType='id',
                         timeout=10):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            self.log.info('Waiting for maximum ::' + str(timeout) +
                          ' :: seconds for element to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType, 'stopFilter_stops-0')))
            self.log.info('Element appeared on the web page')
        except:
            self.log.info('Element not appeared on the web page')
            print_stack()
        return element
