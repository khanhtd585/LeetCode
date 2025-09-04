def largestRectangleArea(heights: list[int]) -> int:
        stack = []
        max_rec = 0
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                t_i, t_h = stack.pop()
                max_rec = max(max_rec, ((i-t_i) * t_h))
                index = t_i
            stack.append((index,h))
            
        while stack:
            t_i, t_h = stack.pop()
            max_rec = max(max_rec, ((len(heights)-t_i) * t_h))
        return max_rec
            
        
        
heights = [7,1,7,2,2,4]
# heights = [2,1,5,6,2,3]
heights = [5,5,1,7,1,1,5,2,7,6]
print(largestRectangleArea(heights))