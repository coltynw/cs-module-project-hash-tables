
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
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return 'hi'
        
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        r = ""
        cur = self.head
        
        while cur is not None:
            r += f'({cur.value})'
            if cur.next is not None:
                r += ' -> '
            cur = cur.next
        return r
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
            
    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None
            
    def delete(self, value):
        cur = self.head
        if cur.value == value:
            self.head = self.head.next
            return cur
        prev = cur
        cur = cur.next         
        while cur is not None:
            if cur.value == value:  
                prev.next = cur.next   
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None


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
        self.data = [LinkedList()] * capacity
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
        # slot = self.hash_index(key)
        # current = self.storage[slot].head
        # while current:
        #     if current.key == key:
        #         current.value = value
        #     current = current.next
            
        # entry = HashTableEntry(key, value)
        # self.storage[slot].insert_at_head(entry)
        # self.count += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        slot = self.hash_index(key)
        self.data[slot].insert_at_head(HashTableEntry(key, value))
        self.count += self.count # iterate the count 


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None)
        self.count -= 1  # decrement the count 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # current = self.storage[slot].head
        # while current:
        #     if current.key == key:
        #         return current.value
        #     current = current.next
        # return None
        slot = self.hash_index(key)
        entry = self.data[slot]
        if entry:
            return entry.find(key)

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_data = [LinkedList()] * new_capacity
        self.capacity = new_capacity
        for i in range(len(self.data)):
            cur = self.data[i].head
            while cur:
                self.hash_index(cur.key)
                new_data[i].insert_at_head(HashTableEntry(cur.key, cur.value))
                cur = cur.next
        self.data = new_data
                
        # self.capacity = new_capacity




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
