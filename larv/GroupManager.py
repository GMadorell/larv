# -*- coding: UTF-8 -*-
import larv
import pprint

class GroupManager:
    """
    Allows the entity manager to add entities to groups and fetch for them.
    For example, we could have a group called 'hero' and add the hero to it,
    and then we could fetch for all the entities that are from the 'hero'
    group, getting only the hero, obviously.

    Usage:
      Binded to Factories and Systems by default (when they're assigned to a 
      engine, the engine does that in the background), as they're where the 
      GroupManagers will be most used.
      Basic usage is:
        - At the factory, when the entity gets created it might be assigned to a
          group.
        - In some systems, it may be convenient to ask for a certain group
          of entities. For example, a system that only acts on the Hero, may
          call for it using self.group_manager.get('hero')
    """
    def __init__(self, engine):
        """
        Constructor.
        @engine: larv.Engine.Engine instance.
        @entitiesByGroup: dictionary, key = group, value = set of entities
        """
        assert isinstance(engine, larv.Engine)
        self.engine = engine
        self.entitiesByGroup = {}

    def add(self, entity, group):
        """
        Adds the given entity to the given grup.
        Note that a entity can't be in the same group twice.
        @entity: lard.Entity.Entity instance
        @group: name (string) of the group
        """
        assert isinstance(entity, larv.Entity)
        assert isinstance(group, str)
        group = group.lower()
        set_entities = self.entitiesByGroup.setdefault(group, set())
        set_entities.add(entity.id)

    def remove(self, entity, group):
        """
        Removes the given entity from the given group.
        @entity: lard.Entity.Entity instance
        @group: name (string) of the group
        """
        assert isinstance(entity, larv.Entity)
        assert isinstance(group, str)
        group = group.lower()
        set_entities = self.entitiesByGroup.get(group, None)
        if set_entities:
            set_entities.remove(entity.id)

    def removeCompletely(self, entity):
        """
        Removes given entity from all groups.
        @entity: larv.Entity.Entity instance.
        """
        assert isinstance(entity, larv.Entity)
        for value in self.entitiesByGroup.values():
            if entity.id in value:
                value.remove(entity.id)

    def get(self, *args):
        """
        Returns a list of all the entities that are in every arg (which are supposed
        to be groups).
        When used with one arg (most common use), will return only the entities
        that are in that group.
        @*args: name (string) of the groups that will be fetched.
        """
        for arg in args:
            assert isinstance(arg, str)

        return_set = set()
        for arg in args:
            if return_set:
                return_set = return_set & self.entitiesByGroup[arg.lower()] # intersection
            else:
                return_set = self.entitiesByGroup[arg.lower()]

        return list(larv.Entity(id_) for id_ in return_set)

    def getGroups(self, entity):
        """
        Returns a list of all the groups the entity is part of.
        @entity: larv.Entity.Entity instance
        """
        assert isinstance(entity, larv.Entity)
        group_names = []
        for key, value in self.entitiesByGroup.items():
            if entity.id in value:
                group_names.append(key)
        return group_names

    def isInGroup(self, entity, group):
        """
        Returns True if the given entity is contained in the given group, 
        False otherwise.
        @entity: larv.Entity.Entity instance
        @group: name (string) of the group
        """
        assert isinstance(entity, larv.Entity)
        assert isinstance(group, str)
        return entity.id in self.entitiesByGroup[group.lower()]

    def doesGroupExist(self, group):
        """
        Returns True if the given group does exist and has at least one entity
        in it, false otherwise.
        @group: name of the group (str)
        """
        assert isinstance(group, str)
        if group not in self.entitiesByGroup.keys():
            return False
        if len(self.entitiesByGroup[group]) == 0:
            return False
        return True

    ##### PYTHONIC METHODS FOR EASIER PROGRAMMING
    def __str__(self):
        """Returns a string representation of the class, useful when debugging."""
        return pprint.pformat(self.entitiesByGroup, indent = 1)

    def __getitem__(self, group):
        """
        Defines the usage of:
            x = y[group]
        which gets all the entities for that group.
        """        
        return self.get(group)

    def __setitem__(self, group, entity):
        """
        Defines the usage of:
            y[group] = entity
        which adds the entity to the group.
        """
        self.add(entity, group)

    def __delitem__(self, entity):
        """
        Defines the usage of:
            del y[entity]
        which removes the entity from all groups."""
        self.removeCompletely(entity)

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent = 1)
    ent1 = larv.Entity(1)
    ent2 = larv.Entity(2)
    ent3 = larv.Entity(3)
    gm = GroupManager(larv.Engine(larv.EntityFactory()))

    gm.add(ent1, 'monsters')
    gm.add(ent2, 'monsters')
    gm.add(ent3, 'monsters')    
    # pp.pprint(gm.entitiesByGroup)

    gm.add(ent2, 'hero')
    gm.add(ent3, 'hero')
    # pp.pprint(gm.entitiesByGroup)

    gm.remove(ent2, 'monsters')
    # pp.pprint(gm.entitiesByGroup)
    gm.add(ent2, 'monsters')

    gm.removeCompletely(ent2)
    # pp.pprint(gm.entitiesByGroup)
    gm.add(ent2, 'monsters')
    gm.add(ent2, 'hero')
    gm.add(ent2, 'hero')
    gm.add(ent2, 'hero')
    # pp.pprint(gm.entitiesByGroup)

    # gm.add(larv.Entity(4), 'test')
    # pp.pprint(gm.entitiesByGroup)
    # alist = []
    # for e in gm.get('hero'):
    #     alist.append(e.id)
    # print('Hero:', str(alist))
    # alist = []
    # for e in gm.get('hero', 'monsters', 'test'):
    #     alist.append(e.id)
    # print('Hero + Monster + Test:', str(alist))    
    # gm.add(ent2, 'test')
    # alist = []
    # for e in gm.get('hero', 'monsters', 'test'):
    #     alist.append(e.id)
    # print('Hero + Monster + Test:', str(alist))

    # print(gm.getGroup(ent2))

    # print(gm.isInGroup(ent2, 'monsters'), gm.isInGroup(larv.Entity(999),'monsters'))

    # print(gm['monsters'])







