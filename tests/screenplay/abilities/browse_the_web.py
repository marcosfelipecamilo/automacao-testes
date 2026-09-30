class BrowseTheWeb:
    """Habilidade que encapsula a instância do Selenium WebDriver."""
    def __init__(self, driver):
        self.browser = driver

    @staticmethod
    def using(driver):
        return BrowseTheWeb(driver)