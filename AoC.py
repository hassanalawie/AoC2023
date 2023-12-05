class AoC():
    def __init__(self):
        self.calibration_doc =  open('calibration_doc.txt', 'r').readlines()
        self.calibration_number_lookup = {
        "one":"o1e",
        "two":"t2o",
        "three":"t3e",
        "four":"f4r",
        "five":"f5e",
        "six":"s6x",
        "seven":"s7n",
        "eight":"e8t",
        "nine":"n9e"
    }
        self.games = open('games.txt', 'r').readlines()
        self.schematic = open('schematic.txt', 'r').readlines()
    
    def getTotalFromCalibration(self, file_info):
        total_sum = 0
        for item in file_info:
            value = (''.join(char for char in item if char.isnumeric()))
            total_sum += int(value[0]+value[-1])
        return total_sum

    def parseCubeGame(self, game):
        sets = game.split(":")[1].split(";")
        parsed = []
        for pull in sets:
            seperated_pull = pull.strip().split(',')
            set_dict = {}
            for color_amount in seperated_pull:
                color_amount_arr = color_amount.strip().split(" ")
                color = color_amount_arr[1]
                amount = color_amount_arr[0]
                set_dict[color] = int(amount)
            parsed.append(set_dict.copy())
            set_dict.clear()
        return parsed
    
    def validate_game(self, game):
        for pull in game:
            if pull.get('blue', 0) > 14 or pull.get('green', 0) > 13 or pull.get('red', 0) > 12:
                return False
        return True

    def in_schematic_bounds(self, i, j):
        max_rows = len(self.schematic)
        max_cols = len(self.schematic[0])
        return i >= 0 and i < max_rows and j >= 0 and j < max_cols
    
    def get_part_number_from_range(self, row, start, end):
        number = ""
        for col_index in range(start, end):
            number += self.schematic[row][col_index]
        return int(number)
    def get_number_from_schematic(self, i, j, left, right):
        original = (i, j)
        start = j
        end = j
        if left and right:
            # keep going left and return where number starts
            while self.in_schematic_bounds(i, j-1) and self.schematic[i][j-1].isnumeric():
                j -= 1
            start = j
            # keep going right and return where number ends
            j = original[1]
            while self.in_schematic_bounds(i, j+1) and self.schematic[i][j+1].isnumeric():
                j += 1
            end = j

            return (start, end)
        if left:
            end = j
            start = j
            while self.in_schematic_bounds(i, j-1) and self.schematic[i][j-1].isnumeric():
                j -= 1
            start = j
            return (start, end)
        if right:
            start = j
            end = j
            while self.in_schematic_bounds(i, j+1) and self.schematic[i][j+1].isnumeric():
                j += 1
            end = j
            return (start, end)

    def dayOnePartOne(self):
        print(self.getTotalFromCalibration(self.calibration_doc))
    
    def dayOnePartTwo(self):
        new = []
        for item in self.calibration_doc:
            for key in self.calibration_number_lookup.keys():
                if key in item:
                    item = item.replace(key, self.calibration_number_lookup[key])
            new.append(item)
        self.calibration_doc = new
        print(self.getTotalFromCalibration(self.calibration_doc))

    def dayTwoPartOne(self):
        valid_game_ids = set()
        for (i, game) in enumerate(self.games):
            game = self.parseCubeGame(game)
            if self.validate_game(game):
                valid_game_ids.add(i+1)
        print(sum(list(valid_game_ids)))
    
    def dayTwoPartTwo(self):
        total_sum = 0
        for game in self.games:
            game = self.parseCubeGame(game)
            max_blue = 0
            max_green = 0
            max_red = 0
            for pull in game:
                if 'blue' in pull:
                    max_blue = max(max_blue, pull['blue'])
                if 'green' in pull:
                    max_green = max(max_green, pull['green'])
                if 'red' in pull:
                    max_red = max(max_red, pull['red'])
            power = max_blue * max_green * max_red
            total_sum += power
        print(total_sum)

    def dayThreePartOne(self):
        seen = set()
        valid_number_set = set()
        for i in range(len(self.schematic)):
            for j in range(len(self.schematic[0].replace("\n",""))):
                if self.schematic[i][j] == "." or self.schematic[i][j].isnumeric():
                    continue
                else:
                    # Check each direction
                    directions = [
                        [-1,-1,True,True],
                        [-1,0,True,True],
                        [-1,1,True,True],
                        [0, 1, False, True],
                        [1,1,True, True],
                        [1,0,True,True],
                        [1,-1, True,True],
                        [0,-1,True,False]
                    ]
                    for direction in directions:

                        row = i + direction[0]
                        col = j + direction[1]
                        if self.schematic[row][col].isnumeric():
                            start, end = self.get_number_from_schematic(row, col, direction[2], direction[3])
                            valid_number_set.add((row, start, end+1))
                            values = range(start, end+1)
                            for value in values:
                                if (row, value) not in seen:
                                    seen.add((row, value))
        valid_numbers = []
        for number_range in list(valid_number_set):
            number = ""
            row = number_range[0]
            start = number_range[1]
            end = number_range[2]
            for col_index in range(start, end):
                number += self.schematic[row][col_index]
            valid_numbers.append(int(number))
        print(sum(valid_numbers))

                    
    def dayThreePartTwo(self):
        seen = set()
        valid_number_set = set()
        for i in range(len(self.schematic)):
            for j in range(len(self.schematic[0].replace("\n",""))):
                if self.schematic[i][j] == "." or self.schematic[i][j].isnumeric():
                    continue
                else:
                    # Check each direction
                    directions = [
                        [-1,-1,True,True],
                        [-1,0,True,True],
                        [-1,1,True,True],
                        [0, 1, False, True],
                        [1,1,True, True],
                        [1,0,True,True],
                        [1,-1, True,True],
                        [0,-1,True,False]
                    ]
                    for direction in directions:

                        row = i + direction[0]
                        col = j + direction[1]
                        if self.schematic[row][col].isnumeric():
                            start, end = self.get_number_from_schematic(row, col, direction[2], direction[3])
                            symbol = self.schematic[i][j]
                            valid_number_set.add((symbol, row, start, end+1, i, j))
                            values = range(start, end+1)
                            for value in values:
                                if (row, value) not in seen:
                                    seen.add((row, value))
        gears_dict = {}
        for part in list(valid_number_set):
            symbol = part[0]
            if symbol == "*":
                gear_coord = (part[4], part[5])
                if gear_coord in gears_dict:
                    if len(gears_dict[gear_coord]) > 0:
                        gears_dict[gear_coord] = gears_dict[gear_coord]+ [(part[1], part[2], part[3])]
                else:
                    gears_dict[gear_coord] = [(part[1], part[2],part[3])]
        valid_gears = []
        for key in gears_dict.keys():
            if len(gears_dict[key]) == 2:
                valid_gears.append(gears_dict[key])
        total_gear_ratio = 0
        for vd in valid_gears:
            gear1 = self.get_part_number_from_range(vd[0][0], vd[0][1], vd[0][2])
            gear2 = self.get_part_number_from_range(vd[1][0], vd[1][1], vd[1][2])
            gr = gear1*gear2
            total_gear_ratio += gr
        print(total_gear_ratio)

if __name__ == '__main__':
    advent = AoC()
    advent.dayOnePartOne()
    advent.dayOnePartTwo()
    advent.dayTwoPartOne()
    advent.dayTwoPartTwo()
    advent.dayThreePartOne()
    advent.dayThreePartTwo()



