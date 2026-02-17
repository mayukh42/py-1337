
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
            if not stack:
                # got an orphan paren
                return False
            last = stack.pop()
            if state_map[ss[i]] is not last:
                return False
    return True


def is_balanced_by_count(ss):
    # normalize the string with only one type of parens
    ss = ss.replace("{", "(", -1)
    ss = ss.replace("[", "(", -1)
    ss = ss.replace("}", ")", -1)
    ss = ss.replace("]", ")", -1)

    # 0/1 states: 0 = closed, 1 = open
    state = 0
    for i in range(len(ss)):
        if ss[i] == "(":
            state += 1
        elif ss[i] == ")":
            state -= 1

    return state == 0

