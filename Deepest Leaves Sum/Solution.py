class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curr = [root]
        while curr:
            prev, curr = curr, [child for p in curr for child in [p.left, p.right] if child]
        return sum(node.val for node in prev)
