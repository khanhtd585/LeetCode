class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        rs = 0
        count = {}
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) 
            maxf = max(count[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            print(r, l, maxf, s[l:r+1])
            rs = max(rs, (r - l + 1))
        return rs

sol = Solution()
s = "ABBBA"
k = 2
print(sol.characterReplacement(s, k))


# block comment
# mục tiêu của bài là tìm độ dài của longest substring có thể thay thế tối đa k ký tự để tất cả các ký tự trong substring đều giống nhau.
# sử dụng sliding window để giải quyết bài toán này
# ban đầu cứ trượt và mở rộng window về bên phải, 
# lấy ký tự bên trái để làm chuẩn replace 
# và count số lần replace để khi bằng k thì ta sẽ tính độ dài window
# khi số lần replace vượt quá k thì ta sẽ thu hẹp window từ bên trái
# khi theo hướng trên ta sẽ gặp 1 vấn đề là ở trưởng hợp ABBBA với k = 2
# vấn đề là nên replace theo ký tự nào để được độ dài lớn nhất
# nhận thấy ta nên replace theo ký tự xuất hiện nhiều nhất trong window để được độ dài lớn nhất
# vậy làm sao để biết được ký tự nào xuất hiện nhiều nhất trong window và khi nào thì vượt quá k lần replace
# nhận thấy rằng ta có thể tính số ký tự cần replace bằng công thức: (r - l + 1) - maxf
# trong đó r là vị trí end của window, l là vị trí start của window,
# maxf là số lần xuất hiện của ký tự xuất hiện nhiều nhất trong window
# (r - l + 1) là độ dài window hiện tại
# (r - l + 1) - maxf là số lần ký tự cần replace
# để biết được maxf ta cần 1 biến count để đếm số lần xuất hiện của các ký tự trong window
# Khi đã xác định được số ký tự cần replace ta sẽ so sánh với k 
# để biết khi nào cần thu hẹp window và tiến hành thu hẹp window từ bên trái

# Bài học rút ra là: hãy nghĩ sâu hơn về vấn đề để tìm ra công thức giải quyết
# đừng chỉ nghĩ đơn giản là mở rộng window và thu hẹp window và thực hiện các thao tác replace ký tự trong window
