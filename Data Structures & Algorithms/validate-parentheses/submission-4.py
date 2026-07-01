class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        bracket_dict = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        stack = []
        for bracket in s:
            if bracket in bracket_dict.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracket_dict[stack.pop()] != bracket:
                    return False
        

        return len(stack) == 0