## Problem 2

# Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        BFS Solution
        Time Complexity: O(N) where N is the number of nodes in the tree. In the worst case, we visit every node.
        Space Complexity: O(N) because the queue can hold at most N/2 nodes at the lowest level of a balanced tree.
        """
        q = collections.deque()
        q.append(root)
        
        # Traverse the tree level by level
        while q:
            size = len(q)
            xfound = yfound = False
            
            # Process all nodes at the current level
            for i in range(size):
                curr = q.popleft()
                
                # Check if we found x or y at this level
                if curr.val == x:
                    xfound = True
                elif curr.val == y:
                    yfound = True
                    
                # Check if x and y share the same parent (siblings, not cousins)
                if curr.left and curr.right:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False
                        
                # Queue the children for the next level's processing
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            # If one is found but not the other at the same level, they aren't cousins
            if xfound and not yfound:
                return False
            if yfound and not xfound:
                return False
                
            # If both are found at the current level and didn't share a parent, they are cousins
            if xfound and yfound:
                return True

        return False

        """
        # DFS Solution
        # Time Complexity: O(N) where N is the number of nodes, as we may visit all nodes.
        # Space Complexity: O(H) where H is the height of the tree due to the recursion stack. 
        #                   In the worst case (skewed tree) it's O(N), in the best (balanced) it's O(log N).
        
        # sameParent = False
        # xlevel = ylevel = 0
        
        # def dfs(root, level):
        #     nonlocal sameParent, x, y, xlevel, ylevel
            
        #     # Base case: if node is null, stop traversing
        #     if not root:
        #         return
                
        #     # Record the depth level if we find x or y
        #     if root.val == x:
        #         xlevel = level
        #     if root.val == y:
        #         ylevel = level
                
        #     # Check if the current node is the parent of both x and y
        #     if root.left and root.right:
        #         if root.left.val == x and root.right.val == y:
        #             sameParent = True
        #         if root.left.val == y and root.right.val == x:
        #             sameParent = True
                    
        #     # Continue DFS traversal down the left and right subtrees, incrementing the level
        #     dfs(root.left, 1 + level)
        #     dfs(root.right, 1 + level)
            
        # dfs(root, 0)
        
        # # To be cousins, they must be on the same level but have different parents
        # return xlevel == ylevel and not sameParent
        """