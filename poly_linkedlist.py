

class Node():

    def __init__(self,const,pow1):
        self.const = const
        self.pow = pow1
        self.nxt = None

class LinkedList():

    def __init__(self,head):
        self.head = None

    def append(self,const,pow1):

        new_node = Node(const,pow1)
        if self.head is None:
            self.head = new_node
        else:
            while temp.nxt is not None:
                temp = temp.nxt
            temp.nxt = new_node

    def printList(self):

        temp = self.head
        while temp is not None:
            print(temp.data,'x',end='')
            temp = temp.nxt
            if temp.nxt is not None:
                print('+',end='')