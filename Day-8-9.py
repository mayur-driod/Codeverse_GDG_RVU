# Implement stack using queue
class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for i in range(len(self.queue) -1):
            self.queue.append(self.queue.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
    
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0



# Implement stack using queue
class MyQueue(object):

    def __init__(self):
        self.inp = []
        self.out = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inp.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.out.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.out:
            while self.inp:
                self.out.append(self.inp.pop())
        return self.out[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.inp and not self.out
        


# Remove k digits:
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stk = []

        for i in num:
            if len(stk) == 0:
                stk.append(i)
            elif i<stk[-1] and k>0:
                while stk and i < stk[-1] and k > 0:
                    stk.pop()
                    k -= 1
                stk.append(i)
            else:
                stk.append(i)

        if k>0:
            stk = stk[:-k]

        return str(int("".join(stk))) if stk else "0"


      
# Design Circular Queue
