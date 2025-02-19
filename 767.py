from collections import Counter, deque
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        heap = []
        q = deque()

        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))

        result = []
        while heap or q:
            if q and q[0][2] < len(result):
                key, freq, _ = q.popleft()
                heapq.heappush(heap, (freq, key))

            if not heap:
                break

            freq, key = heapq.heappop(heap)
            result.append(key)
            freq += 1

            if freq < 0:
                q.append((key, freq, len(result)))

        return "".join(result) if len(result) == len(s) else ""