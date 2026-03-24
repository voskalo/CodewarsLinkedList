'''Can you get the loop ?'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def loop_size(node: 'Node'):
    '''smth'''

    if not node or not node.next:
        return node

    visited = {}
    cur = node
    idx = 0

    while cur:
        if cur in visited.keys():
            return idx - visited[cur]

        visited[cur] = idx
        cur = cur.next
        idx += 1

    return 0
