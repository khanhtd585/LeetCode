from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0]) 
        res, visit = set(), set()
        
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        def dfs(r, c, node: TrieNode, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r,c) in visit  
                or board[r][c] not in node.children
            ):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                
                res.add(word)
            
            dfs(r-1,c, node, word)
            dfs(r+1,c, node, word)
            dfs(r,c-1, node, word)
            dfs(r,c+1, node, word)
            
            visit.remove((r,c))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j, root, "")
        
        return list(res)
            


board=[["a","b","c"],["a","e","d"],["a","f","g"]]
words=["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]

sol = Solution()
print(sol.findWords(board, words))

# ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]















