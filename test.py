def makeTree(n,array):
    if n == 0:
        return None
    if len(array) == 1:
        return TreeNode(n)
    c = 0
    i = array.index(n)
    tree = TreeNode(n)
    if not array[:i+c]:
        array.insert(0,0)
        c += 1
    if not array[i+c:]:
        array.append(0)
    for left in array[:i+c]:
        for right in array[i+c:]:
            tree.left = makeTree(left, array[:i+c])
            tree.right = makeTree(right, array[i+c:])
    return tree


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        array = []
        dp = [i for i in range(1,n+1)]
        c = 0
        for i in dp:
            if not dp[:i]:
                dp.insert(0,0)
                c += 1
            if not dp[i:]:
                dp.append(0)
            tree = TreeNode(i)
            for left in dp[:i+c]:
                for right in dp[i+c:]:
                    tree.left = makeTree(left, dp[:i+c])
                    tree.right = makeTree(right, dp[i+c:])
                    array.append(tree)
        return array



        