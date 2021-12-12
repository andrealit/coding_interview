# letter combinations of a phone number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# the number could represent

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # length is small, only four
        # case 0: check for empty string
        if len(digits) == 0:
            return []
        
        # assign letters to digits
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                  "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # if the final path is the same length as the digits, we're good
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            # get letters the current digit represents and loop
            possible_combo = letters[digits[index]]
            
            for letter in possible_combo:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
                
        # do backtracking
        combinations = []
        backtrack(0, [])
        return combinations
        