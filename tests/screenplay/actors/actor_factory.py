from screenpy import Actor
from tests.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.fixtures.driver import create_driver

def create_actor(name="Marcos Felipe Camilo"):
    driver = create_driver()
    actor = Actor.named(name).who_can(BrowseTheWeb.using(driver))
    actor.driver = driver
    return actor