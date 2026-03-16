class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_Awal(self, data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru

    def Insert_Akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node_baru

    def Tampilkan(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
            print("None")


if __name__ == '__main__':
    LL = LinkedList()
    LL.Insert_Awal(10)
    LL.Insert_Awal(20)
    LL.Insert_Awal(30)
    LL.Tampilkan()