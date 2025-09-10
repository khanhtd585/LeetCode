class Solution:
    def minWindow(self, s: str, t: str) -> str:
        max_int = len(s) + 1
        l, r = 0, 0
        count_win, count_t = {}, {}
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        have, need = 0, len(count_t)
        res_len = max_int
        res_pos = [0, 0]
        
        for r in range(len(s)):
            count_win[s[r]] = 1 + count_win.get(s[r], 0)
                
            if s[r] in count_t and count_win[s[r]] == count_t[s[r]]:
                have += 1
            
            if have == need:
                while have == need:
                    count_win[s[l]] -= 1
                    if s[l] in count_t and count_win[s[l]] < count_t[s[l]]:
                        have -= 1
                    l += 1
                if res_len > (r - (l - 1) + 1):
                    res_len = (r - (l - 1) + 1)
                    res_pos = [l-1, r+1]
            r += 1
        l, r = res_pos
        return s[l: r]

sol = Solution()
s = "OUZODYXAZV"
t = "XYZ"
print(sol.minWindow(s, t))