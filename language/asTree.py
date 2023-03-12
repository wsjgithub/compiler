class Node:
    def __init__(self, value, type = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.type = type

    def print(self, indent, write = False):
        output = '\t'*indent + self.value+': '+self.type
        if write:
            return output + '\n'
        else:
            print(output)

    
    def preorder(self, indent = 0):
        self.print(indent)
        self.left and self.left.preorder(indent + 1)
        self. right and self.right.preorder(indent + 1)

    def preorderOutput(self, indent = 0):
        output = self.print(indent, True)
        if self.left:
            output += self.left.preorderOutput(indent + 1)
        if self.right:
            output += self.right.preorderOutput(indent + 1)
        return output
    
    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
        
class Test:
    def __init__(self, root):
        self.root = root
    
    def preorder(self):
        self.preorderR(self.root)

    def preorderR(self, node):
        if not node: return
        node.print()
        self.preorderR(node.left)
        self.preorderR(node.right)