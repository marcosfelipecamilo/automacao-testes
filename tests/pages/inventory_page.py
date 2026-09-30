class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url