# Task 4 finished at 22:28 27.6.2020
class Solution:
    def isValid(self, s):
        # my code (it doesn't work)
        open_brackets = ['{', '(', '[']
        close_brackets = ['}', ')', ']']

        '''print(s)
        if not bracket_type == -1:
            print('Close: ' + close_brackets[bracket_type])

        print('---------')

        if s == '':
            return True

        char = s[0]

        for bracket in range(len(open_brackets)):
            if open_brackets[bracket] == char:
                return self.isValid(s[1 : len(s)], bracket_type=bracket)
        if not close_brackets[bracket_type] == char:
            return False
        return True'''

        # custom implementation of someone's code
        valid = []

        for char in s:
            for bracket in open_brackets:
                if char == bracket:
                    valid.append(char)
                    break
            else:
                last_open_bracket = valid.pop()
                target_bracket = ''

                for bracket in range(len(close_brackets)):
                    if open_brackets[bracket] == last_open_bracket:
                        target_bracket = bracket
                if not char == close_brackets[target_bracket]:
                    return False
        if len(valid) == 0:
            return True
        return False



# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))