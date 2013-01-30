import larv

from ..Components import PositionComponent
from ..Components import RenderComponent

class RenderSystem(larv.System):
    """
    Takes all the components that have:
        - PositionComponent
        - RenderComponent
    and calls surface.blit on all of them (paints them on the screen).
    """
    def __init__(self, surface):
        self.surface = surface

    def update(self):
        list_entities = self.entityManager.getEntitiesHavingComponents(
                            PositionComponent.__name__,
                            RenderComponent.__name__)

        for entity in list_entities:
            position_comp = self.entityManager.getComponent(entity, PositionComponent.__name__)
            render_comp = self.entityManager.getComponent(entity, RenderComponent.__name__)

            x = position_comp.x
            y = position_comp.y
            self.surface.blit(render_comp.sprite, (x, y))

if __name__ == "__main__":
    __package__ = "barebones_project"