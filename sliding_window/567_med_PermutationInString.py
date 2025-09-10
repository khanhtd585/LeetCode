class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                print(need, cur, count1, count2)
                if cur == need:
                    return True
        return False
    
    
    def checkInclusion_dict(self, s1: str, s2: str) -> bool:
        d1 = {}
        for c in s1:
            d1[c] = 1 + d1.get(c, 0)
        for i in range(len(s2) - len(s1) + 1):
            d2 = {}
            for c in s2[i: i+len(s1)]:
                d2[c] = 1 + d2.get(c, 0)
            if d1 == d2:
                return True
        return False
    
    def checkInclusion_sliding(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
sol = Solution()
s1 = "abca"
s2 = "lecaabee"
print(sol.checkInclusion_sliding(s1, s2))

# comment block
# hướng giải đầu tiên là dùng 2 dict để đếm tần số các kí tự trong s1 và s2
# sau đó so sánh 2 dict với nhau, nếu bằng nhau thì return True
# cách này sẽ tốn O(n*m) time và O(m) space, trong đó n là độ dài s2, m là độ dài s1
# cũng một cách khác dùng dict để chứa count của s1 và s2 
# nhưng check tầng suất xuất hiện của từng kí tự trong windown s2
# nếu vượt quá tần suất của s1 thì break, nếu tất cả các kí tự trong windown s2 đều có tần suất
# trong s1 thì return True
# cách này tốn O(n*m) time và O(m) space
# cách tối ưu hơn là dùng sliding window
# Ý tưởng là chỉ cần so sánh tần suất của 26 chữ cái trong bảng chữ cái
# nếu tần suất của tất cả các chữ cái đều bằng nhau thì return True
# cách này tốn O(n) time và O(1) space
# Nhưng mà nó hơi khó hiểu :))
# để làm được thì cũng dùng static sliding window kích thước len(s1)
# sau đó dùng biến matches để đếm số lượng chữ cái có tần suất bằng nhau 
# trường hợp dịch sang bên phải của node right thì thêm tần suất của chữ cái mới vào
# và nếu tần suất của chữ cái mới bằng tần suất trong s1 thì tăng matches lên 1
# nếu tần suất của chữ cái mới vượt quá tần suất trong s1 thì giảm matches đi 1
# tương tự với node left thì giảm tần suất của chữ cái bị bỏ đi 
# nếu tần suất của chữ cái bị bỏ đi bằng tần suất trong s1 thì tăng matches lên 1
# nếu tần suất của chữ cái bị bỏ đi thấp hơn tần suất trong s1 thì giảm matches đi 1
# cuối cùng nếu matches == 26 thì return True
