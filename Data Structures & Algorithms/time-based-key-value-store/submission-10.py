class TimeMap:

    def __init__(self):
        self.t_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = [(timestamp, value)]
            return

        self.t_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t_map:
            return ""
        timestamps = self.t_map[key]
        l, r = 0, len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid][0] > timestamp:
                r = mid - 1
            elif timestamps[mid][0] < timestamp:
                l = mid + 1
            else:
                break
        mid = (l + r) // 2
        t, v = timestamps[mid]
        return v if t <= timestamp else ""
                



        
