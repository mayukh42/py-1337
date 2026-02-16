
'''
    canonical balanced parenthesis problem

    examples 
    ()[]{} -> true
    ([]) -> true
    ([)] -> false
'''

def is_balanced_par(ss):
    state_map = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    state = ""
    stack = []
    for i in range(len(ss)):
        if ss[i] == "(":
            stack.append("(")
        elif ss[i] == "{":
            stack.append("{")
        elif ss[i] == "[":
            stack.append("[")
        elif ss[i] == ")" or ss[i] == "}" or ss[i] == "]":
            last = stack.pop()
            if state_map[ss[i]] is not last:
                return False
    return True


