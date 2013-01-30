# encoding: UTF-8

class PriorityList:
    """
    Implements a list of ordered nodes.
    Every node will be a 2 item tuple:
        - First item will be the content we want to store
        - Second item will be the content used for ordering the list.
          This item needs to have the __lt__ method.
    Optimized thinking that users will introduce higher priority items first.

    Note: Ordered from lower value to higher, that's thought out
          for easy usage using numbers, where 0 will be max priority (assuming
          no use of negative numbers) and every other number will have less and
          less priority as they get higher.
    """
    def __init__(self):
        self.list = []

    def add(self, item, order_value):
        """
        Adds the given item in the list.
        @item: stored content.
        @order_value: used for knowing in which position the content will be stored.
        """
        for i in range(len(self.list), 0, -1):
            if self.list[i-1][1] < order_value:
                self.list.insert(i, (item, order_value))
                return
        else:
            self.list.insert(0, (item, order_value))

    def remove(self, item):
        """Removes the given item from the priority list."""
        self.list.remove(item)

    def __iter__(self):
        """Iterates over the content values of the list."""
        for item in self.list:
            yield item[0]

    def __str__(self):
        return 'PriorityList: {0}'.format(str(self.list))


if __name__ == '__main__':
    ## TESTING
    import random
    some_values = []
    for i in range(0,300,3):
        some_values.append(('test',i))

    random.shuffle(some_values)
    # print(some_values)
    p_list = PriorityList()
    for item in some_values:
        p_list.add(item[0],item[1])

    # print(p_list)
    
    # for item in p_list:
    #     print(item)