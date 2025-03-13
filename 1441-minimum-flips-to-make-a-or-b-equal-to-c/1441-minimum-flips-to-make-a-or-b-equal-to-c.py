class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        _a , _b, _c = a, b, c
        flips = 0
        while _c > 0:
            lsb_a, lsb_b, lsb_c = _a & 1, _b & 1, _c & 1
            flips += ((lsb_a ^ 1) & (lsb_b ^ 1) & lsb_c)
            flips += ((lsb_c ^ 1) & lsb_a)
            flips += ((lsb_c ^ 1) & lsb_b)
            _c = _c >> 1
            _a = _a >> 1
            _b = _b >> 1
        while _a > 0:
            flips += (_a & 1)
            flips += (_b & 1)
            _a = _a >> 1
            _b = _b >> 1
        while _b > 0:
            flips += (_b & 1)
            _b = _b >> 1
        return flips
        

        