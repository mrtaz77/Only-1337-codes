class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mask = 1
        _a , _b, _c = a, b, c
        flips = 0
        while _c > 0:
            flips += (((_a & mask) ^ 1) & ((_b & mask) ^ 1) & (_c & mask))
            flips += (((_c & mask) ^ 1) & (_a & mask))
            flips += (((_c & mask) ^ 1) & (_b & mask))
            _c = _c >> 1
            _a = _a >> 1
            _b = _b >> 1
        while _a > 0:
            flips += (_a & mask)
            flips += (_b & mask)
            _a = _a >> 1
            _b = _b >> 1
        while _b > 0:
            flips += (_b & mask)
            _b = _b >> 1
        return flips
        

        