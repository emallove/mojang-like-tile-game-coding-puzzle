tiles1 = "11133555"
tiles2 = "111333555"
tiles3 = "00000111"
tiles4 = "13233121"
tiles5 = "11223344555"
tiles6 = "99999999"
tiles7 = "999999999"
tiles8 = "9"
tiles9 = "99"
tiles10 = "000022"
tiles11 = "888889"
tiles12 = "889"
tiles13 = "88888844"
tiles14 = "77777777777777"
tiles15 = "1111111"
tiles16 = "1111122222"

def is_hand(s):

    num_triples = 0
    has_pair = False
    num_pairs = 0    
    too_many_pairs = False
    straggler = False # % 1 == 0

    # > 1 pairs
    # < 1 triple
    # combination of above 2

    ret = False
    for i in range(10):
        c = s.count(str(i))
        if (c % 3) == 0:
            num_triples += int(c / 3)
        elif c == 2:
            num_pairs += 1
        elif (c - 2) % 3 == 0:
            num_pairs += 1
            num_triples += ((c - 2) / 3)
        elif c > 2 and (c % 2) == 0:
            num_pairs += int(c / 2)
        elif (c % 2) == 1 or ((c - 2) % 2 == 1):
            straggler = True
            break
        elif (c % 2) == 0:
            has_pair = True

    if num_triples > -1 and num_pairs == 1 and not straggler:
        ret = True

    return ret
    
assert(is_hand(tiles1) == True)
assert(is_hand(tiles2) == False)
assert(is_hand(tiles3) == True)
assert(is_hand(tiles4) == True)
assert(is_hand(tiles5) == False)
assert(is_hand(tiles6) == True)
assert(is_hand(tiles7) == False)
assert(is_hand(tiles8) == False)
assert(is_hand(tiles9) == True)
assert(is_hand(tiles10) == False)
assert(is_hand(tiles11) == False)
assert(is_hand(tiles12) == False)
assert(is_hand(tiles13) == True)
assert(is_hand(tiles14) == True)
assert(is_hand(tiles15) == False)
assert(is_hand(tiles16) == False)
