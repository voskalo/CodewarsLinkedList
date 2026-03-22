'''Parse a linked list from a string'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    '''test funct'''

    if list_repr is None:
        return None

    parts = list_repr.split(' -> ')
    first = None
    cur = None

    for el in parts[:-1]:
        node = Node(int(el))
        if not first:
            first = node
            cur = node

        else:
            cur.next = node
            cur = node

    return first
