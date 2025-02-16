import json
import itertools as it

def steno_braille_spaces(space_buttons = "AOEU"):
    
    res_dict = {}
    for _combo_count in range(1, len(space_buttons)+1):
        for _key in it.combinations(space_buttons, _combo_count):
            res_dict[''.join(_key)] = "{^ ^}"

    with open('BrailleVowelSpaces.json', 'w', encoding='utf-8') as f:
        print(res_dict)
        json.dump(res_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    steno_braille_spaces()