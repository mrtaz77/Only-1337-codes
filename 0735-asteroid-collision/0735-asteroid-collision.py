class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            last = 0
            if stack and asteroid < 0 and stack[-1] > 0:
                last = 0
                while stack and stack[-1] > 0 and asteroid < 0:
                    last = stack.pop()
                    if last == -asteroid:
                        break
                    if last > -asteroid:
                        stack.append(last)
                        break
                if last < -asteroid:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
            
        return stack
            
                





        