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

# Binary Tree Inorder Traversal

        
