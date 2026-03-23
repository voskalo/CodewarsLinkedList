'''Swap Node Pairs In Linked List'''

class Node:
    '''smth'''
    def __init__(self, next=None):
        '''init'''
        self.next = next

def swap_pairs(head: 'Node'):
    '''funct'''

    if not head or not head.next:
        return head

    node = Node()
    node.next = head
    prev = node

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return node.next
