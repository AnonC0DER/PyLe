# <------CoDed By AnonCODER------>
# <------First Version : v2.0----->
# <------Help me improve it :)------>

#imports
from os import system
from colorama import Fore
from time import sleep
import random
import urllib.request
import json

# Trying to make Shortcode
fp = open('database/data.json', 'r')
data = fp.read()
fp.close()


#again
def again_1():
    again_v = input(Fore.GREEN+'For Menu type (M) for Exit type (E) : ')
    if again_v.upper() == 'M' or again_v.upper() == 'Menu' or again_v.lower() == 'm' or again_v.lower() == 'menu':
        start()
    elif again_v.upper() == 'E' or again_v.upper() == 'Exit' or again_v.lower() == 'e' or again_v.lower() == 'exit':
        print(Fore.YELLOW+'[-] Good Luck !')
    else:
        print(Fore.RED+'Wrong Value !')
        again_1()

#colors class
class colors:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


random_color = [colors.HEADER,colors.IMPORTANT,colors.NOTICE,colors.OKBLUE,colors.OKGREEN,colors.WARNING,colors.RED,colors.END,colors.LOGGING]
random.shuffle(random_color)



#Colors Libraries
def c_lib():
    print (random_color [0] + '''   
 ▄████▄   ▒█████   ██▓     ▒█████   ██▀███    ██████ 
▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▒██░    ▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒██   ██░▒██▀▀█▄    ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░░██████▒░ ████▓▒░░██▓ ▒██▒▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░
░        ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒    ░░   ░ ░  ░  ░  
░ ░          ░ ░      ░  ░    ░ ░     ░           ░  
░                                                    
''')                             

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Python Text Coloring Libraries group.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.BLUE +'''
{-------------}
[1] => Colored
[2] => Colorma
[3] => Termcolor

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    colors_lib = int(input(Fore.YELLOW +'PyLe ~$ '))

    if colors_lib == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/colored/')
        print('')
        colord = input(Fore.YELLOW +'PyLe ~$ ')

        if colord.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install colored --upgrade')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif colord.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Colors']['colored_dec'])
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif colord.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + json.loads( data )['Colors']['colored_exm'])          
           print(Fore.YELLOW + '<---Example--->')
           print('')
           again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif colors_lib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/colorama/')
        print('')
        colorma = input(Fore.YELLOW +'PyLe ~$ ')

        if colorma.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install colorama')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif colorma.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Colors']['colorama_dec']) 
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif colorma.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + json.loads( data )['Colors']['colorama_exm']) 
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print('')
           again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif colors_lib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/termcolor/')
        print('')
        termcolor = input(Fore.YELLOW +'PyLe ~$ ')
        if termcolor.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install termcolor')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif termcolor.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Colors']['termcolor_dec'])  
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif termcolor.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + json.loads( data )['Colors']['termcolor_exm'])
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print('')
           again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif colors_lib == 1000:
        system('clear')
        contact()
        again_1()

    elif colors_lib == 100:
        system('clear')
        update()

    elif colors_lib == 99:
        system('clear')
        start()

    elif colors_lib == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED+'[!]──# Wrong Value')
        again_1()


#Machine Learning
def machine_learning():
    print (random_color [0] + '''   
   __     __)                              _                           
  (, /|  /|         /)   ,             ___/__)                ,        
    / | / |  _   _ (/     __    _     (, /    _  _   __ __     __   _  
 ) /  |/  |_(_(_(__/ )__(_/ (__(/_      /   _(/_(_(_/ (_/ (__(_/ (_(_/_
(_/   '                                (_____                     .-/  
                                              )                  (_/                                        
''')                             

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Python Machine Learning Libraries.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.BLUE +'''
{-------------}
[1] => Scikit-learn
[2] => Keras 
[3] => Xgboost
[4] => Statsmodels
[5] => Tensorflow   

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    machine_lib = int(input(Fore.YELLOW +'PyLe ~$ '))

    if machine_lib == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/scikit-learn/')
        print('')
        scikit = input(Fore.YELLOW +'PyLe ~$ ')
        if scikit.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install scikit-learn')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif scikit.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['scikit_dec']) 
            print('')
            print (Fore.RED + json.loads( data )['Machin_Learning']['scikit_req']) 
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif machine_lib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/keras/')
        print('')
        keras = input(Fore.YELLOW +'PyLe ~$ ')

        if keras.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install keras')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif keras.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['keras_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif keras.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://keras.io/examples/')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['keras_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    
    elif machine_lib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.GREEN + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html')
        print('')
        xgboost = input(Fore.YELLOW +'PyLe ~$ ')
        if xgboost.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install xgboost')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif xgboost.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['xgboost_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif xgboost.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['xgboost_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif machine_lib == 4:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/statsmodels/')
        print('')
        statsmodels = input(Fore.YELLOW +'PyLe ~$ ')
        if statsmodels.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install statsmodels')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif statsmodels.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['statsmodels_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif statsmodels.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.statsmodels.org/stable/' + Fore.GREEN + ' &  https://datatofish.com/statsmodels-linear-regression/')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['statsmodels_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif machine_lib == 5:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.tensorflow.org/tutorials')
        print('')
        tensorflow = input(Fore.YELLOW +'PyLe ~$ ')
        if tensorflow.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install tensorflow')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif tensorflow.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['tensorflow_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif tensorflow.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://rubikscode.net/2018/02/05/introduction-to-tensorflow-with-python-example/')
            print (Fore.WHITE + json.loads( data )['Machin_Learning']['tensorflow_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif machine_lib == 1000:
        system('clear')
        contact()
        again_1()

    elif machine_lib == 100:
        system('clear')
        update()

    elif machine_lib == 99:
        system('clear')
        start()

    elif machine_lib == 0:
        print('[-]──# Se You Later :)')

    else:
        print(Fore.RED+'[!]──# Wrong Value')
        again_1()



#Telegram Robots
def telegram_bots():
  print(random_color [0] + '''  
 _____    _                                 ______       _       
|_   _|  | |                                | ___ \     | |      
  | | ___| | ___  __ _ _ __ __ _ _ __ ___   | |_/ / ___ | |_ ___ 
  | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \  | ___ \/ _ \| __/ __|
  | |  __/ |  __/ (_| | | | (_| | | | | | | | |_/ / (_) | |_\__\\
  \_/\___|_|\___|\__, |_|  \__,_|_| |_| |_| \____/ \___/ \__|___/
                  __/ |                                          
                 |___/                                           
''')

  print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the section on building robots with Python.')
  print (Fore.YELLOW + '[#]' + Fore.MAGENTA + ' In this section you can find libraries that help you build a telegram robot')
  print (Fore.YELLOW + '[#]' + Fore.MAGENTA + ' Choose Your Library...')
  
  print (Fore.BLUE +'''
{-------------}
[1] => Python-telegram-bot
[2] => Pyrogram
[3] => Telegram

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

  robots_lib = int(input(Fore.YELLOW +'PyLe ~$ '))
  if robots_lib == 1:
    print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Examples 'E.'")
    print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/python-telegram-bot/')
    print('')
    python_telegram_bot = input(Fore.YELLOW +'PyLe ~$ ')
    if python_telegram_bot.upper() == 'I':
      print ('')
      print(Fore.YELLOW + '<---Installation--->')
      print (Fore.WHITE + 'pip install python-telegram-bot')
      print(Fore.YELLOW + '<---Installation--->') 
      print('')
      again_1()

    elif python_telegram_bot.upper() == 'D':
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print (Fore.WHITE + json.loads( data )['Telegram_bots']['python_telegram_bot_dec'])
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()

    elif python_telegram_bot.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.CYAN + 'More Details : https://python-telegram-bot.readthedocs.io/en/stable/')
      print (Fore.WHITE + json.loads( data )['Telegram_bots']['python_telegram_bot_exm'])
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print('')
      again_1()
      
    else:
      print(Fore.RED + '[!] Wrong Value')
      again_1()


  elif robots_lib == 2:
    print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
    print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/Pyrogram/')
    print('')
    pyrogram = input(Fore.YELLOW +'PyLe ~$ ')
    if pyrogram.upper() == 'I':
      print ('')
      print(Fore.YELLOW + '<---Installation--->')
      print (Fore.WHITE + 'pip install Pyrogram')
      print(Fore.YELLOW + '<---Installation--->') 
      print('')
      again_1()
          
    elif pyrogram.upper() == 'D':
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print(Fore.WHITE + json.loads( data )['Telegram_bots']['pyrogram_dec'])
      print(Fore.RED + json.loads( data )['Telegram_bots']['pyrogram_req'])
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()
      
    elif pyrogram.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.CYAN + 'More Details : https://docs.pyrogram.org/start/examples/')
      print(Fore.WHITE + json.loads( data )['Telegram_bots']['pyrogram_exm'])
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print('')
      again_1()

    else:
      print(Fore.RED + '[!] Wrong Value')
      again_1()


  elif robots_lib == 3:
    print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
    print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/telegram.py/')
    print('')
    pyrogram = input(Fore.YELLOW +'PyLe ~$ ')
    if pyrogram.upper() == 'I':
      print ('')
      print(Fore.YELLOW + '<---Installation--->')
      print (Fore.WHITE + 'pip install telegram.py')
      print(Fore.YELLOW + '<---Installation--->') 
      print('')
      again_1()
          
    elif pyrogram.upper() == 'D':
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print(Fore.WHITE + json.loads( data )['Telegram_bots']['telegram_dec'])
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()
      
    elif pyrogram.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.WHITE + json.loads( data )['Telegram_bots']['telegram_exm'])
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print('')
      again_1()

    else:
      print(Fore.RED + '[!] Wrong Value')
      again_1()

  elif robots_lib == 1000:
    system('clear')
    contact()
    again_1()

  elif robots_lib == 100:
    system('clear')
    update()

  elif robots_lib == 99:
    system('clear')
    start()

  elif robots_lib == 0:
    print(Fore.YELLOW+'[-]──# Se You Later :)')

  else:
    print(Fore.RED + '[!] Wrong Value')
    again_1()
  
  
  #Game Development
def game_dev():
    print(random_color [0] + '''
   ____      _      __  __  U _____ u      ____  U _____ u__     __   
U /"___|uU  /"\  uU|' \/ '|u\| ___"|/     |  _"\ \| ___"|/\ \   /"/u  
\| |  _ / \/ _ \/ \| |\/| |/ |  _|"      /| | | | |  _|"   \ \ / //   
 | |_| |  / ___ \  | |  | |  | |___      U| |_| |\| |___   /\ V /_,-. 
  \____| /_/   \_\ |_|  |_|  |_____|      |____/ u|_____| U  \_/-(_/  
  _)(|_   \\    >><<,-,,-.   <<   >>       |||_   <<   >>   //        
 (__)__) (__)  (__)(./  \.) (__) (__)     (__)_) (__) (__) (__)    
''')

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Python game development section.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.BLUE +'''
{-------------}
[1] => Pygame
[2] => Turtles
[3] => PyOpenGL

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    g_dev = int(input(Fore.YELLOW +'PyLe ~$ '))
    if g_dev == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.pygame.org/docs/')
        print('')
        pygame = input(Fore.YELLOW +'PyLe ~$ ')
        if pygame.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install pygame')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()
        
        elif pygame.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['game_devel']['pygame_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pygame.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.pygame.org/docs/ref/examples.html')
            print(Fore.WHITE + json.loads( data )['game_devel']['pygame_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    
    elif g_dev == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Examples 'E.'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/turtle.html')
        print('')
        turtles = input(Fore.YELLOW +'PyLe ~$ ')
        if turtles.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install turtles')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif turtles.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['game_devel']['turtles_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif turtles.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://michael0x2a.com/blog/turtle-examples')
            print(Fore.WHITE + json.loads( data )['game_devel']['PyOpenGL_dec'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()
      
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif g_dev == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Examples 'E.'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' http://pyopengl.sourceforge.net/documentation/index.html')
        print('')
        pyopengl = input(Fore.YELLOW +'PyLe ~$ ')
        if pyopengl.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install PyOpenGL')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif pyopengl.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['game_devel']['PyOpenGL_dec']) 
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pyopengl.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://noobtuts.com/python/opengl-introduction')
            print(Fore.WHITE + json.loads( data )['game_devel']['PyOpenGL_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()
      
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif g_dev == 1000:
        system('clear')
        contact()
        again_1()

    elif g_dev == 100:
        system('clear')
        update()

    elif g_dev == 99:
        system('clear')
        start()

    elif g_dev == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()
    

#File & Text Encryption
def ft_enc():
    print(random_color [0] + '''
███████ ██ ██      ███████  ████████ ███████ ██   ██ ████████     ███████ ███    ██  ██████ 
██      ██ ██      ██          ██    ██       ██ ██     ██        ██      ████   ██ ██      
█████   ██ ██      █████ █████ ██    █████     ███      ██        █████   ██ ██  ██ ██      
██      ██ ██      ██          ██    ██       ██ ██     ██        ██      ██  ██ ██ ██      
██      ██ ███████ ███████     ██    ███████ ██   ██    ██        ███████ ██   ████  ██████                                                                                                                                                                   
''')

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Encryption section in Python.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.BLUE +'''
{-------------}
[1] => Cryptography
[2] => Pycrypto 
[3] => pyAesCrypt

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    ft_en = int(input(Fore.YELLOW +'PyLe ~$ '))
    if ft_en == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://cryptography.io/en/latest/')
        print('')
        cryptography = input(Fore.YELLOW +'PyLe ~$ ')
        if cryptography.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install cryptography')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()
            
        elif cryptography.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['file_enc']['cryptography_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif cryptography.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://cryptography.io/en/latest/')
            print(Fore.WHITE + json.loads( data )['file_enc']['cryptography_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif ft_en == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/pycrypto/')
        print('')
        pycrypto = input(Fore.YELLOW +'PyLe ~$ ')
        if pycrypto.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install pycrypto')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif pycrypto.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['file_enc']['pycrypto_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pycrypto.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.dlitz.net/software/pycrypto/')
            print(Fore.WHITE + json.loads( data )['file_enc']['pycrypto_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif ft_en == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.aescrypt.com/pyaescrypt.html')
        print('')
        pyaescrypt = input(Fore.YELLOW +'PyLe ~$ ')
        if pyaescrypt.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install pyAesCrypt')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif pyaescrypt.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['file_enc']['pyAesCrypt_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pyaescrypt.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://pypi.org/project/pyAesCrypt/')
            print(Fore.WHITE + json.loads( data )['file_enc']['pyAesCrypt_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif ft_en == 1000:
        system('clear')
        contact()
        again_1()

    elif ft_en == 100:
        system('clear')
        update()

    elif ft_en == 99:
        system('clear')
        start()

    elif ft_en == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


#Sql Libraries
def sql_lib():
    print(random_color [0] + '''
 .d8888b.   .d88888b.  888           888      d8b 888      
d88P  Y88b d88P" "Y88b 888           888      Y8P 888      
Y88b.      888     888 888           888          888      
 "Y888b.   888     888 888           888      888 88888b.  
    "Y88b. 888     888 888           888      888 888 "88b 
      "888 888 Y8b 888 888           888      888 888  888 
Y88b  d88P Y88b.Y8b88P 888           888      888 888 d88P 
 "Y8888P"   "Y888888"  88888888      88888888 888 88888P"  
                  Y8b                                                                                                                                                                                                        
''')

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Python SQL libraries.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.BLUE +'''
{-------------}
[1] => SQLite
[2] => MySQL 
[3] => PostgreSQL

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    sql_plib = int(input(Fore.YELLOW +'PyLe ~$ '))
    if sql_plib == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/sqlite3.html#module-sqlite3')
        print('')
        SQLite = input(Fore.YELLOW +'PyLe ~$ ')
        if SQLite.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install pysqlite3')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif SQLite.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['sqllib']['SQLite_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif SQLite.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.tutorialspoint.com/sqlite/sqlite_python.htm')
            print(Fore.WHITE + json.loads( data )['sqllib']['SQLite_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif sql_plib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html')
        print('')
        MySQL = input(Fore.YELLOW +'PyLe ~$ ')
        if MySQL.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install mysql-connector-python')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif MySQL.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['sqllib']['mysql_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif MySQL.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.w3schools.com/python/python_mysql_select.asp')
            print(Fore.WHITE + json.loads( data )['sqllib']['mysql_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif sql_plib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.tutorialspoint.com/postgresql/postgresql_python.htm')
        print('')
        postgres = input(Fore.YELLOW +'PyLe ~$ ')
        if postgres.upper() == 'I':
            print ('')
            print(Fore.YELLOW + '<---Installation--->')
            print (Fore.WHITE + 'pip install postgres')
            print(Fore.YELLOW + '<---Installation--->') 
            print('')
            again_1()

        elif postgres.upper() == 'D':
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print(Fore.WHITE + json.loads( data )['sqllib']['postgres_dec'])
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif postgres.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://stackabuse.com/working-with-postgresql-in-python/')
            print(Fore.WHITE + json.loads( data )['sqllib']['postgres_exm'])
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print('')
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif sql_plib == 1000:
        system('clear')
        contact()
        again_1()

    elif sql_plib == 100:
        system('clear')
        update()

    elif sql_plib == 99:
        system('clear')
        start()

    elif sql_plib == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


# For beginners
def For_beginners():
    print(random_color [0] + '''    
   .-._.---'           .-.                                                      
  (_) /               (_) )-.                   .-.                             
     /--..-._.).--.      / __)    .-.  .-.      `-'.  .-..  .-.   .-.  ).--..   
    /   (   )/          /    `. ./.-'_(   )    /    )/   ))/   )./.-'_/    / \  
 .-/     `-'/          /'      )(__.'  `-/-'_.(__. '/   ('/   ( (__.'/    / ._) 
(_/                 (_/  `----'      -._/                `-    `-        /         
''')

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Beginners Menue.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' In this section you can find books and movies suitable for starting Python.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ ' What do you want?')
    print (Fore.BLUE +'''
<<<<<<<<--->>>>>>>>
[1] => BooKs

#####
More Option Coming !
#####

[1000] ~> About Author && Contact Author
[100] ~> Update
[99] ~> Main Menu
[0] ~> Exit
<<<<<<<<--->>>>>>>>''')

    for_beginners = int(input(Fore.YELLOW +'PyLe ~$ '))
    if for_beginners == 1:
        system('clear')
        print (Fore.YELLOW + '[#]' + Fore.LIGHTMAGENTA_EX+ ' Here it is, Now you can choose your books :)')
        print (Fore.LIGHTBLUE_EX +'''
////////////////////////////////////////////////////////////////////
| <1> => Learn Python in One Day                                   |
| <2> => Python Programming for Beginners                          |
| <3> => PYTHON : PYTHON'S COMPANION                               |
| <4> => Black hat Python                                          |
| <5> => Mastering Machine Learning with Python in Six Steps       |
| <6> => Automate the boring stuff with python                     |
|                                                                  |
| [99] ~> Main Menu                                                |
| [0] ~> Exit                                                      |
////////////////////////////////////////////////////////////////////''')

        books = int(input(Fore.YELLOW +'PyLe ~$ '))
        if books == 1:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Learn Python in One Day.')
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            Learn_Python = 'https://pyle-pythonlearning.ir/downloads/Learn%20Python%20in%20One%20Day.pdf'
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (545.90 KB)')
            def PythoninOne():
                try:
                    urllib.request.urlretrieve(Learn_Python, 'Learn Python in One Day (PyLe).pdf')
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + 'Trying...')
                    sleep(3.0)
                    PythoninOne()
            PythoninOne()

        elif books == 2:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Python Programming for Beginners.')
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            Python_Programming = 'https://pyle-pythonlearning.ir/downloads/Python%20Programming%20for%20Beginners.pdf'
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (9.89 MB)')
            def Python_Programming():
                try:
                    urllib.request.urlretrieve(Python_Programming, 'Python Programming for Beginners (PyLe).pdf')
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                    sleep(3.0)
                    Python_Programming()
            Python_Programming()
        
        elif books == 3:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + " You Choose PYTHON : PYTHON'S COMPANION.")
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            PYTHON = "https://pyle-pythonlearning.ir/downloads/PYTHON'S%20COMPANION.pdf"
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (10.78 MB)')
            def PYTHONSCOMPANION():
                try:
                    urllib.request.urlretrieve(PYTHON, "PYTHONS COMPANION (PyLe).pdf")
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                    sleep(3.0)
                    PYTHONSCOMPANION()
            PYTHONSCOMPANION()
            

        elif books == 4:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Black hat Python.')
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            Black_hat = "https://pyle-pythonlearning.ir/downloads/Black%20hat%20Python.pdf"
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (10.03 MB)')
            def Blackhat():
                try:
                    urllib.request.urlretrieve(Black_hat, "Black hat Python (PyLe).pdf")
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                    sleep(3.0)
                    Blackhat()
            Blackhat()
            

        elif books == 5:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Mastering Machine Learning with Python in Six Steps.')
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            MasteringMachine = "https://pyle-pythonlearning.ir/downloads/Mastering%20Machine%20Learning%20with%20Python%20in%20Six%20Steps.pdf"
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (9.60 MB)')
            def MasteringMachine():
                try:
                    urllib.request.urlretrieve(MasteringMachine, "Mastering Machine Learning with Python in Six Steps (PyLe).pdf")
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                    sleep(3.0)
                    MasteringMachine()
            MasteringMachine()
            
        
        elif books == 6:
            print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Automate the boring stuff with python.')
            print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
            Automate_the_boring = "https://pyle-pythonlearning.ir/downloads/automate%20the%20boring%20stuff%20with%20python.pdf"
            print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (10.7 MB)')
            def Automate():
                try:
                    urllib.request.urlretrieve(Automate_the_boring, "Automate the boring stuff with python (PyLe).pdf")
                    print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    For_beginners()

                except:
                    print(Fore.LIGHTRED_EX + 'No Internet !')
                    print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                    sleep(3.0)
                    Automate()
            Automate()
            
        elif books == 99:
            system('clear')
            start()

        elif books == 0:
            print(Fore.YELLOW+'[-]──# Se You Later :)')

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif for_beginners == 1000:
        system('clear')
        contact()
        again_1()

    elif for_beginners == 100:
        system('clear')
        update()

    elif for_beginners == 99:
        system('clear')
        start()

    elif for_beginners == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()       


# What is python ?
def wip():
    print(random_color [0] + '''
 __          ___     _       _____       _   _                ___  
 \ \        / / |   ( )     |  __ \     | | | |              |__ \ 
  \ \  /\  / /| |__ |/ ___  | |__) |   _| |_| |__   ___  _ __   ) |
   \ \/  \/ / | '_ \  / __| |  ___/ | | | __| '_ \ / _ \| '_ \ / / 
    \  /\  /  | | | | \__ \ | |   | |_| | |_| | | | (_) | | | |_|  
     \/  \/   |_| |_| |___/ |_|    \__, |\__|_| |_|\___/|_| |_(_)  
                                    __/ |                          
                                   |___/ 
    ''')
    print (Fore.YELLOW + '[#]' + Fore.LIGHTCYAN_EX+ ' Python is a programming language that lets you work quickly')
    print (Fore.LIGHTCYAN_EX+ 'and integrate systems more effectively')
    print (Fore.LIGHTMAGENTA_EX + '[#]' + Fore.LIGHTCYAN_EX+ ' More Information ?')
    print (Fore.RED + '[#]' + Fore.LIGHTCYAN_EX+ " Well, Choose what do you want to know frind...")
    print (Fore.LIGHTCYAN_EX+'''
...................................................
.  [1] What is Python?                            .
.  [2] Who wrote Python?                          .
.  [3] Programming examples                       .
.                                                 .
.  [99] ~> Main Menu                              .
.  [100] ~> Update                                .
.  [1000] ~ > About Author && Contact Author      .
.  [0] ~> Exit                                       .  
...................................................''')

    whs_python = int(input(Fore.YELLOW + 'PyLe ~$ '))
    if whs_python == 1:
        print('')
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.python.org/')
        print('')
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        print(Fore.WHITE + json.loads( data )['what_is_python']['whs_py'])
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        again_1()

    elif whs_python == 2:
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://en.wikipedia.org/wiki/Python_(programming_language)#History')
        print('')
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        print(Fore.WHITE + json.loads( data )['what_is_python']['woh_wrote'])
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        again_1()

    elif whs_python == 3:
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://en.wikipedia.org/wiki/Python_(programming_language)#History')
        print('')
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        print(Fore.WHITE + json.loads( data )['what_is_python']['exm'])
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        again_1()

    elif whs_python == 1000:
        system('clear')
        contact()
        again_1()

    elif whs_python == 100:
        system('clear')
        update()
    
    elif whs_python == 99:
        system('clear')
        start()

    elif whs_python == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()  


#Apps
def apps():
    print(random_color [0] + '''
         _                   _          _          _         
        / /\                /\ \       /\ \       / /\       
       / /  \              /  \ \     /  \ \     / /  \      
      / / /\ \            / /\ \ \   / /\ \ \   / / /\ \__   
     / / /\ \ \          / / /\ \_\ / / /\ \_\ / / /\ \___\  
    / / /  \ \ \        / / /_/ / // / /_/ / / \ \ \ \/___/  
   / / /___/ /\ \      / / /__\/ // / /__\/ /   \ \ \        
  / / /_____/ /\ \    / / /_____// / /_____/_    \ \ \       
 / /_________/\ \ \  / / /      / / /      /_/\__/ / /       
/ / /_       __\ \_\/ / /      / / /       \ \/___/ /        
\_\___\     /____/_/\/_/       \/_/         \_____\/                                                                
    ''')
    print (Fore.YELLOW + '[#]' + Fore.LIGHTMAGENTA_EX + ' Here I have prepared a list of software you may needed to start Python programming')
    print (Fore.RED + '[#]' + Fore.LIGHTCYAN_EX+ " Now Choose Your apps...")
    print (Fore.LIGHTYELLOW_EX+'''
===============================================
| (1) ~> Python Version +3                    |
| (2) ~> Python Version +2                    |
| (3) ~> Cmder                                |
| (4) ~> Atom                                 |
| (5) ~> NotePad ++                           |
| (6) ~> Sublime                              |
|                                             |
| <99> ~> Main Menu                           |
| <100> ~> Update                             |
| <1000> ~> About Author && Contact Author    |
| <0> ~> Exit                                 |
===============================================
''')
    
    apps_var = int(input(Fore.YELLOW + 'PyLe ~$ '))
    # download Python 3
    if apps_var == 1:
        system('clear')
        print(Fore.LIGHTYELLOW_EX + '[#]' + Fore.LIGHTMAGENTA_EX + 'Windows,Unix|Linux,Mac (W/U/M)')
        print()
        py3 = input(Fore.YELLOW + 'PyLe ~$ ')
        if py3.upper() == 'W':
            print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
            py3WV = int(input(Fore.YELLOW + 'PyLe ~$ '))
            if py3WV == 64:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (64bit)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe', 'python-3.9.5-amd64.exe')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            elif py3WV == 32:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (32bit)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/3.9.5/python-3.9.5.exe', 'python-3.9.5.exe')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            else:
                print(Fore.RED + '[!] Wrong Value')
                again_1()
        elif py3.upper() == 'U':
            print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (Unix/Linux Ver)')
            try:
                urllib.request.urlretrieve('https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz', 'Python-3.9.5.tgz')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()
        elif py3.upper() == 'M':
            print(Fore.LIGHTBLUE_EX + 'Which one ? for macOS 10.9 and later, for macOS 10.9 and later, including macOS 11 Big Sur on Apple Silicon (10/11)')
            py3M = int(input(Fore.YELLOW + 'PyLe ~$ '))
            if py3M == 10:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (10.9 and later)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/3.9.5/python-3.9.5-macosx10.9.pkg', 'python-3.9.5-macosx10.9.pkg')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            elif py3M == 11:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (Including macOS 11)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/3.9.5/python-3.9.5-macos11.pkg', 'python-3.9.5-macos11.pkg')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            else:
                print(Fore.RED + '[!] Wrong Value')
                again_1()
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    # download Python 2
    elif apps_var == 2:
        system('clear')
        print(Fore.LIGHTYELLOW_EX + '[#]' + Fore.LIGHTMAGENTA_EX + 'Python 2.7 / Windows,Unix|Linux,Mac (W/U/M)')
        print()
        py2 = input(Fore.YELLOW + 'PyLe ~$ ')
        if py2.upper() == 'W':
            print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
            py2WV = int(input(Fore.YELLOW + 'PyLe ~$ '))
            if py2WV == 64:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (2.7.18 / 64bit)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi', 'python-2.7.18.amd64.msi')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            elif py2WV == 32:
                print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (2.7.18 / 32bit)')
                try:
                    urllib.request.urlretrieve('https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi', 'python-2.7.18.msi')
                    print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                    sleep(1.0)
                    system('clear')
                    apps()
                except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            else:
                print(Fore.RED + '[!] Wrong Value')
                again_1()
        
        elif py2.upper() == 'U':
            print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (2.7.18v / Unix/Linux)')
            try:
                urllib.request.urlretrieve('https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz', 'Python-2.7.18.tgz')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()
        
        elif py2.upper() == 'M':
            print(Fore.LIGHTGREEN_EX + 'Wait friend, Downloading... (2.7.18 / Mac OS X 10.9)')
            try:
                urllib.request.urlretrieve('https://www.python.org/ftp/python/2.7.18/python-2.7.18-macosx10.9.pkg', 'python-2.7.18-macosx10.9.pkg')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                    print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                    again_1()
            else:
                print(Fore.RED + '[!] Wrong Value')
                again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    # download cmder
    elif apps_var == 3:
        print()
        print(Fore.LIGHTCYAN_EX + 'Great, Downloading...')
        try:
            urllib.request.urlretrieve('https://github.com/cmderdev/cmder/releases/download/v1.3.18/cmder.7z', 'Cmder.7z')
            print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
            sleep(1.0)
            system('clear')
            apps()
        except:
            print(Fore.LIGHTRED_EX + '[!] Connection Lost')
            again_1()

    elif apps_var == 4:
        system('clear')
        print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
        atom = int(input(Fore.YELLOW + 'PyLe ~$ '))
        if atom == 64:
            try:
                print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (Atom LastVer 64bit)')
                urllib.request.urlretrieve('https://github.com/atom/atom/releases/download/v1.57.0/AtomSetup-x64.exe', 'AtomSetup-x64.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()

        elif atom == 32:
            try:
                print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (Atom LastVer 32bit)')
                urllib.request.urlretrieve('https://github.com/atom/atom/releases/download/v1.57.0/AtomSetup.exe', 'AtomSetup.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    # download Notpad ++
    elif apps_var == 5:
        system('clear')
        print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
        notepad = int(input(Fore.YELLOW + 'PyLe ~$ '))
        if notepad == 64:
            print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (NotePad ++ LastVer 64bit)')
            try:
                urllib.request.urlretrieve('https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.5/npp.7.9.5.Installer.x64.exe', 'npp.7.9.5.Installer.x64.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                apps()

        elif notepad == 32:
            print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (NotePad ++ LastVer 32bit)')
            try:
                urllib.request.urlretrieve('https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.5/npp.7.9.5.Installer.exe', 'npp.7.9.5.Installer.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    # Download Sublime
    elif apps_var == 6:
        system('clear')
        print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
        sublime = int(input(Fore.YELLOW + 'PyLe ~$ '))
        if sublime == 64:
            print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (Sublime 3.2 64bit)')
            try:
                urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/apps/Sublime%20Text%20Build%203211%20x64%20Setup.exe', 'Setup64x.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!] Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()
        elif sublime == 32:
            print(Fore.LIGHTYELLOW_EX + 'Ok, Downloading... (Sublime 3.2 32bit)')
            try:
                urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/apps/Sublime%20Text%20Build%203211%20Setup.exe', 'Setup.exe')
                print(Fore.LIGHTMAGENTA_EX + '[!] Done !')
                sleep(1.0)
                system('clear')
                apps()
            except:
                print(Fore.LIGHTRED_EX + '[!] Connection Lost')
                again_1()
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
            
    ##########
    elif apps_var == 99:
        system('clear')
        start()            

    elif apps_var == 100:
        system('clear')
        update()

    elif apps_var == 1000:
        system('clear')
        contact()
        again_1()
    
    elif apps_var == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')
    
    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()
    

#Update
def update():
    print(Fore.RED + '[#]' + Fore.WHITE + ' This is 2.0 version')
    print(Fore.YELLOW + '[?]' + Fore.GREEN+ ' Do you wanna download last version From github? (Y/N)')
    version_pyle = input(Fore.YELLOW +'PyLe ~$ ')
    if version_pyle.upper() == 'Y':
        print(Fore.YELLOW + 'Please Wait ...')
        urllib.request.urlretrieve('https://github.com/AnonC0DER/PyLe/archive/refs/heads/main.zip' , 'PyLe.zip')
        system('clear')
        print(Fore.GREEN + '~> Download completed !')
    elif version_pyle.upper() == 'N':
        start()
    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


#About Me && contact Me
def contact():
    system('clear')
    print(Fore.LIGHTYELLOW_EX +'''
 ____________________________________________                                       
|   # I'm AnonCODER                          |                         
|       # My real name is Hesam              |         
| # if you have any idea for this appliction |
|        # or you wanna talk to me           |
|       # Contact Me : @AnonC0DER            |
|      # Email : AnonCODER@tutanota.com      |
|____________________________________________|
''')


#start
def start():
    system('clear')
    print(random_color [0] +'''
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌               ▐░▌     ▐░▌          ▐░▌          
▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀                 ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
 -------------
| Version 2.0 |
 -------------
''')

    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' Learn Python Libraries by Python script.')
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' PyLe helps you know new python libraries.')
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' The first Python script to help you progress in Python.')
    print (Fore.RED + '[$]' + Fore.LIGHTCYAN_EX+ " So, Let's Start !")

    print (Fore.LIGHTYELLOW_EX+'''
{-------------------------------------------------}
{ <Libraries>:                                    }
{        [1] > Colors                             }
{        [2] > Machine Learning                   }
{        [3] > Telegram Robots                    }
{        [4] > Game Development                   }
{        [5] > File & Text Encryption             }
{        [6] > Python SQL Libraries               }
{                                                 }
{ <Biginners>:                                    }
{        [10] ~> For beginner                     }
{        [99] ~> What Is Python ?                 }    
{        [999] ~> Apps                            }
{                                                 }
{                                                 }      
{ [100] ~> Update                                 }  
{ [1000] ~ > About Author && Contact Author       }
{ [0] Exit                                        }
{-------------------------------------------------}''')

    try:
        pyle_start = int(input(Fore.YELLOW + 'PyLe ~$ ')) 

        if pyle_start == 1:
            system('clear')
            c_lib()

        elif pyle_start == 2:
            system('clear')
            machine_learning()
            
        elif pyle_start == 3:
            system('clear')
            telegram_bots()
        
        elif pyle_start == 4:
            system('clear')
            game_dev()

        elif pyle_start == 5:
            system('clear')
            ft_enc()

        elif pyle_start == 6:
            system('clear')
            sql_lib()

        elif pyle_start == 10:
            system('clear')
            For_beginners()

        elif pyle_start == 1000:
            system('clear')
            contact()
            again_1()

        elif pyle_start == 100:
            system('clear')
            update()

        elif pyle_start == 99:
            system('clear')
            wip()

        elif pyle_start == 999:
            system('clear')
            apps()

        elif pyle_start == 0:
            print(Fore.YELLOW+'[-]──# Se You Later :)')

        else:
            print(Fore.RED+'[!]──# Wrong Value')
            again_1()
    except:
        print(Fore.RED+'[!]──# Wrong Value')
        again_1()


start()

# <------CoDed By AnonCODER------>
# <------First Version : v2.0------>
# <------Help me improve it :)------>
