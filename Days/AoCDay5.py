import sys
from typing import Tuple, List
class AoC():
    def __init__(self):
        self.plants = open('files/plants.txt', 'r').readlines()
    
    def parse_input (self, lines: List[str]) -> Tuple[List[int], List[int]]:

        seeds = [
            int(number) for number in lines[0].strip().split(": ")[-1].split()
        ]
        mappings = []
        for line in lines[1:]:
            if not line.strip():
                mappings.append([])
            elif line[0].isdigit():
                mappings[-1].append([int(number) for number in line.strip().split()])

        return seeds, mappings

    def get_map_details(self, plant_map):
        # Given a list like  [50, 98, 2] return a map like (98, 100): -48
        # [52, 50, 48] -> (50, 98): + 2
        start = plant_map[1]
        end = plant_map[1] + plant_map[2]
        value = plant_map[0] - plant_map[1]
        return {(start, end): value}


    def get_full_ranges(self, ranges):
        full_ranges = []
        current_index = 0
        current_smallest_number = 0
        positive_infinity = float('inf')
        biggest_number = list(ranges[-1].keys())[0][1]
        while current_smallest_number < biggest_number and current_index < len(ranges):
            if current_smallest_number < list(ranges[current_index].keys())[0][0]:
                full_ranges.append(
                    {
                        (current_smallest_number, list(ranges[current_index].keys())[0][0]):0
                    })
                current_smallest_number = list(ranges[current_index].keys())[0][0]
            else:
                full_ranges.append(ranges[current_index])
                current_smallest_number = list(ranges[current_index].keys())[0][1]
                current_index += 1
        full_ranges.append(
            {
                (biggest_number, positive_infinity):0
            }
        )
        return full_ranges
    def get_all_maps(self, plant_maps):
        plant_maps.sort(key = lambda x: x[1])
        new_ranges = []
        for pm in plant_maps:
            new_ranges.append(self.get_map_details(pm))
        return self.get_full_ranges(new_ranges)
    
    def get_seeds(self, seed_line):
        return seed_line.split(":")[1][:-1].strip().split(" ")

    def get_seeds_2(self, seed_line):
        res = []
        l = seed_line.split(":")[1][:-1].strip().split(" ")
        seed_numbers = []
        for sn in l:
            seed_numbers.append(int(sn))
        it = iter(seed_numbers)
        new_numbers = [*zip(it, it)]
        for r in new_numbers:
            res += list(range(r[0], r[0]+r[1]))
        return res
    def convert_to_int(self, pm):
        n1 = []
        for i in pm:
            n = []
            for j in i:
                n.append(int(j))
            n1.append(n)
        return n1

    def generate_formatted_map(self, plant_map):
        fm = []
        f1 = []
        for m in plant_map[1:]:
            fm.append(m.strip().split(" "))

        return self.convert_to_int(fm)
    
    def get_number_from_map(self, current_number, plant_map):
        biggest_number = list(plant_map[-1].keys())[0][0]
        if current_number >= biggest_number:
            return current_number
        for i, r in enumerate(plant_map):
            lower = list(r.keys())[0][0]
            higher = list(r.keys())[0][1]
            if current_number >= lower and current_number < higher:
                return current_number + r[(lower,higher)]

    def get_location_number(self, seed, maps):
        current_number = seed
        for m in maps:
            current_number = self.get_number_from_map(current_number, m)
        
        return current_number


    def find_lowest_location_with_ranges(self, seeds: List[int], mappings: List[int]) -> int:
        seed_ranges = [
            (start, start + length) for start, length in zip(seeds[0::2], seeds[1::2])
        ]
        candidates = [[] for _ in range(len(mappings))]

        for range_start, range_end in seed_ranges:
            ranges = [(range_start, range_end)]

            for i, mapping in enumerate(mappings):
                while ranges:
                    range_start, range_end = ranges.pop()

                    for destination_start, source_start, range_length in mapping:
                        source_end = source_start + range_length
                        offset = destination_start - source_start

                        if source_end <= range_start or range_end <= source_start:
                            continue

                        if range_start < source_start:
                            ranges.append((range_start, source_start))
                            range_start = source_start

                        if source_end < range_end:
                            ranges.append((source_end, range_end))
                            range_end = source_end
                        
                        range_start += offset
                        range_end += offset

                        break
                    
                    candidates[i].append((range_start, range_end))

                ranges = candidates[i]

        return min(candidates[-1])[0]

    def dayFivePartOne(self):
        string_seed_numbers = self.get_seeds(self.plants[0])
        seed_numbers = []
        for sn in string_seed_numbers:
            seed_numbers.append(int(sn))
        cutoff = 0
        new_arr = []
        for i, line in enumerate(self.plants):
            if line == '\n':
                new_arr.append(self.plants[cutoff+1: i])
                cutoff = i
        new_arr.append(self.plants[cutoff+1:len(self.plants)])
        formatted_maps = []
        for plant_map in new_arr[1:]:
            formatted_maps.append(self.generate_formatted_map(plant_map))
        nrs = []
        for m in formatted_maps:
            nr = self.get_all_maps(m)
            nrs.append(nr)
        locations = []
        for seed in seed_numbers:
            location_number = self.get_location_number(seed, nrs)
            locations.append(location_number)
        print(min(locations))

    def dayFivePartTwo(self):
        with open("files/plants.txt", encoding="utf-8") as f:
            input_lines = [line.strip() for line in f.readlines()]
            seeds, mappings = self.parse_input(input_lines)
            print("Part 2: Lowest location with seed ranges is ", self.find_lowest_location_with_ranges(seeds, mappings))
if __name__ == '__main__':
    advent = AoC()
    advent.dayFivePartOne()
    advent.dayFivePartTwo()
    



