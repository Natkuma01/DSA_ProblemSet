class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    # Create maX_val = head.value
    # set up a current that store the value when run over the linkedlist
    # while loop to check whether the current is max or
    max_val = head.value
    curr = head
    while curr:
        if curr.value > max_val:
            max_val = curr.value
        curr = curr.next
    return max_val


# time complxity - O(n)
# space complxity - O(1)
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))



class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("None")
        return None
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    if not head:
        return None
    if not head.next:
        return head 
        
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    curr = head
    while curr:
        if curr.next and curr.value == curr.next.value:
            dups = curr.value
            while curr and curr.value == dups:
                curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return dummy.next
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
head1 = Node(1)
head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(5))))))
# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
print_linked_list(delete_dupes(head1))
print_linked_list(delete_dupes(head2))

# 1.     2.     3.     3.     4.     5
#              cur
#                     cur.n
#       prev

# 2 -> 2 -> 2 -> 2 -> 2 -> 2
# 1 -> 1 -> 2 -> 3 -> 3 -> 4