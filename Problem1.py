## Problem 1

# Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(N) 
        Where N is the total number of nodes in the tree. We visit every single node 
        in the tree exactly once.
        
        Space Complexity: O(H) 
        Where H is the height of the tree. This accounts for the maximum depth of the 
        recursive call stack. In the worst-case scenario (a highly skewed tree), 
        H could be N, making it O(N). In the best-case (a perfectly balanced tree), 
        the height is log(N), making space complexity O(log N).
        """
        result = []

        def dfs(root, level):
            nonlocal result

            # Base case: If we reach a null node, we backtrack.
            if not root:
                return

            # The logic relies on visiting the right side of the tree first.
            # Whenever our current level equals the size of our result array, 
            # it means this is the very first node we are encountering at this depth.
            # Because we prioritize right-branch traversal, this guaranteed to be the 
            # rightmost node at the current level.
            resLen = len(result)
            if level == resLen:
                result.append(root.val)

            # Traverse the right child first to ensure rightmost nodes are processed 
            # and added to our result before any left nodes at the same level.
            dfs(root.right, 1 + level)
            
            # Traverse the left child next. Left nodes will only be added if there 
            # is no right node at that particular depth (i.e., if level == resLen).
            dfs(root.left, 1 + level)

        # Kick off the depth-first search starting at the root (level 0).
        dfs(root, 0)
        
        return result




        # DFS Solution
        # result = []

        # def dfs(root, level):
        #     nonlocal result

        #     if not root:
        #         return

        #     resLen = len(result)
        #     if level == resLen:
        #         result.append(root.val)

        #     dfs(root.right, 1 + level)
        #     dfs(root.left, 1 + level)  

        # dfs(root, 0)
        # return result