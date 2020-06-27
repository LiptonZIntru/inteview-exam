# Task 3: finished v 9:01 26.6.2020

class Solution: 
    def longestPalindrome(self, s):
        begin = 0
        end = len(s) - 1
        palindrom = ""

        for char in range(len(s)):
            counter = 0
            for i in s[char + 1 : len(s)][::-1]:
                counter = counter + 1
                if s[char] == i:
                    begin = char
                    end = len(s) - counter

                    diff = int((end - begin) / 2)

                    pal_begin = ""
                    pal_end = ""
                    is_valid = True

                    for a in range(diff + 1):
                        first_char = s[begin + a]
                        last_char = s[end - a]
                        if first_char == last_char:
                            if not begin + a == end - a:
                                pal_begin = pal_begin + first_char
                            pal_end = last_char + pal_end
                        else:
                            is_valid = False
                            break
                    if is_valid and len(palindrom) < len(pal_begin + pal_end):
                        palindrom = pal_begin + pal_end

        return palindrom
        
# Test program
s = "tracecars"
s = "eerreeeeerrrrrrreee"
print(str(Solution().longestPalindrome(s)))
# racecar