'''
Below code is based on this repo: https://github.com/joeyajames/Python/tree/master/LinkedLists
See also:
CircularLinkedList.py
DoublyLinkedList1.py
DoublyLinkedList2.py
'''

class Node(object):
    
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n
        
    def get_data(self):
        return self.data
    
    def set_data(self, d):
        self.data = d
        
    def to_string(self):
        return "Node value: " + str(self.data)
    
    def has_next(self):
        if self.get_next() is None:
            return False
        return True
    
    def compare_to(self, y):
        if self.to_string() < y.to_string():
            return -1
        elif self.to_string() > y.to_string():
            return 1
        return 0

class LinkedList(object):
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
    def add_node(self, n):
        n.set_next(self.root)
        self.root = n
        self.size += 1
        
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node:
            if this_node.get_data() == d:
                if prev_node: # removing node that is not the root
                    prev_node.set_next(this_node.get_next())
                else: # removing root node
                    self.root = this_node.get_next()
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # data not found
    
    '''Alternative find'''
    # def find(self, d):
    #     this_node = self.root
    #     while this_node:
    #         if this_node.get_data() == d:
    #             return d
    #         else:
    #             this_node = this_node.get_next()
    #     return None

    '''Alternative find'''
    def find (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()
    
    def print_list(self):
        print('Print List...')
        if self.root is None:
            return
        current = self.root
        print(current.to_string())
        while current.has_next():
            current = current.get_next()
            print(current.to_string())
            
    def sort(self):
        if self.size > 1:
            newlist = []
            current = self.root
            newlist.append(self.root)
            while current.has_next():
                current = current.get_next()
                newlist.append(current)
            newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True)
            newll = LinkedList()
            for node in newlist:
                newll.add_node(node)
            return newll
        return self


# Experementing...

myList = LinkedList()
myList.add(5)
myList.add(9)
myList.add(3)
myList.add(8)
myList.add_node(Node(11))
myList.add(9)
print("size="+str(myList.get_size()))
myList.print_list()
myList = myList.sort()
myList.print_list()
myList.remove(8)
print("size="+str(myList.get_size()))
print("Remove 15", myList.remove(15))
print("size="+str(myList.get_size()))
print("Find 25", myList.find(25))
myList.print_list()




'''
Below code is old one
'''
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)

    def is_empty(self):
        return self.head == None

    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
        
    # function to delete any node
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


    # function to get the last node
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # function to print the list nodes
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next


# Experementing with old code...
# s = linked_list()
# s.add_at_front(5)
# s.add_at_end(8)
# s.add_at_front(9)
# s.delete_node(5)

# s.print_list()