import pytest
from tests.screenplay.actors.actor_factory import create_actor
from tests.screenplay.tasks.login import PerformLogin
from tests.screenplay.questions.inventory import InventoryPageIsLoaded

@pytest.mark.smoke
def test_login_com_sucesso():
    actor = create_actor("Marcos Felipe Camilo")
    try:
        actor.attempts_to(
            PerformLogin.with_credentials("standard_user", "secret_sauce")
        )
        assert InventoryPageIsLoaded().answered_by(actor)
    finally:
        actor.driver.quit()