class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head: 'Node'):
    '''smth'''

    if not head or not head.next:
        raise ValueError('None or 1 el node')

    first = head
    second = head.next

    first_node = first
    second_node = second

    cur = head.next.next

    queue = True

    while cur:
        if queue:
            first_node.next = cur
            first_node = first_node.next
        else:
            second_node.next = cur
            second_node = second_node.next

        queue = not queue
        cur = cur.next

    first_node.next = None
    second_node.next = None

    return Context(first, second)
