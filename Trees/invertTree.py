class Solution:
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        

        que = collections.deque([(root)])
        
        while que:
            node = que.popleft()
            if node:
                node.left, node.right = node.right,node.left

                que.append(node.left)
                que.append(node.right)
        
        return root
