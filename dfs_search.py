class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_preorder(root):
    result = []

    def dfs(node):
        if not node:
            return

        # 1) visit current node
        result.append(node.val)

        # 2) go left
        dfs(node.left)

        # 3) go right
        dfs(node.right)

    dfs(root)
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(dfs_preorder(root))
