from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        cur = head
        group = 0
        count = 0
        while cur:
            count += 1
            cur = cur.next
        group = count // k * k
        if count < 0 or group == 0: return head

        dumN = ListNode()
        headDum = dumN
        prev = None
        tail = head
        prevTail = None
        while head and group > 0:
            temp = head.next
            headDum.next = head
            head.next = prev
            prev = head
            head = temp

            if group % k == 1:
                headDum = tail
                prevTail = tail
                tail = head
                prev = None
            group -= 1
            
        if tail is not None:
            prevTail.next = tail
        return dumN.next
    
# Giải thích:
# Bài này có 2 vấn đề cần giải quyết: 
# 1. tìm cái group link-lít với k phần tử
# 2. là reverse group đó
# sẽ có những trường hợp đặc biệt cần loại trừ sớm như
# - k=1 nó có nghĩa là không reverse tại vì nó đi reverse group có 1 phần tử vô nghĩa
# - link-list rỗng
# - k > len(link-list)
# Mình sẽ duyệt qua link-list và đếm số lượng phần từ group trước
# sau đó mình sẽ tính lại group = len(link-list) // k * k
# lúc này group sẽ là số phần tử cần duyệt để nghịch đảo
# ta thấy đuôi của group này sẽ là đầu của group kia nên ta cần 1 biến tail để làm head cho group sau
# group ban đầu là n*k và sẽ giảm dần về 0
# ở giá trị mà group % k = 1 thì đó là lúc ta phải set head mới cho group tiếp theo bằng tail của group trước đó 
# và cập nhật tail mới cũng chính là head đầu tiên của group tiems theo
# trong trường hợp group == len(link-list)
# thì tail == none.
# trong trường hợp group > len(link-list)
# thì tail đầu của group tiếp theo nhưng vì group tiếp theo ko đủ phần tử nên đã break while
# lúc này ta cần nối group chưa đủ phần tử đó vào link-list mới này
# để làm được điều đó ta cần prevTail đẻ nhớ được vị trí tail trước đó để nối 
# prevTail.next = tail.
