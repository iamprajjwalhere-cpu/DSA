#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if (s.empty() || words.empty()) return res;

        int word_len = words[0].length();
        int num_words = words.size();
        int total_len = word_len * num_words;
        int s_len = s.length();

        unordered_map<string, int> word_counts;
        for (const string& w : words) {
            word_counts[w]++;
        }
        for (int i = 0; i < word_len; ++i) {
            int left = i;
            int right = i;
            unordered_map<string, int> current_counts;
            int words_used = 0;

            while (right + word_len <= s_len) {

                string w = s.substr(right, word_len);
                right += word_len;

                if (word_counts.count(w)) {
                    current_counts[w]++;
                    words_used++;

                    while (current_counts[w] > word_counts[w]) {
                        string left_w = s.substr(left, word_len);
                        current_counts[left_w]--;
                        words_used--;
                        left += word_len;
                    }

                    if (words_used == num_words) {
                        res.push_back(left);
                    }
                } else {
                    current_counts.clear();
                    words_used = 0;
                    left = right;
                }
            }
        }
        return res;
    }
};
