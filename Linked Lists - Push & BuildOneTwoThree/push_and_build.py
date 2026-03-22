'''Linked Lists - Push & BuildOneTwoThree'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    '''push'''

    if head is None:
        head = Node(data)
        return head

    cur = head
    head = Node(data)
    head.next = cur
    return head




def build_one_two_three():
    '''funct'''

    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
