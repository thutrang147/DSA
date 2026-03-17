class LinkedList:
    def __init__(self): # Initialize an empty list
        self.head = None
        self.size = 0
    
    def __len__(self): # Return the number of elements
        return self.size
    
    def is_empty(self): # Check if the list is empty
        return self.__len__ == 0
    
    def __getitem__(self, k): # Access data at position k
        if k < 0 or k >= self.size:
            raise IndexError("Index out of range")
            
        curr = self.head
        for _ in range(k):
            curr = curr.next_node
            
        return curr.value
    
    def insert(self, k, data): # Insert a new node with data at position k
        if k < 0 or k > self.size:
            raise IndexError("Index out of range")
        
        new_node = Node(data)
        if k == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(k - 1):
                if curr is None:
                    raise IndexError("Index out of range")
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node
        
        self.size += 1

    def __delitem__(self, k): # Delete item at posion k
        if k < 0 or k >= self.size:
            raise IndexError("Index out of range")
        
        if k == 0:
            self.head = self.head.next_node
        else:
            curr = self.head
            for _ in range(k - 1):
                curr = curr.next_node
            curr.next_node = curr.next_node.next_node

        self.size -= 1
    
    # Delete all nodes with value val. Return deleted values.
    def delete_by_value(self, val): 
        pos = self.search(val)
        if pos == -1:
            print("Not found")
            return []
        
        for pos in sorted(pos, reverse=True):
            self.__delitem__(pos)


    # Find nodes with value `val`. Return position(s). 
    # Return `-1` and print("Not found") if `val` is not in list.
    def search(self, val):
        curr = self.head
        index = 0
        pos = []
        while curr:
            if curr.value == val:
                pos.append(index)
            curr = curr.next_node
            index += 1
        
        if not pos:
            print("Not found")
            return -1
        return pos

    def update(self, k, new_val): # Update data at posion k
        if k < 0 or k > self.size:
            raise IndexError("Index out of range")
        
        curr = self.head
        for _ in range(k):
            curr = curr.next_node
        
        curr.value = new_val
    
    def add_end(self, data):
        new_node = Node(data, None)
        
        if self.head is None:
            self.head = new_node
            return 
        
        curr = self.head
        while curr.next_node:
            curr = curr.next_node
        
        curr.next_node = new_node
                
    def __str__(self): # Return a string representation of the list.
        start = self.head
        elements = []
        while (start):
            elements.append(start.value)
            start = start.next_node

        elements.append(None)
        return ' -> '.join(map(str, elements))