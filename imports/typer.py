import time
from colorama import Fore
import random

#colors class
class colors:
    MAGENTA = Fore.LIGHTMAGENTA_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BLUE = Fore.LIGHTBLUE_EX
    RED = Fore.LIGHTRED_EX
    CYAN = Fore.LIGHTCYAN_EX
    WHITE = Fore.LIGHTWHITE_EX


random_color = [colors.MAGENTA,colors.YELLOW,colors.RED,colors.BLUE,colors.CYAN,colors.WHITE]
random.shuffle(random_color)

class text_type:

	def __init__ (self, text):
		self.text = text

	def dprint(string):
	   for letter in string:
	        print(letter,end = '', flush=True)
	        time.sleep(.06)
	   print("")

	def printer(self):
		print = text_type.dprint
		print(random_color [0] + self.text)