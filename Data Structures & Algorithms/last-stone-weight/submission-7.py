
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [2, 3, 6, 2, 4]
        6,4 => 2
        [2,2,2,3]
        2,3 => 1
        [2, 2, 1]
        2, 1
        1
        """
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stoneA = heapq.heappop(heap)
            stoneB = heapq.heappop(heap)
            if stoneA != stoneB:
                heapq.heappush(heap, -abs(stoneA - stoneB))
        
        return -heap[0] if heap else 0

        """
        [1,2]
        heap = [-2, -1]
        -2, -1
        -1

        """