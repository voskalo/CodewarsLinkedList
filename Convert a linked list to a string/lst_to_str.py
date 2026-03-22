'''Convert a linked list to a string'''

class Node():
    def __init__(self, data, next = None):
        '''init'''
        self.data = data
        self.next = next


def stringify(node: 'Node'):
    '''task func'''

    if node:
        return f'{node.data} -> {stringify(node.next)}'

    return 'None'
