from typing import List
import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.count, tweetId))
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].pop(0)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHip = []
        res = []
        self.followMap[userId].add(userId)
        for u in self.followMap[userId]:
            if u in self.tweet:
                index = len(self.tweet[u]) - 1
                ttime, tid = self.tweet[u][index]
                heapq.heappush(minHip, (ttime, tid, u, index-1))
        
        while minHip and len(res) < 10:
            ttime, tid, u, index = heapq.heappop(minHip)
            res.append(tid)
            
            if index >= 0:
                ttime, tid = self.tweet[u][index]
                heapq.heappush(minHip, (ttime, tid, u, index-1))
                
        return res

    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap.get(followerId, set()):
            self.followMap[followerId].remove(followeeId)
