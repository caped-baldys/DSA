class Node():

    def __init__(self,data = None):
        self.data = data
        self.nxt = None


class Slinked():
    def __init__(self):
        self.head = None

    def printList(self):

        temp = list_link.head
        while temp is not None:
            print(temp.data,end='->')
            temp = temp.nxt

    def append(self,data):
        temp = list_link.head

        while temp.nxt is not None:
            temp = temp.nxt
        temp.nxt = Node(data)

    def AtBegining(self,newdata):

        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self,pos,newdata):
        NewNode = Node(newdata)
        temp = self.head
        while(temp.data != pos):
            temp = temp.nxt

        NewNode.nxt = temp.nxt
        temp.nxt = NewNode
#driver code

list_link = Slinked()

list_link.AtBegining(11)
list_link.append(10)
list_link.append(90)
list_link.printList()

print('Complete')
list_link.Inbetween(10, 30)
list_link.printList()