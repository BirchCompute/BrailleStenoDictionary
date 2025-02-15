import json

def steno_to_braille(
        left_hand_buttons = "STPH", 
        right_hand_buttons = "FPLT",
        space_buttons = "AOEU"):
    
    left_len = len (left_hand_buttons)
    right_len = len (right_hand_buttons)

    if ( left_len < 3 or left_len > 4 or right_len < 3 or right_len > 4 ):
        raise ValueError("There needs to be 3 or 4 buttons in the string")
    
    #Make translation string
    _l = left_hand_buttons[-3:]
    _r = right_hand_buttons[2::-1]
    steno_to_bin_string = _r + _l
    #print(steno_to_bin_string)
    #print(bin(0x283F)[-6:])

    res_dict = {}

    for c in range(0x2800, 0x283F + 1):
        dot_pattern = chr(c)
        binary_string = bin(c)[-6:]

        #Convert binary string to steno key
        steno_key = ""
        for i, b, s in  enumerate(zip(binary_string, steno_to_bin_string)):
            if i
            if b=='1':
                steno_key += s
        #Add to dictionary
        res_dict[steno_key] = dot_pattern

    with open('BrailleSteno.json', 'w', encoding='utf-8') as f:
        print(res_dict)
        json.dump(res_dict, f, ensure_ascii=False, indent=4)

    has_four_left_buttons = left_len == 4
    has_four_right_buttons = right_len == 4



if __name__ == "__main__":
    steno_to_braille()