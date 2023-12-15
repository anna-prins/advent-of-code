import sys

with open(sys.argv[1]) as data:
    lines = data.readlines()
    hands = []

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        cards = { "A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, 
              "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0 }
        translation_map = { "A": "A", "K": "B", "Q": "C", "J": "Z", "T": "E", "9": "F", "8": "G", 
              "7": "H", "6": "I", "5": "L", "4": "M", "3": "N", "2": "O" }
        hand_list = line.rstrip().split(' ')
        translated_card = ''
        for card in hand_list[0]:
            translated_card += translation_map[card]
            cards[card] += 1

        hand = { 'cards':translated_card, 'bid':hand_list[1] }

        if cards['J'] == 5:
            five_of_a_kind.append(hand)
            continue
        elif cards['J'] == 4:
            five_of_a_kind.append(hand)
        elif cards['J'] == 3:
            five = False
            for card_type in cards:
                if card_type != 'J':
                    if cards[card_type] == 2:
                        five_of_a_kind.append(hand)
                        five = True
            if not five:
                four_of_a_kind.append(hand)
        elif cards['J'] == 2:
            found_pair = False
            five = False
            for card_type in cards:
                if card_type != 'J':
                    if cards[card_type] == 3:
                        five_of_a_kind.append(hand)
                        five = True
                        break
                    if cards[card_type] == 2:
                        four_of_a_kind.append(hand)
                        found_pair = True
            if not found_pair and not five:
                three_of_a_kind.append(hand)
        elif cards['J'] == 1:
            num_pairs = 0
            four = False
            five = False
            for card_type in cards:
                if card_type != 'J':
                    if cards[card_type] == 4:
                        five_of_a_kind.append(hand)
                        five = True
                        break
                    elif cards[card_type] == 3:
                        four_of_a_kind.append(hand)
                        four = True
                        break
                    found_pair = False
                    if cards[card_type] == 2:
                        num_pairs += 1
            if num_pairs == 2:
                full_house.append(hand)
            elif num_pairs == 1:
                three_of_a_kind.append(hand)
            elif not four and not five:
                one_pair.append(hand)
        else:
            trio = False
            num_pairs = 0
            is_sorted = False
            for card_type in cards:
                if cards[card_type] == 5:
                    five_of_a_kind.append(hand)
                    is_sorted = True
                elif cards[card_type] == 4:
                    four_of_a_kind.append(hand)
                    is_sorted = True
                elif cards[card_type] == 3:
                    trio = True
                elif cards[card_type] == 2:
                    num_pairs += 1

            if not is_sorted:
                if trio:
                    if num_pairs == 1:
                        full_house.append(hand)
                    else:
                        three_of_a_kind.append(hand)
                else:
                    if num_pairs == 2:
                        two_pair.append(hand)
                    elif num_pairs == 1:
                        one_pair.append(hand)
                    else:
                        high_card.append(hand)

    sorted_five_of_a_kind = sorted( five_of_a_kind, key=lambda x:x['cards'] )
    sorted_four_of_a_kind = sorted( four_of_a_kind, key=lambda x:x['cards'] )
    sorted_full_house = sorted( full_house, key=lambda x:x['cards'] )
    sorted_three_of_a_kind = sorted( three_of_a_kind, key=lambda x:x['cards'] )
    sorted_two_pair = sorted( two_pair, key=lambda x:x['cards'] )
    sorted_one_pair = sorted( one_pair, key=lambda x:x['cards'] )
    sorted_high_card = sorted( high_card, key=lambda x:x['cards'])

    answer = 0
    i = len(lines)

    for five in sorted_five_of_a_kind:
        answer += (int(five['bid'])*i)
        i -= 1

    for four in sorted_four_of_a_kind:
        answer += (int(four['bid'])*i)
        i -= 1

    for full in sorted_full_house:
        answer += (int(full['bid'])*i)
        i -= 1

    for three in sorted_three_of_a_kind:
        answer += (int(three['bid'])*i)
        i -= 1

    for two in sorted_two_pair:
        answer += (int(two['bid'])*i)
        i -= 1

    for one in sorted_one_pair:
        answer += (int(one['bid'])*i)
        i -= 1

    for high in sorted_high_card:
        answer += (int(high['bid'])*i)
        i -= 1

    print( "answer: " + str(answer) )