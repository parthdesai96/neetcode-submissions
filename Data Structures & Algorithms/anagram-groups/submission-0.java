class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> stringMaps = new HashMap<>();
        for(String s : strs)
        {
            char[] sortedString = s.toCharArray();
            Arrays.sort(sortedString);
            String key = new String(sortedString);
            if(!stringMaps.containsKey(key))
                stringMaps.put(key, new ArrayList<>());
            stringMaps.get(key).add(s);
        }
        return new ArrayList<>(stringMaps.values());
    
    }
}
