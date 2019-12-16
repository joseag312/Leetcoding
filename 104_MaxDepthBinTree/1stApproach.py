class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        if root.left != None:
            l = self.maxDepth(root.left)
        else:
            l = 0
        if root.right != None:
            r = self.maxDepth(root.right)
        else:
            r = 0
            
        
        return max(l+1,r+1,1)