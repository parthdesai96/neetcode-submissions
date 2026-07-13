class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        result = [];
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in myMap:
                myMap[sortedString].append(string)
            else:
                myMap[sortedString] = [string]

        for values in myMap.values():
            result.append(values)
        return result
        