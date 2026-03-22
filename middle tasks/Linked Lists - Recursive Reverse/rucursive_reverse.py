'''Linked Lists - Recursive Reverse'''

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head: 'Node'):
    '''smth'''

    if not head:
        return head

    if not head.next:
        return head

    new = reverse(head.next)
    head.next = head

    return new
