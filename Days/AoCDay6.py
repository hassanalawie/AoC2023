import numpy
import math
class AoC():
    def __init__(self):
        self.boat_rides = open('files/boat_times.txt', 'r').readlines()

    def quadratic_equation_solve(self, time, distance):
        return (math.ceil((time / 2) - math.sqrt((time / 2) ** 2 - (distance +1))),
                math.floor((time / 2) + math.sqrt((time / 2) ** 2 - (distance + 1))))
    def formatLine(self, arr):
        new_arr = []
        for num in arr:
            if num == "":
                continue
            num = num.strip()
            new_arr.append(int(num))
        return new_arr
    def parseInput(self):
        split_arr = self.boat_rides
        split_arr[0].replace("\n","")
        time_arr_unformatted = split_arr[0].split(" ")[1:]
        distance_arr_unformatted = split_arr[1].split(" ")[1:]
        time_arr = self.formatLine(time_arr_unformatted)
        distance_arr = self.formatLine(distance_arr_unformatted)
        return [time_arr, distance_arr]


    def daySixPartOne(self):
        mat = self.parseInput()
        current_row = 0
        max_row = len(mat[0])
        win_list = []
        while current_row < max_row:
            wins = 0
            root1, root2 = self.quadratic_equation_solve(mat[0][current_row], mat[1][current_row])
            root1 = math.floor(root1)
            root2 = math.floor(root2)
            if root1 == None:
                print("0")
                return
            elif root1 == root2:
                wins = 1
            else:
                wins = root2 - root1 + 1
            win_list.append(wins)
            current_row += 1
        
        print(f"Final Answer: {numpy.prod(win_list)}")



    def daySixPartTwo(self):
        mat = self.parseInput()
        time = int(''.join([str(n) for n in mat[0]]))
        distance = int(''.join([str(n) for n in mat[1]]))
        root1, root2 = self.quadratic_equation_solve(time, distance)
        print(f"Final Answer: {root2 - root1 + 1}")


    

if __name__ == '__main__':
    advent = AoC()
    advent.daySixPartOne()
    advent.daySixPartTwo()




