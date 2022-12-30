
class Node():

    def __init__(self,data=None):
        self.data = data
        self.nxt = None

class CircularLinkedList():

    def __init__ (self):
        self.head = None

    def add_Data(self,data):
        temp = self.head
        new_node = Node(data)
        new_node.nxt = self.head

        if self.head is not None :

                while temp.nxt != self.head:
                    temp = temp.nxt
                temp.nxt = new_node
        else:
            new_node.nxt = new_node
            self.head = new_node
            
            
            

    def print_cl(self):
        temp = self.head
        if self.head is not None:
            while temp.nxt != self.head:
                print(temp.data)
                temp = temp.nxt
        else:
            print("Empty")
    
my_list = CircularLinkedList()
my_list.add_Data(103)
my_list.add_Data(102)
my_list.add_Data(101)
my_list.add_Data(100)
my_list.print_cl()