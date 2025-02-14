The goal:
The goal is to make a steno dictionary that translates steno to braille.
The program will allow us to pick which steno buttons we want to use,
so people who prefer bottom row or alt layouts that have top row #
can use it too.

This should be a function with these parameters:
-A string of 8 steno buttons in steno order
-An optional string of at least 1 button to act as 'space'
The program should reject any string that uses * star


There are a few resources to consider first:

Steno!
This is steno order: #STKPWHRAOEUFRPBLGTSDZ
         #
S1 T P H   F P L T D
S2 K W R * R B G S Z
    A O   E U       
S1 and S2 are joined. 
The # number bar goes across the top.
Steno order can be cleanly converted to binary,
it's a chorded system so each button is either
up or down, but JSON dictionaries are usually
written with the capital letters like
{'key':'value'} to {'STOEUPB':'steno'}
we so represent that as 0110000001110011000000
Our goal is to take 8 buttons and 
at least one space button and use those.
So STPH(AOEU)FPLT 
Space key is not used in chording,
Space inputs can be made separately or left out

Braille!
-Braille is
-https://en.wikipedia.org/wiki/Braille_Patterns
6 buttons were used before the last two were added,
so braille order looks like this:
1 o o 4
2 o o 5
3 o o 6
7 o o 8


Unicode!
U+28FF is chr(0x28FF)
Braille dot patterns start with the empty char
at U+2800 or 10240, it's right here: (⠀)
https://en.wikipedia.org/wiki/Braille_pattern_dots-0
Braille
English!