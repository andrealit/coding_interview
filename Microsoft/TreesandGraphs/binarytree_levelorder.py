# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        # go until end
        queue = deque([root,])
        while queue:
            #start the current level
            levels.append([])
            #number of elements in current level
            level_len = len(queue)
            
            
            for i in range(level_len):
                node = queue.popleft()
                # fill the current lvl
                levels[level].append(node.val)
                
                # add child nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                
            level += 1
            
        return levels