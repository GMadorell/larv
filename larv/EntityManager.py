# encoding: UTF-8
from larv.Entity import Entity
from larv.Component import Component

"""
Notes: -Decide whether getEntitiesHavingComponent should return an
        empty list or raise an exception when trying to access a component that 
        doesn't exist in the dictionary (now raises exception).
"""

"""
List of all methods:
    - componentsByClass property
    - entities property

    - generateNewId(self)
    - createEntity(self)    
    - removeEntity(self, entity)  

    - addComponent(self, entity, component)
    - removeComponent(self, entity, component)
    - hasComponent(self, entity, component)
    - getComponent(self, entity, component)
    - getComponentName(self, component)

    - getEntitiesHavingComponent(self, component)
    - getEntitiesHavingComponents(self, *args)
    - getComponentsOfEntity(self, entity)
    - getComponentsOfType(self, component)

"""

class EntityManager:
    """
    EntityManager is a object that acts as the 'database' of the system.
    It's used for looking up entities, getting their list of components, creating
    the entities (managing that they all have unique ID's), etc.

    When using components as arguments, you can use either a component of that
    type as the argument or (recommended) calling for the class_name of the component
    like so: EntityManager.getEntitiesHavingComponent(HealthComponent.__name__).

    NOTE: restricted to one component type per entity, so the same entity cannot
          have, as an example, two instances of HealthComponent. In order to change
          that -> 2nd dict value should be a list.
    """
    def __init__(self):
        """
        Constructor.
        @self.__entities: used for keeping all the active entities id's.
        @self.__components_by_class: dict that will hold a list of each type of components.
            -structure: dictionary of dictionaries:
                - key first dictionary = class name of component
                - value first dictionary = dictionary
                - key 2nd dictionary = entity id
                - value 2nd dictionary = the component itself
        @self.__lowest_assigned_id: used for assigning a id whenever a new entity is created.
        """        
        self.__entities = []
        self.__components_by_class = {}
        self.__lowest_assigned_id = 1

    @property
    def componentsByClass(self):
        return self.__components_by_class

    @property
    def entities(self):
        return self.__entities

    def generateNewId(self):
        """Returns a new unique ID."""
        n = self.__lowest_assigned_id
        self.__lowest_assigned_id += 1
        return n

    def createEntity(self):
        """
        Creates and returns a new entity object.
        Adds the entity to entity list.
        """
        # Generate new id and add the id to the list of entities
        new_id = self.generateNewId()
        self.__entities.append(new_id)
        # Create a new entity with the new id and return it
        new_entity = Entity(new_id)
        return new_entity

    def removeEntity(self, entity):
        """
        Removes the given entity from the entity manager.
        @entity: entity instance, not id.
        """
        assert isinstance(entity, Entity)
        assert entity.id in self.__entities

        for key, value in self.__components_by_class.items():
            if entity.id in value.keys():
                value.pop(entity.id)
        self.__entities.remove(entity.id)

    def addComponent(self, entity, component):
        """
        Adds the given component to the given entity.
        @entity: must be a entity instance, not an id.
        @component: component instance.
        """
        assert isinstance(entity, Entity)
        assert isinstance(component, Component)
        component_name = self.getComponentName(component)
        # Use setdefault so if it didn't exist we create a new dict
        second_dict = self.__components_by_class.setdefault(component_name, {})
        second_dict[entity.id] = component

        ## DEBUG
        # print(entity.id, )
        # print (self.__components_by_class)
        # return self.__components_by_class
        ## /DEBUG

    def removeComponent(self, entity, component):
        """
        Removes the given component of the given entity. If entity or component
        aren't found, this method does nothing.
        @entity: entity instance.
        @component: class name name or instance of the component.
        """
        assert isinstance(entity, Entity)
        if not isinstance(component, str):
            component = self.getComponentName(component)

        if component not in self.__components_by_class:
            return None
        if entity.id not in self.__components_by_class[component]:
            return None
        
        self.__components_by_class[component].pop(entity.id)

    def hasComponent(self, entity, component):
        """
        Returns True if given entity has given component, False instead.
        @entity: entity instance.
        @component: name or instance of the component.
        """
        assert isinstance(entity, Entity)
        if not isinstance(component, str):
            component = self.getComponentName(component)

        if component not in self.__components_by_class:
            return False
        if entity.id not in self.__components_by_class[component]:
            return False
        return True

    def getComponent(self, entity, component):
        """
        Given a entity and a component or a component type, returns the component 
        if the entity has it.
        Returns None if not found.
        @entity: must be a entity instance, not an id.
        @component: can be either a string or a component (which will be traduced
                    to a string internally).
        """
        assert isinstance(entity, Entity)
        if not isinstance(component, str):
            component = self.getComponentName(component)

        if component not in self.__components_by_class:
            return None
        if entity.id not in self.__components_by_class[component]:
            return None
        return self.__components_by_class[component][entity.id]

    def getEntitiesHavingComponent(self, component):
        """
        Returns a list of all the entities (not their id) that have the given 
        component.
        @component: class name or instance of the component.
        """
        # If component isn't a string, we transform it to a string
        if not isinstance(component, str):
            component = self.getComponentName(component)
        if component not in self.__components_by_class:
            raise KeyError('Error: \'{0}\' not found (component)'.format(component))
        # Then we iterate over the components dictionary and fill the return list
        entites_list = []
        comp_dict = self.__components_by_class[component]
        for key in comp_dict:
            entites_list.append(Entity(key))
        return entites_list

    def getEntitiesHavingComponents(self, *args):
        """
        Returns a list of all the entities that have all the args (which will be
        components).
        @args: indefinite tuple of arguments. They should all be components
               instances or components names.
        """
        ### THIS MAY BE VERY LOW PERFORMANCE!
        # Transform all components to their name if they weren't in string form.
        list_args = []
        for component in args:
            if not isinstance(component, str):
                component = self.getComponentName(component)
            list_args.append(component)

        # Get a set for every argument containing the id of those entities that 
        # have that argument.
        list_sets = []
        for component in list_args:
            new_set = set()
            for entity in self.getEntitiesHavingComponent(component):
                new_set.add(entity.id)
            list_sets.append(new_set)

        # Get the intersection of all the sets in order to get those entities that
        # have all the given components.
        final_set = list_sets[0]
        for set_ in list_sets[1:]:
            final_set = final_set.intersection(set_)

        return list(Entity(id_) for id_ in final_set)

    def getComponentsOfEntity(self, entity):
        """
        Returns a list of all the components that the given entity has.
        @entity: entity instance.
        """
        assert isinstance(entity, Entity)
        return_list = []
        for key, value in self.__components_by_class.items():
            component = value.get(entity.id, None)
            if component:
                return_list.append(component)
        return return_list

    def getComponentsOfType(self, component):
        """
        Returns a list of every component of the given type.
        @component: component class name or component instance.
        """
        if not isinstance(component, str):
            component = self.getComponentName(component)
        if component not in self.__components_by_class:
            raise KeyError('Error: \'{0}\' not found (component)'.format(component))
        return_list = []
        for value in self.__components_by_class[component].values():
            return_list.append(value)
        return return_list

    def getComponentName(self, component):
        """Given a component, returns it's name."""
        return component.__class__.__name__

