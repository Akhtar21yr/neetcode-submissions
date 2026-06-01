class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        while min_speed <= max_speed:
            speed = (min_speed + max_speed) // 2

            _hours = 0
            for pile in piles:
                _hours += pile // speed if pile % speed == 0 else pile // speed + 1

            if h >= _hours:
                max_speed = speed - 1
            else:
                min_speed = speed + 1

        return min_speed