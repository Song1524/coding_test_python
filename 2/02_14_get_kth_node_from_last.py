class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        # 먼저 리스트의 길이를 구하고 리스트길이 - k 로 구하고 싶은 인덱스를 찾으면 될거같은데
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        cur = self.head

        for i in range(count - k):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!