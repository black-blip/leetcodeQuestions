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
###DFS
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        

        st = [root]
        
        while st:
            node = st.pop()
            if node:
                node.left, node.right = node.right,node.left
                st.extend([node.right,node.left])
       
        return root

##Recursive
    def invertTree(self,root: Optional[TreeNode])->Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
