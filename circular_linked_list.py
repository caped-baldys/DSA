
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


    def del_data(self,data):
        temp = self.head
        if temp is not None:
            prev = None
            while temp.data != data:
                prev = temp
                temp = temp.nxt
            prev.nxt = temp.nxt

    def insert_data(self,index,data):
        temp = self.head
        new_node = Node(data)
        if temp is not None:
            prev = None
            while index>=0 :
                index -= 1
                prev = temp
                temp = temp.nxt
            prev.nxt = new_node
            new_node.nxt = temp

    def print_cl(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print("%d" %(temp.data)),
                temp = temp.nxt
                if (temp == self.head):
                    break
        else:
            print("Empty")
    
my_list = CircularLinkedList()
my_list.add_Data(103)
my_list.add_Data(102)
my_list.add_Data(101)
my_list.add_Data(100)

print('Insertion')
my_list.insert_data(2, data=111)
my_list.print_cl()

print('\n Deletion')
my_list.del_data(100)
my_list.print_cl()