class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        if index < 0 or index > self.length():
            return
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def delete_value(self, data):
        self.delete_node(data)

    def delete_index(self, index):
        if self.head is None or index < 0 or index >= self.length():
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(index - 1):
            temp = temp.next
        target = temp.next
        if target:
            temp.next = target.next
            target = None

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def menu():
    sll = Linkedlist()
    while True:
        print("\n1. Append\n2. Insert at Start\n3. Insert at Index\n4. Delete Value\n5. Delete Index\n6. Display\n7. Exit")
        choice = int(input("Choice: "))
        
        match choice:
            case 1:
                val = int(input("Value: "))
                sll.append(val)
            case 2:
                val = int(input("Value: "))
                sll.insert_at_start(val)
            case 3:
                idx = int(input("Index: "))
                val = int(input("Value: "))
                sll.insert(idx, val)
            case 4:
                val = int(input("Value to delete: "))
                sll.delete_value(val)
            case 5:
                idx = int(input("Index to delete: "))
                sll.delete_index(idx)
            case 6:
                sll.display()
            case 7:
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    menu()