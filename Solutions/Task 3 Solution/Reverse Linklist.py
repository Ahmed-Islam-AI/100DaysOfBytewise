class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next   # Store the next node
        current.next = prev        # Reverse the current node's pointer
        prev = current             # Move pointers one position ahead
        current = next_node
    return prev

# Example usage
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original linked list:")
    print_linked_list(head)

    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)









