import json

def steno_to_braille(
        left_hand_buttons = "TPH", 
        right_hand_buttons = "FPL"):
    
    left_len = len (left_hand_buttons)
    right_len = len (right_hand_buttons)
    if ( left_len != 3 and right_len != 3):
        raise ValueError("There needs to be 3 buttons in each string")
    steno_string = left_hand_buttons + right_hand_buttons


    #TPHFPL to 321456 to 0b543210
    #left to right
    steno_to_bin_list = [5,4,3,0,1,2]
    #for i in steno_to_bin_list:
    #    print(steno_string[i])


    res_dict = {}
    #loop through every dot pattern and index
    for _c in range(0x2801, 0x283F + 1):
        #The last 6 digits encode our steno input
        binary_string = bin(_c)[-6:]
        #This our dictionary value
        dot_pattern = chr(_c)
        print(binary_string)
        print(dot_pattern)

        #Convert binary string to braille dot pattern to steno dictionary key
        steno_key = ""
        right_key = ""
        left_key = ""
        for i, (b, l) in enumerate(zip(binary_string, steno_to_bin_list)):
            if(i<3):
                if b=='1':
                    right_key += steno_string[l]
            if i == 3:
                right_key+='-'
            if(i>=3):
                if b=='1':
                    left_key += steno_string[l]

        #Put the answer back into steno order
        steno_key = left_key + right_key[::-1]
        #Add to dictionary
        res_dict[steno_key] = dot_pattern

    with open('BrailleSteno.json', 'w', encoding='utf-8') as f:
        print(res_dict)
        json.dump(res_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    steno_to_braille()