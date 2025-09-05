class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = {}
        rs = 0
        l = 0
        for r in range(len(s)):
            if s[r] in sub_str:
                l = max(l, sub_str[s[r]] + 1)
            sub_str[s[r]] = r
            rs = max(rs, (r-l+1))
        return rs

sol = Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))

# Ý tưởng là dùng dynamic sliding window trượt từ trái sang phải để tìm longest sub str
# đầu tiên ta cứ mở rộng phạm vi window theo hường bên phải
# Khi gặp char duplicate (char trong window) thì thu hẹp window từ bên trái
# ta cần các biến sau:
#   left: vị trí start của window 
#   right: vị trí end của window 
#   sub_str: lưu sub_str tạm thời để tính độ dài
#   rs: kết quả trả về
# Dùng for loop để duyệt qua toàn bộ string và add các char và sub_str
# Khi gặp char duplicate thì dùng while loop để remove các phần tử ở phía trái của sub_str với mục đích là thu hẹp window và cạp nhật vị trí left
# công thức để tìm và tính độ dài các longest_sub_str là: r - l + 1 (l là điểm start của win, r là điểm end của win, 1 là bù số)
# Ta thấy giải pháp trên ổn nhưng
# với r sẽ được cập nhật sau mỗi for loop
# vấn đề là ở việc cập nhật l bằng while loop có thể tối ưu không?
# Nhận thấy mục đích của while loop là cập nhật vị trí left
# để cập nhật l ta chỉ cân xác định được vị trí của các char đã xuất hiện trong substring là được không nhất thiết phải while loop
# và khi phát hiện duplicate ta chỉ cần nhảy tới vị trí của char duplicate và + 1 để loại bỏ char trùng.
# có nghĩ là ta cập nhật vị trí l bằng cach nhảy tới vị trí sau vị trí trùng là được: l = sub_str[char_dub] + 1
# như vậy sẽ không cần phải while loop để cập nhật l
# và để làm được điều đó ta chỉ cần lưu vị trí của các char trên str. đối với các chả trùng thì cứ lấy vị trí mới nhất vì chúng ta duyệt từ trái sang phải.
# việc update vị trí các chả cũng chỉ cần nằm trong for loop là đủ. Vậy nó tối ưu được while loop
# Time complexity : O(n) 1 for loop
# Space complexity : O(m) m các char unique trong str (các char xuất hiện trong str)

