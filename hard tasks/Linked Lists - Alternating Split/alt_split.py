'''Linked Lists - Alternating Split'''

class Node(object):
    '''smth'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''smth'''
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head: 'Node'):
    '''smth'''

    if not head or not head.next:
        return head

    first = Node()
    second = Node()

    cur = head
    nxt = head.next

    while head.next:
        if cur:
            first.next = cur
        if nxt:
            second.next = nxt

        if not nxt or not cur:
            return Context(first.next, second.next)

        cur = first
        nxt = second
        first = second.next
        second = second.next.next
