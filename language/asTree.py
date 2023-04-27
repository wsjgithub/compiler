import copy
class Node:
    def __init__(self, value, type = None, left = None, middle = None, right = None):
        self.value = value
        self.left = left
        self.middle = middle
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
        self.middle and self.middle.preorder(indent + 1)
        self. right and self.right.preorder(indent + 1)
    
    def preorderStack(self, stack):
        stack.append(self)
        self.left and self.left.preorderStack(stack)
        self.middle and self.middle.preorderStack(stack)
        self. right and self.right.preorderStack(stack)
        
    def preorderOutput(self, indent = 0):
        output = self.print(indent, True)
        if self.left:
            output += self.left.preorderOutput(indent + 1)
        if self.middle:
            output += self.middle.preorderOutput(indent + 1)
        if self.right:
            output += self.right.preorderOutput(indent + 1)
        return output
    
    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
    
    def __str__(self):
        return str(self.value)

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