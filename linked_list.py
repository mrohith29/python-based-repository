class sll:
    def __init__(self):
        self.data = None
        self.next = None


head = None
count = 0


def insert(pos):
    global head, count
    newnode = sll()
    temp = head
    ptr = None

    if pos < 1 or pos > count+1:
        print('position doesnot exist - cannot insert newnode')
        return

    newnode.data = int(input())
    if pos == 1:
        newnode.next = head
        head = newnode
    else:
        for i in range(1, pos):
            ptr = temp
            temp = temp.next
        newnode.next = temp
        ptr.next = newnode
    count += 1

def delete(pos):
    global head, count
    temp = head
    ptr = None

    if count < pos or pos < 1:
        print(pos,'does not exist - please enter a valid position to delete')
        return
    if pos == 1:
        print('Deleted element from sll is',head.data)
        head = head.next
    else:
        for i in range(1,pos):
            ptr = temp
            temp = temp.next
        print('Deleted element from sll is',temp.data)
        ptr.next = temp.next
    count -= 1

if __name__ == '__main__':
    while True:
        choice = int(input())
        if choice == 1:
            position = int(input())
            insert(position)
        elif choice == 2:
            position = int(input())
            delete(position)