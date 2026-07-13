class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
           return []
      
        # Mappings of digits to letters as found on a phone dialpad
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = ['']
        for digit in digits:
            tmp = []
            for curStr in combinations:
                for c in digitToChar[digit]:
                    tmp.append(curStr+c)
            combinations = tmp
        
        return combinations
        