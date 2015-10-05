# Definition for singly-linked list.
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

'''
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def get_data(self):
        return self.data
    @property
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                current = current.get_next
        if current is None:
            print "Data not in list"
            return False
            
        return "Node: {} found in linked list.".format(current.get_data)

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        tmp_prev = None
        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                tmp_prev = current
                current = current.get_next

        if current is None:
            print "Data not found in list. Cannot delete!"
            return
        else:
            if tmp_prev == None:
                self.head = self.head.get_next
            else:
                tmp_next = current.get_next
                current = tmp_prev
                current.set_next(tmp_next)
                self.print_list

    @property
    def print_list(self):
        tmp_lst = []
        current = self.head
        if not current:
            print "Linked List does not contain any nodes! Quit!"
            return 

        while current:
            tmp_lst.append(str(current.get_data))
            current = current.get_next
        tmp_lst.append('None')

        string = "->".join(tmp_lst)
        print "Linked List conatins: {}".format(string)

    def partition(self, x):
        current = self.head
        smaller_lst = []
        larger_lst = []
        while current:
            if current.get_data < 3:
                smaller_lst.append(current.get_data)
            if current.get_data >= 3:
                larger_lst.append(current.get_data)
            current = current.get_next
        #re-creating the linked list
        smaller_lst.reverse()
        larger_lst.reverse()
        self.head = None
        for each in larger_lst:
            self.insert(each)
        for each in smaller_lst:
            self.insert(each)

            
            
            

'''
ll = LinkedList()
for i in xrange(10):
    print "inserting {}".format(i)
    ll.insert(i)
print ll.search(9)
print ll.search(11)
ll.print_list
print "adding 11"
ll.insert(11)
ll.print_list
print "deleting 5"
ll.delete(5)
ll.print_list
print "deleting 11"
ll.delete(11)
ll.print_list
'''
ll = LinkedList()
lst = [1,5,2,2,3,0,3,10]
lst.reverse()
for i in lst:
    ll.insert(i)
ll.print_list
print "Partition at 3"
ll.partition(3)
ll.print_list

