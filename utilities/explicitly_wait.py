
class explicitlyWait:

    def wait_for_element(self, locator, locatorType='id',
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            print('Waiting for maximum ::' + str(timeout) +
                  ' :: seconds for element to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, 'stopFilter_stops-0')))
            print('Element appeared on the web page')
        except:
            print('Element not appeared on the web page')
            print_stack()
        return element