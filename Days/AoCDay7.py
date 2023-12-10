from collections import Counter
from functools import cmp_to_key
class AoC():
    def __init__(self):
        self.camel_cards = open('files/camel_cards.txt', 'r').readlines()
        self.card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    def checkFiveOfAKind(self, hand):
        hand_set = set(hand)
        return len(list(hand_set)) == 1
    def checkFourOfAKind(self,hand):
        hand_set = set(hand)
        max_amount = 0
        for item in hand_set:
            max_amount = max(max_amount, hand.count(item))
        return len(list(hand_set)) == 2 and max_amount == 4

    def transform_element(self, element):
        mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        return int(mapping.get(element, element))

    def get_second_score(self, hand):

        score = 0
        hand_list = [self.transform_element(item) for item in hand[0]]
        for i, number in enumerate(hand_list):
            score += (10**(12-2*i)) * number

        return score

    def get_second_score_2(self,hand):

        score = 0
        hand_list = self.hand_to_list_of_int(hand)
        for i, number in enumerate(hand_list):
            score += (10**(12-2*i)) * number

        return score

    def custom_compare_2(self, hand_x, hand_y):

        hand_x_XX= hand_x.replace("J", "X")
        hand_y_XX = hand_y.replace("J", "X")

        # Compare elements based on their custom order
        hand_x_score = self.get_first_score_2(hand_x_XX)
        hand_y_score = self.get_first_score_2(hand_y_XX)

        if hand_x_score == hand_y_score:
            hand_x_score = self.get_second_score_2(hand_x)
            hand_y_score = self.get_second_score_2(hand_y)

        return (hand_x_score > hand_y_score) - (hand_x_score < hand_y_score)

    def custom_compare(self, hand_x, hand_y):

        hand_x_score = self.get_relative_score(hand_x)
        hand_y_score = self.get_relative_score(hand_y)

        if hand_x_score == hand_y_score:
            hand_x_score = self.get_second_score(hand_x)
            hand_y_score = self.get_second_score(hand_y)

        return (hand_x_score > hand_y_score) - (hand_x_score < hand_y_score)

    def checkFullHouse(self, hand):
        return self.checkThreeOfAKind(hand) and self.checkTwoOfAKind(hand)

    def checkThreeOfAKind(self, hand):
        hand_set = set(hand)
        max_amount = 0
        for item in hand_set:
            max_amount = max(max_amount, hand.count(item))
        return max_amount == 3

    def checkTwoOfAKind(self, hand):
        hand_set = set(hand)
        max_amounts = []
        for item in hand_set:
            max_amounts.append(hand.count(item))
        return 2 in max_amounts
    
    def checkTwoPair(self,hand):
        hand_set = set(hand)
        max_amounts = []
        for item in hand_set:
            max_amounts.append(hand.count(item))
        return ''.join(str(x) for x in max_amounts).count("2") == 2
    
    def checkOnePair(self,hand):
        hand_set = set(hand)
        max_amounts = []
        for item in hand_set:
            max_amounts.append(hand.count(item))
        return ''.join(str(x) for x in max_amounts).count("2") == 1

    def checkHighCard(self, hand):
        hand_set = set(hand)
        return len(list(hand_set)) == 5 

    def testHelpers(self):
        assert self.checkFiveOfAKind("AAAAA")
        assert not self.checkFiveOfAKind("AA8AA")
        assert self.checkFourOfAKind("AA8AA")
        assert not self.checkFourOfAKind("23332")
        assert self.checkFullHouse("23332")
        assert not self.checkFullHouse("TTT98")
        assert self.checkThreeOfAKind("TTT98")
        assert not self.checkThreeOfAKind("23432")
        assert self.checkTwoPair("23432")
        assert not self.checkTwoPair("A23A4")
        assert self.checkOnePair("A23A4")
        assert not self.checkOnePair("23456")
        assert self.checkHighCard("23456")

    def get_relative_score(self, hand):
        if self.checkFiveOfAKind(hand):
            return 1000
        elif self.checkFourOfAKind(hand):
            return 900
        elif self.checkFullHouse(hand):
            return 800
        elif self.checkThreeOfAKind(hand):
            return 700
        elif self.checkTwoPair(hand):
            return 600
        elif self.checkOnePair(hand):
            return 500
        elif self.checkHighCard(hand):
            return 400

    def parse_camel_cards(self):
        camel_cards_no_n = []
        camel_card_tuples = []
        for cc in self.camel_cards:
            ncc = cc.replace("\n", "")
            camel_cards_no_n.append(ncc)
        for cc in camel_cards_no_n:
            cc.strip()
            hand,bid = cc.split(" ")
            camel_card_tuples.append((hand, bid))
        
        return camel_card_tuples
    def custom_sort(self, item):
        weights = {card: weight for weight, card in enumerate(self.card_strength)}
        
        for char in item[0]:
            if char in weights:
                return weights[char]
        
        return float('inf')

    def getTotalWinnings(self, gameStack):
        total = 0
        total_games = len(gameStack)
        for i, game in enumerate(gameStack):
            m = total_games - i
            total += int(game[1]) * m
        return total
    def daySevenPartOne(self):
        self.testHelpers()
        five_of_a_kinds = []
        four_of_a_kinds = []
        full_houses = []
        three_of_a_kind = []
        two_pairs = []
        one_pairs = []
        high_cards = []
        games_ranked_stack = []
        order = {key: i for i, key in enumerate(self.card_strength)}
        ccs = self. parse_camel_cards()
        for hand, bid in ccs:
            if self.checkFiveOfAKind(hand):
                five_of_a_kinds.append((hand, bid))
            elif self.checkFourOfAKind(hand):
                four_of_a_kinds.append((hand, bid))
            elif self.checkFullHouse(hand):
                full_houses.append((hand, bid))
            elif self.checkThreeOfAKind(hand):
                three_of_a_kind.append((hand, bid))
            elif self.checkTwoPair(hand):
                two_pairs.append((hand, bid))
            elif self.checkOnePair(hand):
                one_pairs.append((hand, bid))
            elif self.checkHighCard(hand):
                high_cards.append((hand, bid))
        
            
        if len(five_of_a_kinds) > 0:
            games_ranked_stack += sorted(five_of_a_kinds, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(four_of_a_kinds) > 0:
            games_ranked_stack += sorted(four_of_a_kinds, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(full_houses) > 0:
            games_ranked_stack += sorted(full_houses, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(three_of_a_kind) > 0:
            games_ranked_stack += sorted(three_of_a_kind, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(two_pairs) > 0:
            games_ranked_stack += sorted(two_pairs, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(one_pairs) > 0:
            games_ranked_stack += sorted(one_pairs, key=cmp_to_key(self.custom_compare), reverse=True)
        if len(high_cards) > 0:
            games_ranked_stack += sorted(high_cards, key=cmp_to_key(self.custom_compare), reverse=True)
            

        ans = self.getTotalWinnings(games_ranked_stack)
        print(f"Final Answer: {ans}")

    def hand_to_list_of_int(self, hand):

        hand_list = list(hand)
        transformed_list = [self.transform_element(item) for item in hand_list]

        return transformed_list

    def get_first_score_2(self, hand):

        hand_list = list(hand)
        joker_counts = hand_list.count("X")
        # print("joker_counts", joker_counts)

        if joker_counts == 0:
            return self.get_score_2(hand)

        joker_idx = [index for index, value in enumerate(hand_list) if value == "X"]

        score = 0

        for idx in joker_idx:

            for replacement_value in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]:
                hand_list[idx] = replacement_value
                hand_str = ''.join(hand_list)
                new_score = self.get_first_score_2(hand_str)
                score = max(score, new_score)

        return score

    def get_score_2(self, hand):

        hand_list = self.hand_to_list_of_int(hand)

        result = Counter(hand_list)

        counts_most_common = result.most_common(1)[0][1]

        # hand score
        is_five_of_a_kind = len(set(hand_list)) == 1

        if is_five_of_a_kind:
            # print("Five of a kind")
            # score = 1000 + hand_list[0]
            return 1000

        is_four_of_a_kind = counts_most_common == 4

        if is_four_of_a_kind:
            # print("Four of a kind")
            # score = 900 + value_most_common
            return 900

        is_full_house = len(set(hand_list)) == 2 and not is_four_of_a_kind
        if is_full_house:
            # print("Full house")
            return 800

        is_three_of_a_kind = len(set(hand_list)) == 3 and counts_most_common == 3
        if is_three_of_a_kind:
            # print("Three of a kind")
            return 700

        is_two_pair = len(set(hand_list)) == 3 and not is_three_of_a_kind
        if is_two_pair:
            # print("Two pair")
            return 600

        is_one_pair = len(set(hand_list)) == 4
        if is_one_pair:
            # print("One pair")
            return 500

        is_high_card = len(set(hand_list)) == 5
        if is_high_card:
            # print("High card")
            return 400

        return 0

    def daySevenPartTwo(self):
        hand_str_list = []
        bid_dict = {}

        for id, line in enumerate(self.camel_cards):
            # print("progress: ", id, "/", len(lines))
            hand_str = line.split()[0]

            bid = int(line.split()[1])
            hand_str_list.append(hand_str)
            bid_dict[hand_str] = bid

        print("Sorting start")
        # Sort the list based on the custom comparison function
        sorted_hands = sorted(hand_str_list, key=cmp_to_key(self.custom_compare_2))
        print("Sorting done")

        # final stuff
        sum = 0
        for i, hand in enumerate(sorted_hands):

            rank = i + 1
            bid = bid_dict[hand]
            sum += bid * rank

        print(f"Final Answer: {sum}")

    

if __name__ == '__main__':
    advent = AoC()
    advent.daySevenPartOne()
    advent.daySevenPartTwo()




