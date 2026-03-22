'''remove duplicates'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''function'''

    if head is None or head.next is None:
        return head

    return head
