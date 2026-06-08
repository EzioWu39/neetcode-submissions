class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter, defaultdict
        heap = []
        feq = Counter() # feq = defaultdict(int)
        for num in nums:
            feq[num] += 1
        for key, v in feq.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key))
            else:
                if heap[0][0] < v:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (v, key))
        return [tup[1] for index, tup in enumerate(heap)]