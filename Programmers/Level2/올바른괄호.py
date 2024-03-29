def solution(s):
    stack = list()
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                
    if len(stack) == 0:
        return True
    else:
        return False
