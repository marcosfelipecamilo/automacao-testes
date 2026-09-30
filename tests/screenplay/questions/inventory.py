from tests.pages.inventory_page import InventoryPage

class InventoryPageIsLoaded:
    def answered_by(self, actor):
        browse_ability = actor.ability_to(type(actor.abilities[0]))
        driver = browse_ability.browser
        
        page = InventoryPage(driver)
        return page.is_loaded()