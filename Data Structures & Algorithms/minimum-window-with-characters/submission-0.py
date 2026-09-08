class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        
        res = [-1, -1]
        res_len = float('inf')
        need = len(freq_t)
        have = 0
        l = 0
        freq_s = {}

        for r in range(len(s)):

            if s[r] in freq_t:
                freq_s[s[r]] = freq_s.get(s[r], 0) + 1

                if freq_s[s[r]] == freq_t[s[r]]:
                    have += 1
                
            while have == need:

                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                if s[l] in freq_t:
                    freq_s[s[l]] -= 1
                    
                    if freq_s[s[l]] < freq_t[s[l]]:
                        have -= 1
                
                l += 1


        l, r = res

        return s[l: r + 1] if res != float('inf') else ""
