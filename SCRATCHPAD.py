# Come back here, I couldn't do this.
# https://leetcode.com/problems/merge-two-sorted-lists/


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.val = None
        self.numOfNodes = 0
        # self.next = next

    def insert_start(self, val):
        new_node = Node(val)
        self.numOfNodes = self.numOfNodes + 1

        if not self.val:
            self.val = new_node
        else:
            new_node.next = self.val
            self.val = new_node


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_start(4)
    l1.insert_start(2)
    l1.insert_start(1)

    print(l1.val.val)
    print(l1.val.next)
    print(l1.numOfNodes)

