#use bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque([])
        if root:
            q.append(root)
        levels = []
        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    
                    l.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                
                    if node.right:
                        q.append(node.right)
            levels.append(l)
            
        
        return levels
            
