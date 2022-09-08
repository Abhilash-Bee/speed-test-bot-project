class CheckSpeed:

    def __init__(self, driver, by):
        self.driver = driver
        self.By = by
        self.download = None
        self.upload = None

    def go(self):
        go = self.driver.find_element(self.By.CSS_SELECTOR, ".start-text")
        go.click()

    def return_data(self):
        self.download = self.driver.find_element(self.By.CSS_SELECTOR, ".download-speed")
        print(self.download.text)

        self.upload = self.driver.find_element(self.By.CSS_SELECTOR, ".upload-speed")
        print(self.upload.text)
