from collections import deque
class HitCounter:

    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            # Do a cleanup ; we only need upto 300 seconds worth of hits in the queue
            # we are finding out the time passed between the first hit and the latest hit. 
            diff = timestamp - self.hits[0]
            # if it is greater than or equals 300, we clear out the old records
            if diff >= 300:
                self.hits.popleft()
            else:
                break

        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
