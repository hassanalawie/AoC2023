class AoC():
    def __init__(self):
        self.games = open('files/games.txt', 'r').readlines()

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
    
    def get_game_number(self, current_game):
        current_game_number = current_game[4:]
        current_game_number = current_game_number.strip()
        current_game_number = int(current_game_number)
        return current_game_number

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

if __name__ == '__main__':
    advent = AoC()
    advent.dayTwoPartOne()
    advent.dayTwoPartTwo()

    



