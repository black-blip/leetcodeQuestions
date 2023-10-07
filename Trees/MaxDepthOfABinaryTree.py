# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#use iterative DFS in this problem with stack and keep a record of the depth of each node 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        st = [(root,1),]
        res = 0
        while st:
            node,depth = st.pop()
            if node:
                res = max(res,depth)
                st.append((node.left,depth+1))
                st.append((node.right,depth+1))
        return res
