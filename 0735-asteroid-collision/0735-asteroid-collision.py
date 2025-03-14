class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            if asteroid > 0:
                break
            i += 1
        for j in range(i+1, len(asteroids)):
            curr = asteroids[j]
            if curr > 0 or len(stack) == 0:
                stack.append(curr)
            else:
                top = stack.pop()
                while top < -curr and top > 0 and len(stack) > 0:
                    top = stack.pop()
                if top > -curr:
                    stack.append(top)
                elif top < 0:
                    stack.append(top)
                    stack.append(curr)
                elif top < -curr:
                    stack.append(curr)
        return stack
                





        