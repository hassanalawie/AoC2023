class AoC():
    def __init__(self):
        self.network = open('files/network.txt', 'r').readlines()
        self.instruction_map = {
            "R":1,
            "L":0
        }
        self.current_instruction = 0
        self.current_location = ""
        self.maps = {}
        self.instructions = ""
        self.step_count = 0

    def update_current_instruction(self):
        if self.current_instruction == len(self.instructions) - 1:
            self.current_instruction = 0
        else:
            self.current_instruction += 1

    def parse_file(self):
        self.instructions = self.network[0][:-1]
        maps = self.network[2:]
        first = True
        for m in maps:
            key, value = m.split(" = ")
            value = value[:-1]
            value_tuple = (value[1:4], value[6:9])
            self.maps[key] = value_tuple
            if first:
                first = False
                self.current_location = key
        
    def dayEightPartOne(self):
        self.parse_file()

        while self.current_location != "ZZZ":
            self.step_count += 1
            options_from_current_location = self.maps[self.current_location]
            direction = self.instructions[self.current_instruction]
            right_or_left = self.instruction_map[direction]
            self.current_location = options_from_current_location[right_or_left]

            self.update_current_instruction()

        print(f"Final Answer: {self.step_count}")
    def dayEightPartTwo(self):
        return 1
    
if __name__ == '__main__':
    advent = AoC()
    advent.dayEightPartOne()
    advent.dayEightPartTwo()