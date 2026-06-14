class TimeMap:

    def __init__(self):
        self.tmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = [(value, timestamp)]
        else:
            self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        ans = -1
        left, right = 0, len(self.tmap[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            tmp = self.tmap[key][mid][1]
            if tmp <= timestamp:
                ans = mid
                left = mid + 1
            if tmp > timestamp:
                right = mid - 1
        return "" if ans == -1 else self.tmap[key][ans][0]