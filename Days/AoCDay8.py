class AoC():
    def __init__(self):
        self.network = open('files/network.txt', 'r').readlines()
        self.instruction_map = {
            "R":1,
            "L":0
        }
        self.current_location = "AAA"
        self.maps = {}
        self.instructions = ""
        self.step_count = 0

    def get_start_nodes(self):
        sn = []
        for key in self.maps.keys():
            if key[-1] == "A":
                sn.append((key, self.maps[key]))
        return sn

    def get_current_instruction(self):
        return(self.step_count - 1) % len(self.instructions)

    def parse_file(self):
        self.instructions = self.network[0][:-1]
        maps = self.network[2:]
        first = True
        for m in maps:
            key, value = m.split(" = ")
            value = value[:-1]
            value_tuple = (value[1:4], value[6:9])
            self.maps[key] = value_tuple
    def __gcd(self, a, b):
        if (a == 0):
            return b
        return self.__gcd(b % a, a)
    def LcmOfArray(self, arr, idx):
        # lcm(a,b) = (a*b/gcd(a,b))
        if (idx == len(arr)-1):
            return arr[idx]
        a = arr[idx]
        b = self.LcmOfArray(arr, idx+1)
        return int(a*b/self.__gcd(a,b))

    def dayEightPartOne(self):
        self.parse_file()

        while self.current_location != "ZZZ":
            self.step_count += 1
            options_from_current_location = self.maps[self.current_location]
            direction = self.instructions[self.get_current_instruction()]
            right_or_left = self.instruction_map[direction]
            self.current_location = options_from_current_location[right_or_left]

        print(f"Final Answer: {self.step_count}")

    def dayEightPartTwo(self):
        self.parse_file()
        start_nodes = self.get_start_nodes()
        print("hi")
        steps = []
        for node in start_nodes:
            self.current_location = node[0]
            while self.current_location[-1] != "Z":
                self.step_count += 1
                options_from_current_location = self.maps[self.current_location]
                direction = self.instructions[self.get_current_instruction()]
                right_or_left = self.instruction_map[direction]
                self.current_location = options_from_current_location[right_or_left]
            steps.append(self.step_count)
            self.__init__()
            self.parse_file()
        print(f"Final Answer: {self.LcmOfArray(steps,0)}")

    
if __name__ == '__main__':
    advent = AoC()
    # advent.dayEightPartOne()
    advent.dayEightPartTwo()