class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    #searching elements in the List
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,3,4,2]
    numbers_tree = build_tree(numbers)
    
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    
    # Inserting a new element
    numbers_tree.add_child(7)
    print("In order traversal after inserting 7:", numbers_tree.in_order_traversal())

    numbers_tree.add_child(0)
    print("In order traversal after inserting 0:", numbers_tree.in_order_traversal())
    
    #search for element 15 and 3 
    search_for = 15
    print(search_for," is in the list? ", numbers_tree.search(search_for))
    search_for = 3
    print(search_for," is in the list? ", numbers_tree.search(search_for))
    
    
    # for finding minimum element in the list 
    print("Minimum value in the tree:", numbers_tree.find_min())
    # for finding maximum element in the list 
    print("Maximum value in the tree:", numbers_tree.find_max())

    # Deleting elements
    numbers_tree.delete(3)
    print("In order traversal after deleting 3:", numbers_tree.in_order_traversal())

    numbers_tree.delete(5)
    print("In order traversal after deleting 5:", numbers_tree.in_order_traversal())

    numbers_tree.delete(1)
    print("In order traversal after deleting 1:", numbers_tree.in_order_traversal())