import System
import HealthComponent
import RenderComponent

class HealthSystem(System.System):
    """
    Example system implementation.
    """
    def __init__(self, entity_manager):
        super().__init__(entity_manager)

    def update(self):        
        health_comp_name = HealthComponent.HealthComponent.__name__
        render_comp_name = RenderComponent.RenderComponent.__name__

        # first we get all the entities which have a health component
        entities = self.entityManager.getAllEntitiesPossessingComponentOfClass(health_comp_name)

        # iterate over all entites and update them
        for e in entities:
            # get the components (remember that will return None if not found)
            health_comp = self.entityManager.getComponentOfClass(e, health_comp_name)
            render_comp = self.entityManager.getComponentOfClass(e, render_comp_name)

            ## process the components
            # if entity is dead, continue to the next one
            if not health_comp.alive:
                continue
            # if entity has a max hp of zero, continue
            if health_comp.max_p == 0:
                continue
            # if hitpoints are below zero, we kill the entity
            if health_comp.current_hp <= 0:
                health_comp.alive = False
                # and then proceed to check if entity had a render component
                if render_comp:
                    # Process the dieing. 
                    # We should do some code like indicate that death animation
                    # should happen right now or similar things.
                    # This includes communicating with other components, probably,
                    # to do that just look how are we communicating with the
                    # render component and do the same.
                    # Another system should do the entity remove work.
                    pass
                else:
                    # we remove the entity directly
                    self.entityManager.removeEntity(e)








