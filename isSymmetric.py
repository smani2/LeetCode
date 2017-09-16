# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Solution(object):
    def isSymmetric(self, root):
        queue = Queue()
        queue.enqueue(root)
        queue.enqueue(root)
        while(queue.isEmpty() == False):
            node1 = queue.dequeue()
            node2 = queue.dequeue()
            if (node1 == None):
                if node2 != None: 
                    return False
            elif (node2 == None):
                if node1 != None:
                    return False
            elif (node1.val != node2.val): return False
            else:
                queue.enqueue(node1.right)
                queue.enqueue(node2.left)
                queue.enqueue(node1.left)
                queue.enqueue(node2.right)
        return True


        """
        :type root: TreeNode
        :rtype: bool
        """
        
