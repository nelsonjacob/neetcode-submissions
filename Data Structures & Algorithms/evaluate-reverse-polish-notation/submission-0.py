class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        
        The operators include '+', '-', '*', and '/'.

        Assume that division between integers always truncates toward zero.

        

        tokens = ["1","2","+","3","*","4","-"]
        (int) are in the string format
        '''


        stack = []
        
        for token in tokens:
            if token == '+':
                o2 = stack.pop()
                o1 = stack.pop()

                stack.append(o1 + o2)
                continue

            if token == '-':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(o1 - o2)
                continue

            if token == '*':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(o1 * o2)
                continue

            if token == '/':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(int(o1 / o2)) # -3.6 trunc to -3
                continue

            # case in which we have an integer  
            # Assumption is token is a str rep of an integer

            stack.append(int(token))




        return stack[-1]

        