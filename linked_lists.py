import os

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def print_node(self):
        print(f'''{self.val} {self.next}''')
        
class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def remove_from_front(self):
        self.head = self.head.next

    def last_node(self):
        temp_node = self.head
        while(temp_node.next != None):
            temp_node = temp_node.next
        return temp_node

    def is_empty(self):
        if(self.head == None):
            return True
        else:
            return False

    def add_to_end(self, val):
        if(self.is_empty()):
            self.add_to_front(val)
        else:
            new_node = Node(val)
            self.last_node().next = new_node

    def remove_from_end(self):
        if(self.head == None):
            return
        elif(self.head.next == None):
            self.head = None
        else:
            temp_node = self.head
            while(temp_node.next.next != None):
                temp_node = temp_node.next
            temp_node.next = None

    def find_parent(self, child_node):
        '''an abandoned idea'''
        if(self.head == child_node):
            return False
        else:
            temp_node = self.head
            while(temp_node.next != None):
                if(temp_node.next == child_node):
                    return temp_node
                temp_node = temp_node.next
            return False

    def remove_val(self, val):
        if(self.head == None):
            return self
        elif(self.head.val == val):
            self.head = self.head.next
        elif(self.head.next.val == val):
            self.head.next = self.head.next.next
            return self
        else:
            temp_node = self.head
            while(temp_node.next != None):
                if(temp_node.next.val == val):
                    temp_node.next = temp_node.next.next
                    return self
                temp_node = temp_node.next
        return self

    def insert_at(self, val, n):
        if(int(n) == 0):
            self.add_to_front(val)
        else:
            temp_node = self.head
            for i in range(0, int(n)-1):
                temp_node = temp_node.next
            new_node = Node(val)
            new_node.next = temp_node.next
            temp_node.next = new_node

    def print_all(self):
        temp_node = self.head
        while(temp_node != None):
            temp_node.print_node()
            temp_node = temp_node.next

#main start
my_list = SList()

choice = ""
while (choice != "7"):
    os.system('cls')
    print("***List***")
    my_list.print_all()
    print("***End****")
    print('''
    1 - Add to front
    2 - Remove from front
    3 - Add to End
    4 - Remove from End
    5 - Remove by Value
    6 - Insert At
    7 - Quit
    ''')
    choice = input("Enter choice: ")
    if(choice=="1"):
        value = input("Enter Value: ")
        my_list.add_to_front(value)
    elif(choice=="2"):
        my_list.remove_from_front()
    elif(choice=="3"):
        value = input("Enter Value: ")
        my_list.add_to_end(value)
    elif(choice=="4"):
        my_list.remove_from_end()
    elif(choice == "5"):
        value = input("Enter Value: ")
        my_list.remove_val(value)
    elif(choice== "6"):
        value = input("Enter Value: ")
        index = input("Enter Index: ")
        my_list.insert_at(value, index)
    elif(choice == "7"):
        break

# print("\n#######################")
# my_list.remove_from_end()
# my_list.print_all()

# my_list.add_to_end("X")
# print("\n#######################")
# my_list.remove_from_end()
# my_list.print_all()

# my_list.add_to_end("X")
# my_list.add_to_end("Y")
# print("\n#######################")
# my_list.remove_from_end()
# my_list.print_all()

# print("\n#######################")
# my_list.add_to_end("T")
# my_list.print_all()

# print("\n#######################")
# my_list.add_to_front("A")
# my_list.print_all()

# print("\n########################")
# my_list.add_to_front("B")
# my_list.print_all()

# print("\n########################")
# my_list.add_to_front("C")
# my_list.print_all()

# print("\n########################")
# my_list.add_to_end("D")
# my_list.print_all()

# print("\n########################")
# my_list.remove_from_front()
# my_list.print_all()

# print("\n########################")
# my_list.remove_from_end()
# my_list.print_all()

