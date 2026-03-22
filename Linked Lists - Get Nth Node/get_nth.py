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

    cur = node
    for _ in range(index):
        nxt = cur.next

        cur = nxt

    if nxt:
        cur = nxt

    return cur
