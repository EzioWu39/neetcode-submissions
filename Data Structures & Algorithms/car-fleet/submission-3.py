class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        def can_catch(
            target: int, 
            position_1: int, 
            position_2: int, 
            speed_1: int, 
            speed_2: int
        ) -> bool:
            if speed_1 <= speed_2:
                return False
            if speed_1 * ((position_2 - position_1)/(speed_1 - speed_2)) + position_1 > target:
                return False
            return True

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(cars)):
            pos, spe = cars[i][0], cars[i][1]
            if not stack:
                stack.append((pos, spe))
            else:
                while stack and can_catch(target, stack[-1][0], pos, stack[-1][1], spe):
                    stack.pop()
                stack.append((pos, spe))
        return len(stack)