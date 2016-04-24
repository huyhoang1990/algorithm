

class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, value):
        self.next_node = value


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if data == current.get_data():
                found = True
            else:
                current = current.get_next()

        if not found:
            raise ValueError("Item is not in list")

        return current

    def delete(self, data):
        current = self.head
        next_node = current.get_next()
        back_node = None
        delete = False

        while current and delete is False:
            if current.get_data() == data:
                delete = True
                if back_node is None:
                    self.head = current.get_next()
                else:
                    back_node.set_next(next_node)
                    self.head = back_node
            else:
                back_node = current
                current = current.get_next()
                if current:
                    next_node = current.get_next()

        if delete is False:
            raise ValueError("Data is not in list")


if __name__ == '__main__':
    a = LinkedList()
    a.insert("hoang")
    a.insert("hihi")
    a.insert("hihi")
    a.insert("hoho")
    print a.size()
    a.delete("hihi")
    a.delete("hihi")
    print a.size()
    a.delete("hoang")
    print a.size()
    a.delete("hoho")
    print a.size()