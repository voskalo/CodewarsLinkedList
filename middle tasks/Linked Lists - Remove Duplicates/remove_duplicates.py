'''remove duplicates'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head: 'Node'):
    '''function'''

    if head is None or head.next is None:
        return head

    current = head

    while current is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        current = current.next

    return head
