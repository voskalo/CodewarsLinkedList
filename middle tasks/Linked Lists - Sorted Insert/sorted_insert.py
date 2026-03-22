'''Linked Lists - Sorted Insert'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head: 'Node', data):
    '''funct'''

    new_node = Node(data)

    if not head:
        return new_node

    if data < head.data:
        new_node.next = head
        return new_node

    return head
