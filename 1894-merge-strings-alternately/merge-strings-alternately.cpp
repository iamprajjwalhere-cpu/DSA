#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string result = "";

        result.reserve(word1.length() + word2.length());
        
        int i = 0, j = 0;
        int m = word1.length(), n = word2.length();
        
        while (i < m || j < n) {
            if (i < m) {
                result += word1[i++];
            }
            if (j < n) {
                result += word2[j++];
            }
        }
        
        return result;
    }
};