# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == '__main__':
    a = [2,4,7,6,5,,6,8,9,10]
    s  = Solution()
    s.minDepth(a)
    


                        5
                    /      \
                   5         8
                 /   \       / \
               8     10     9  14
              / \    / \
            15  11  13  10
