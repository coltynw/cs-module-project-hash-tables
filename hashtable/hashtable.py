
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

# unnecessisary linked list. 
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def __str__(self):
#         r = ""
#         cur = self.head
        
#         while cur is not None:
#             r += f'({cur.value})'
#             if cur.next is not None:
#                 r += ' -> '
#             cur = cur.next
#         return r
        
#     def insert_at_head(self, node):
#         node.next = self.head
#         self.head = node
        
#     def find(self, value):
#         cur = self.head
#         while cur is not None:
#             if cur.value == value:
#                 return cur
#             cur = cur.next
#         return None
            
#     def delete(self, value):
#         cur = self.head
#         if cur.value == value:
#             self.head = self.head.next
#             return cur
#         prev = cur
#         cur = cur.next         
#         while cur is not None:
#             if cur.value == value:  
#                 prev.next = cur.next   
#                 return cur
#             else:
#                 prev = prev.next
#                 cur = cur.next
#         return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.count = 0
        self.data = [None] * capacity
        # same as data with 8 none's in it


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity 
        # divide the count by the capacity to get the load factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # increment size
        self.count += 1 
        # get the index
        index = self.djb2(key) #run the hash method on the key
        # go to the node corresponding with the hash, aka the index variable 
        print(index)
        index = index % self.capacity
        freshnode = self.data[index]
        # if the bucket is empty
        if freshnode is None:
            #create node, add it, return
            self.data[index] = Node(key, value)
            return
        # Iterate to the end of the LL at the provided index
        else: 
            newNode = Node(key, value)
            newNode.next = freshnode
            self.data[index] = newNode
        # Add a new node at the end of the list provided key/value




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None) # set node to None
        self.count -= 1  # decrement the count 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # compute hash
        index = self.djb2(key)
        # go to the first node in list 
        index = index % self.capacity
        node = self.data[index]
        # traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # now, node is the requested key/value pair or None
        if node is None:
            #we didn't find it
            return None
        else:
            # found it, return data
            return node.value



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        data = self.data

        self.capacity = new_capacity
        self.data = [None] * self.capacity
        self.count = 0

        for d in data:
            if d != None:
                while d.next != None:
                    next = d.next
                    self.put(d.key, d.value)
                    d = next
                self.put(d.key, d.value)





        





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
