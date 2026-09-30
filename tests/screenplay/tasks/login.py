from tests.pages.login_page import LoginPage

class PerformLogin:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def perform_as(self, actor):
        # Obtém o navegador a partir da habilidade do ator
        browse_ability = actor.ability_to(type(actor.abilities[0]))
        driver = browse_ability.browser
        
        page = LoginPage(driver)
        page.open()
        page.login(self.user, self.password)

    @staticmethod
    def with_credentials(user, password):
        return PerformLogin(user, password)