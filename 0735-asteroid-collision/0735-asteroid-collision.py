class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            last = 0
            if stack and asteroid < 0 and stack[-1] > 0:
                last = 0
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                   last = stack.pop()
                if stack: 
                    if stack[-1] == -asteroid:
                        stack.pop()
                    elif stack[-1] < 0:
                        stack.append(asteroid)
                elif last < -asteroid:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
            
        return stack
            
                





        