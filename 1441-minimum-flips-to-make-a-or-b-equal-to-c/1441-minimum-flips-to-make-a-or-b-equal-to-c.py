class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            lsb_a = a & 1
            lsb_b = b & 1
            lsb_c = c & 1
            flips += (((lsb_a | lsb_b) ^ 1) & lsb_c)
            flips += ((lsb_c ^ 1) & lsb_a)
            flips += ((lsb_c ^ 1) & lsb_b)
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
            
        

        