# imports
import json
from time import sleep
from os import system
from colorama import Fore

# Open json data
fp = open('database/data.json', 'r')
data = fp.read()
fp.close()


# Search Class
class Search:

	def __init__ (self, value):
		self.value = value

	# Search Function
	def search(self):
		system('clear')
		Data = self.value.lower()
		Data_correct = Data + '_dec'
		Search_Value = None

		# All json Datas
		json_data = json.loads( data )['Colors']
		json_data2 = json.loads( data )['Machin_Learning']
		json_data3 = json.loads( data )['Telegram_bots']
		json_data4 = json.loads( data )['game_devel']
		json_data5 = json.loads( data )['file_enc']
		json_data6 = json.loads( data )['sqllib']
		json_data7 = json.loads( data )['other']
		
		# first check
		if Data_correct in json_data:
			Search_Value = 'Colors'

		elif Data_correct in json_data2:
			Search_Value = 'Machin_Learning'

		elif Data_correct in json_data3:
			Search_Value = 'Telegram_bots'

		elif Data_correct in json_data4:
			Search_Value = 'game_devel'

		elif Data_correct in json_data5:
			Search_Value = 'file_enc'
		
		elif Data_correct in json_data6:
			Search_Value = 'sqllib'
		
		elif Data_correct in json_data7:
			Search_Value = 'other'

		# check for python_telegram_bot
		if Data == 'python_telegram_bot' or Data == 'python telegram bot' or Data == 'python telegram' or Data == 'telegram bot':
			print()
			print('<---Description--->')
			print(json.loads( data )['Telegram_bots']['python_telegram_bot_dec'])
			print()
			print('<---Description--->')
			print()
			show_examplePTB = input(Fore.LIGHTMAGENTA_EX + '[?] Do you wanna see an example ? (Y/N) : ')
			print()
			if show_examplePTB.upper() == 'Y':
				print()
				print(Fore.LIGHTYELLOW_EX + '<---Example--->')
				print()
				print(json.loads( data )['Telegram_bots']['python_telegram_bot_exm'])
				print()
				print(Fore.LIGHTYELLOW_EX + '<---Example--->')
				print()

			elif show_examplePTB.upper() == 'N':
				pass

			else:
				print(Fore.LIGHTRED_EX + '[!] Wrong Value')


		# Second check
		elif Data_correct in json_data or json_data2 or json_data3 or json_data4 or json_data5 or json_data6 or json_data7:
			print()
			print('<---Description--->')
			print(json.loads( data )[Search_Value][Data+'_dec'])
			print()
			print('<---Description--->')
			print()
			show_example = input(Fore.LIGHTMAGENTA_EX + '[?] Do you wanna see an example ? (Y/N) : ')
			print()
			if show_example.upper() == 'Y':
				print()
				print(Fore.LIGHTYELLOW_EX + '<---Example--->')
				print()
				print(json.loads( data )[Search_Value][Data+'_exm'])
				print()
				print(Fore.LIGHTYELLOW_EX + '<---Example--->')
				print()

			elif show_example.upper() == 'N':
				pass

			else:
				print(Fore.LIGHTRED_EX + '[!] Wrong Value')

		else:
			print(Fore.LIGHTRED_EX + '404 -> Not Found')
