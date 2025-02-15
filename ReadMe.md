# The goal:
The goal is to make a steno dictionary that translates steno to braille. The program will allow us to pick which steno buttons we want to use, so people who prefer bottom row or alt layouts that have # as S1 can use it too.

This should be a function with these parameters:

`-Two strings, left and right hand, each having 3 or 4 steno buttons`

`-An optional string of at least 1 button to act as 'space'`

The function should return a dictionary with steno input keys and braille character values. There should be an option to use ASCII for 6 dots (⠿), but unicode goes all the way up to 8 dots (⣿). 

The function should work for 3 or 4 buttons on each side, making as many definitions as the provided layout can handling. The function should reject any string that uses * star key.

# There are a few resources to consider first:

### ~Steno
This is steno order: `#STKPWHRAOEUFRPBLGTSDZ`

This is what the layout looks like:
```
         #          
S1- T- P- H     F -P L -T D
S2- K  W  R- * -R  B G -S Z
       A  O     E  U       
```
S1 and S2 are typically joined into one key.

Sometimes # is put in place of S1.


The # number bar goes across the top.


Steno order can be cleanly converted to binary, it's a chorded system so each button is either part of a chord or not, but JSON dictionaries are usually written with the capital letters used like
`{'key':'value'}` to `{'STOEUPB':'steno'}`.
We so represent that as `0110000001110011000000`
Our goal is to take 8 buttons and at least one space button and use those. `STPH(AOEU)FPLT`

Space key is not used in chording. Space inputs can be made separately or left out.

### ~Braille
https://en.wikipedia.org/wiki/Braille_Patterns

6 buttons were used before the last 2 were added for a total of 8, so braille order looks like this:
```
1 o o 4
2 o o 5
3 o o 6
7 o o 8
```
Braille writers have buttons in this layout: `7321 4568`

### ~Unicode and ASCII
U+2800 = chr(0x2800) = 10240

Braille dot patterns start with the empty char at U+2800 or 10240, it's right here: (⠀)
https://en.wikipedia.org/wiki/Braille_pattern_dots-0

Unicode includes a means for encoding eight-dot braille; however, Braille ASCII continues to be the preferred format for encoding six-dot braille. 

### ~English!

ord('A') = 65 = 0x41 = U+41

The function should also be used to output English letters.[2]

Capital `A` starts at U+41.


https://en.wikipedia.org/wiki/Braille

https://en.wikipedia.org/wiki/Braille_ASCII

https://en.wikipedia.org/wiki/Braille_Patterns

# Strategy

###  ~Steno to binary

Here are the top steno row and the braille order together.
```
S T P H * F P L T
7 3 2 1 * 4 5 6 8
```
Some swizzling might need to happen. We need this.

``` 
H  P- T- F -P  L  S- -T
1  2  3  4  5  6  7   8
```
but this backwards! We want biggest bit first!
``` 
-T  S- L -P  F  T- P- H
 1  2  3  4  5  6  7  8
```
As we can see with the disambiguating hyphens, there are some buttons on the left and the right hand side. We're going to want to take our inputs as two strings, left and right hand.

###  ~Binary to Braille dot patterns

After we have a binary number, we can convert that to hex and add that to our unicode starting point which is 0x2800.
```
char(0x2800 + 0b00101010) = braille dot pattern character
``` 

### ~Binary to English letters

Wikipedia provides this awesome string. This is a translation of the English braille alphabet to the braille binary order.
```
⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿
 A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)=
 ```
 This means once we have our braille binary value, it's only a matter of looking up our English letter output.