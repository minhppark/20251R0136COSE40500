class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        print(f"Appending {data} to list.")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        print("Linked List content:")
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def search(self, key):
        print(f"Searching for {key} in list.")
        current = self.head
        while current:
            if current.data == key:
                print(f"Found {key} in list.")
                return True
            current = current.next
        print(f"{key} not found in list.")
        return False

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    ll.print_list()
    ll.search(3)
    ll.search(6)