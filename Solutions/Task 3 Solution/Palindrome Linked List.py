class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

if is_palindrome(head):
    print("The linked list is a palindrome.")  
    
else:
    print("The linked list is not a palindrome.")