from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root):
            if root:
                temp = root.left
                root.left = root.right
                root.right = temp
                helper(root.left)
                helper(root.right)
            return 0

        helper(root)
        return root

if __name__ == "__main__":
    root = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))
    solution = Solution()
    test = solution.invertTree(root) 
    printList = [root.val]
    
    def helper(root, printList):
        if root.left:
            printList.append(root.left.val)
        if root.right:
            printList.append(root.right.val)
        if root.left:
            helper(root.left, printList)
        if root.right:
            helper(root.right, printList)        

    helper(root, printList)
    print(printList)
        
        
        
