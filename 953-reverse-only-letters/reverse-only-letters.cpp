class Solution {
public:
    string reverseOnlyLetters(string s) {
        int p=0;
        int q=s.size()-1;
        while (p<q){
            if (isalpha(s[p]) && isalpha(s[q])){
                swap(s[p], s[q]);
                p++;
                q--;
            }
            if(!isalpha(s[p])){
                p++;
            }
            if(!isalpha(s[q])) {
                q--;
            }
        }
        return s;
    }
};