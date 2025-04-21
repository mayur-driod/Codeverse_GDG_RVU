# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        op = ['{', '[', '(']
        cl = ['}', ']', ')']
        stack = []

        if len(s) < 2:
            return False

        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl:
                if not stack or stack[-1] != op[cl.index(i)]:
                    return False
                stack.pop()
        
        return not stack

# Binary Tree Inorder Traversal (recursive approach)
class Solution(object): 
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

# Binary Tree Inorder Traversal (Stack based Non-recursive approach)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        stk = []

        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res
        

#Trapping Rain Water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        lm = height[l]
        rm = height[r]
        quant = 0

        while l<r:
            if lm < rm:
                l+=1
                lm = max(lm,height[l])
                quant += lm - height[l]
            else:
                r -= 1
                rm = max(rm,height[r])
                quant += rm-height[r]
        return quant        


# simplify Path


        
