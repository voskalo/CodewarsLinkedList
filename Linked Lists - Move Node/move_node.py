'''Linked Lists - Move Node'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: 'Node', dest):
    '''funct'''

    if not source:
        raise ValueError('List is empty')

    node_to_move = source
    new_source = source.next
    node_to_move.next = dest


    return Context(new_source, node_to_move)
