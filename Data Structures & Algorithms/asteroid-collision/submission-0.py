class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        asteroids all move at the same speed
        positive asteroids move right ----->
        negative asteroids move left <-----


        If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.


        '''
        
        stack = []


        for asteroid in asteroids:

            if not stack or asteroid > 0:
                stack.append(asteroid)
                
            else: # asteroid < 0
                
                winner = asteroid
                while stack and stack[-1] > 0:

                    contestor = stack.pop()

                    if contestor > abs(asteroid):
                        winner = contestor
                        break
                    elif contestor == abs(asteroid):
                        winner = None
                        break
                    else:
                        # the asteroid is greater than the other asteroid
                        continue
                    
                    
                if winner:
                    stack.append(winner)
        
        return stack