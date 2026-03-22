'''Linked Lists - Get Nth Node'''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node: 'Node', index):
    '''smth'''

    if not node:
        raise ValueError

    if index < 0:
        raise ValueError("Index out of bounds")



    cur = node
    nxt = None


    try:
        for _ in range(index):
            nxt = cur.next

            cur = nxt

        if nxt:
            cur = nxt

    except AttributeError:
        raise ValueError("Index out of bounds")

    if cur is None:
        raise ValueError("Index out of bounds")

    return cur


# n = Node(1, Node(2, Node(3, None)))

# print(get_nth(n, 5))
