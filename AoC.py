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
    
    def getTotalFromCalibration(self, file_info):
        total_sum = 0
        for item in file_info:
            value = (''.join(char for char in item if char.isnumeric()))
            total_sum += int(value[0]+value[-1])
        return total_sum

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

if __name__ == '__main__':
    advent = AoC()
    advent.dayOnePartOne()
    advent.dayOnePartTwo()
    