if __name__ == '__main__':
    import HealthComponent
    import RenderComponent
    import pprint
    pp = pprint.PrettyPrinter(indent=1)
    # testing
    ent_man = EntityManager()
    new_entity = ent_man.createEntity()
    new_entity2 = ent_man.createEntity()
    new_entity3 = ent_man.createEntity()
    new_entity4 = ent_man.createEntity()

    new_component = HealthComponent.HealthComponent(5,10)
    new_component2 = RenderComponent.RenderComponent('test')

    ent_man.addComponent(new_entity, new_component)
    ent_man.addComponent(new_entity2, new_component)
    ent_man.addComponent(new_entity3, new_component)
    ent_man.addComponent(new_entity3, new_component2)

    # print(ent_man.getComponentOfClass(new_entity, new_component))
    # print(ent_man.getComponentOfClass(new_entity, new_component).alive)
    # name = ent_man.getComponentName(new_component)
    # # print(ent_man.getComponentOfClass(new_entity, name))
    # print(ent_man.getComponentOfClass(new_entity4, new_component)) # error testing

    # # check if remove entity works
    # pp.pprint(ent_man.componentsByClass)
    # print(ent_man.entities)
    # print('----')
    # ent_man.removeEntity(new_entity3)
    # pp.pprint(ent_man.componentsByClass)
    # print(ent_man.entities)

    # # check if getAllEntitiesPossessingComponentOfClass works
    # pp.pprint(ent_man.componentsByClass)
    # pp.pprint(ent_man.getAllEntitiesPossessingComponentOfClass(new_component))
    # pp.pprint(ent_man.getAllEntitiesPossessingComponentOfClass(HealthComponent.HealthComponent.__name__))


    # # check if removeComponent works:
    # pp.pprint(ent_man.componentsByClass)
    # ent_man.removeComponent(new_entity, HealthComponent.HealthComponent.__name__)
    # # ent_man.removeComponent(new_entity, new_component)
    # pp.pprint(ent_man.componentsByClass)        

    # # check if getComponentsOfEntity works:
    # pp.pprint(ent_man.componentsByClass)
    # pp.pprint(ent_man.getComponentsOfEntity(new_entity3))
    # pp.pprint(ent_man.getComponentsOfEntity(ent_man.createEntity()))

    #check if getEntitiesHavingComponents works:
    pp.pprint(ent_man.componentsByClass)
    pp.pprint(ent_man.getEntitiesHavingComponents(HealthComponent.HealthComponent.__name__,
                                                  RenderComponent.RenderComponent.__name__))
