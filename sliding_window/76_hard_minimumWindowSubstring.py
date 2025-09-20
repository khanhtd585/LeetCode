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
            
            while have == need:
                if res_len > (r - l + 1):
                    res_len = (r - l + 1)
                    res_pos = [l, r+1]

                count_win[s[l]] -= 1
                if s[l] in count_t and count_win[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res_pos
        return s[l: r]

sol = Solution()
s = "OUZODYXAZV"
t = "XYZ"
print(sol.minWindow(s, t))

# Bài toán yêu cần tìm chuỗi con ngắn nhất trong chuỗi s chứa tất cả các ký tự của chuỗi t.
# Nhưng chuỗi con t có thế chứa ký tự trùng lặp. nên làm bài này khó hơn
# Cách giải quyết là dùng sliding window với 2 con trỏ l, r
# Nhưng thay vì chỉ cần tất cả các ký tự trong t xuất hiện trong cửa sổ [l, r]
# thì cần phải đảm bảo tần suất xuất hiện của các ký tự trong cửa sổ [l, r] phải lớn hơn hoặc bằng tần suất xuất hiện của các ký tự trong t
# Để làm được điều này thì dùng 2 dict để đếm tần suất xuất hiện của các ký tự trong t và trong cửa sổ [l, r]
# Sau đó dùng biến have để đếm số lượng ký tự trong cửa sổ [l, r] có tần suất xuất hiện bằng tần suất xuất hiện trong t
# Khi have == need thì có nghĩa là tất cả các ký tự trong t đều xuất hiện trong cửa sổ [l, r] với tần suất đúng
# Lúc này thì thu nhỏ cửa sổ [l, r] bằng cách dịch con trỏ l sang phải
# Đồng thời cập nhật kết quả nếu cửa sổ hiện tại nhỏ hơn kết quả trước đó.