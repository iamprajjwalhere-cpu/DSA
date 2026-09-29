class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int m = needle.size();
        
        if (m == 0) {
            return 0;
        }       
        for (int i = 0; i <= n - m; i++) {
            int q = 0;           
            while (q < m && haystack[i + q] == needle[q]) {
                q++;
            }           
            if (q == m) {
                return i;
            }
        }
        
        return -1;
    }
};