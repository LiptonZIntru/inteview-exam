# Ukol 2: dokonceno v 2:36 26.6.2020

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        biggest = ""
        sub_string = ""
        for char in s:
            sub_string = sub_string + char
            #print(sub_string)
            # find duplicates
            for i in range(len(sub_string) - 1):  # i = 0 -> 18-1
                for a in sub_string[i + 1:len(sub_string)]:
                    print(sub_string[i], a)
                    print(i, sub_string)
                    print('------')
                    if sub_string[i] == a:
                        sub_string = ""  
                
            if len(sub_string) > len(biggest):
                biggest = sub_string
        return len(biggest)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10