'''Can you get the loop ?'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def loop_size(node: 'Node'):
    '''smth'''

    if not node or not node.next:
        return 0


    slow = node
    fast = node

    # перевірили шо цикл є
    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    else:
        return 0

    meet = slow.next
    res = 1

    while meet != slow:
        res += 1
        meet = meet.next

    return res
