# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    sos.py                                             :+:    :+:             #
#                                                      +:+                     #
#    By: pde-bakk <pde-bakk@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2020/08/30 20:57:46 by pde-bakk      #+#    #+#                  #
#    Updated: 2020/08/30 21:25:54 by pde-bakk      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

morsedict = {
	'a':'.-', 
	'b':'-...', 
	'c':'-.-.', 
	'd':'-..', 
	'e':'.',
	'f':'..-.', 
	'g':'--.', 
	'h':'....', 
	'i':'..', 
	'j':'.---',
	'k':'-.-', 
	'l':'.-..', 
	'm':'--', 
	'n':'-.', 
	'o':'---',
	'p':'.--.', 
	'q':'--.-', 
	'r':'.-.', 
	's':'...', 
	't':'-',
	'u':'..-', 
	'v':'...-', 
	'w':'.--', 
	'x':'-..-', 
	'y':'-.--',
	'z':'--..', 
	'0':'-----', 
	'1':'.----',
	'2':'..---',
	'3':'...--',
	'4':'....-',
	'5':'.....',
	'6':'-....',
	'7':'--...',
	'8':'---..',
	'9':'----.',
	' ':'.-...',
	'ä':'.-.-', 
	'á':'.--.-', 
	'å': '.--.-', 
	'Ch': '----',
	'é':'..-..', 
	'ñ':'--.--', 
	'ö':'---.', 
	'ü':'..--',
	'&':'.-...', 
	'\'':'.----.',
	'@':'.--.-.', 
	')':'-.--.-', 
	'(':'-.--.', 
	':':'---...', 
	',':'--..--', 
	'=':'-...-', 
	'!':'-.-.--', 
	'.':'.-.-.-', 
	'-':'-....-', 
	'+':'.-.-.', 
	'\"':'.-..-.', 
	'?':'..--..', 
	'/':'-..-.', 
	'\n':'.-.-', 
	'\0':'peer'
}

if len(sys.argv) == 1:
	exit()

input = sys.argv[1:]
for i in input:
	for c in i.lower():
		print(morsedict[c],end=' ')
print()