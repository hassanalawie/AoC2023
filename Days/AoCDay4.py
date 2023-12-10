from queue import Queue
class AoC():
    def __init__(self):
        self.scratchcards = open('files/scratchcards.txt', 'r').readlines()


    def get_scratchcard_details(self, card):
        card_split_colon = card.split(":")
        card_game = card_split_colon[0]
        list1, list2 = card_split_colon[1].split("|")
        winning_list = list1.strip()
        my_list = list2.strip()
        winning_numbers = winning_list.split(" ")
        my_numbers_raw = my_list.split(" ")
        my_numbers = []
        for num in my_numbers_raw:
            if len(num) > 0:
                my_numbers.append(num)
        return [winning_numbers, my_numbers, card_game]
    
    def get_game_number(self, current_game):
        current_game_number = current_game[4:]
        current_game_number = current_game_number.strip()
        current_game_number = int(current_game_number)
        return current_game_number

    def dayFourPartOne(self):
        total_winnings = 0
        for i,card in enumerate(self.scratchcards):
            card = card.replace("\n","")
            winning_numbers, my_numbers, game_name = self.get_scratchcard_details(card)
            winning_numbers_set = set(winning_numbers)
            winning_count = 0
            for num in my_numbers:
                if num in winning_numbers:
                    winning_count += 1
            exponent = int(winning_count) - 1
            if winning_count == 0:
                total_winnings += 0
            elif winning_count == 1:
                total_winnings += 1
            else:
                total_winnings += (2**exponent)
        print(total_winnings)
    
    def dayFourPartTwo(self):
        q = Queue()
        card_wins = {}
        total = 0
        for i,card in enumerate(self.scratchcards):
            card = card.replace("\n","")
            winning_numbers, my_numbers, game_name = self.get_scratchcard_details(card)
            winning_numbers_set = set(winning_numbers)
            my_number_set = set(my_numbers)
            # This is cool
            winnings = winning_numbers_set & my_number_set
            card_wins[self.get_game_number(game_name)] = len(winnings)
            q.put(self.get_game_number(game_name))
        while not q.empty():
            total += 1
            k = q.get()
            for i in range(k + 1, k + card_wins[k] + 1):
                q.put(i)
        print(total)

if __name__ == '__main__':
    advent = AoC()
    advent.dayFourPartOne()
    advent.dayFourPartTwo()
    



