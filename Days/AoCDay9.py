import numpy as np

class AoC():
    def __init__(self):
        self.sequences = open('files/sequences.txt', 'r').readlines()

    def parse_sequences(self):
        mat = []
        for s in self.sequences:
            s = s.replace("\n","")
            s.strip()
            a = s.split(" ")
            n = []
            for c in a:
                n.append(int(c))
            mat.append(n)
        
        self.sequences = mat

    def get_final_number(self, sequence):
        if len(sequence) == 1: 
            return [0]
        arr = np.array(sequence)
        diff_arr = list(np.diff(arr))
        return sequence[-1] + self.get_final_number(diff_arr)

    def get_first_number(self, sequence):
        if len(sequence) == 1: 
            return [0]
        arr = np.array(sequence)
        diff_arr = list(np.diff(arr))
        return sequence[0] - self.get_first_number(diff_arr)

    def dayNinePartOne(self):
        self.parse_sequences()
        final_numbers = []
        for sequence in self.sequences:
            fn = self.get_final_number(sequence)
            final_numbers.append(fn[0])
        print(f"Final Answer: {sum(final_numbers)}")

    def dayNinePartTwo(self):
        self.parse_sequences()
        first_numbers = []
        for sequence in self.sequences:
            fn = self.get_first_number(sequence)
            first_numbers.append(fn[0])
        print(f"Final Answer: {sum(first_numbers)}")


if __name__ == '__main__':
    advent = AoC()
    advent.dayNinePartOne()
    advent.__init__()
    advent.dayNinePartTwo()