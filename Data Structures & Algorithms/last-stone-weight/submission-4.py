
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stoneA = heapq.heappop(stones)
            stoneB = heapq.heappop(stones)
            if stoneA != stoneB:
                heapq.heappush(stones, -abs(stoneA - stoneB))
        return -stones[0] if stones else 0
        # if heapq:
        #     return stones[0]
        # else:
        #     return 0