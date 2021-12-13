import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        
        # condition for empty
        if root is None:
            return ans
        
        # use a queue
        queue = collections.deque()
        queue.append(root)
        
        # iterate the entire queue
        while queue:
            currSize = len(queue)
            currList = []
            
            while currSize > 0:
                # dequeue element
                currNode = queue.popleft()
                currList.append(currNode.val)
                currSize -= 1
                
                # check the left
                if currNode.left is not None:
                    queue.append(currNode.left)
                
                # check the right
                if currNode.right is not None:
                    queue.append(currNode.right)
                
            ans.append(currList)
            
        return ans