from utilities.handy_wrappers import HandyWrappers


class ExplicitlyWait:

    def __init__(self, driver,):
        self.driver = driver
        self.hw = HandyWrappers(driver)

