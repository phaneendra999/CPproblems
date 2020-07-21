"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 1
        
    def append(self, new_element):
        # Your code goes here
        if(self.head != None):
            current_element = self.head
            while (current_element.next != None):
                current_element = current_element.next
            current_element.next = new_element
        else:
            self.head = new_element
        self.count += 1
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here]
        if(position <= self.count):
            temp = 1
            current_element = self.head
            while temp < position:
                temp += 1
                current_element = current_element.next
            return current_element
        return None

    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        current_element = self.head
        if(position <= self.count):
            temp =1
            while True:
                if(temp == position -1):
                    new_element.next = current_element.next
                    current_element.next = new_element
                    self.count += 1
                    return
                current_element = current_element.next
                temp += 1
        while True:
            if(current_element.next == None):
                current_element.next = new_element.next
                self.count += 1
                return
            current_element = current_element.next
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        current_element = self.head
        if(current_element != None):
            if(current_element.value == value):
                if(current_element.next == None):
                    self.head = None
                else:
                    self.head = current_element.next
                self.count -= 1
                return current_element
            while(current_element.next != None):
                if(current_element.next.value == value):
                    if(current_element.next.next == None):
                         current_element.next = None
                    else:
                        current_element.next = current_element.next.next
                    self.count -= 1
                    return
                current_element = current_element.next
        return None