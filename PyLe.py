# <------CoDed By AnonCODER------>
# <------v4.0----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>
##################################################################
# imports
import random
import urllib.request
import json
import sys
# For Object-oriented programming
from imports.other_libraries import *
# I use this because, some libraries dosen't need installtion 
from imports import libraries
# Open FreeCourses Function
from imports import Courses
# import send email functions
from imports import Emails
from os import system
# import typing function
from imports import typer
# import search function
from imports import search
from colorama import Fore
from time import sleep

#############
import time
from datetime import datetime
#############

# again
def again_1():
    again_v = input(Fore.GREEN+'For Menu type (M) for Exit type (E) : ')
    if again_v.upper() == 'M' or again_v.upper() == 'Menu' or again_v.lower() == 'm' or again_v.lower() == 'menu':
        start()
    elif again_v.upper() == 'E' or again_v.upper() == 'Exit' or again_v.lower() == 'e' or again_v.lower() == 'exit':
        print(Fore.YELLOW+'[-] Good Luck !')
        close_time()
    else:
        print(Fore.RED+'Wrong Value !')
        again_1()

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
[2] => Colorama
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
        print()
        colord = input(Fore.YELLOW +'PyLe ~$ ')
        colord_info = libraries.all_libraries('colored --upgrade', 'Colors', 'colored_dec', 'colored_exm', 'https://gitlab.com/dslackw/colored/blob/master/CHANGELOG')
        
        if colord.upper() == 'I':
            colord_info.AllLibs_install()
            again_1()

        elif colord.upper() == 'D':
            colord_info.AllLibs_dec()
            again_1()

        elif colord.upper() == 'E':
           colord_info.AllLibs_exm()
           again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif colors_lib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/colorama/')
        print()
        colorama = input(Fore.YELLOW +'PyLe ~$ ')
        colorama_info = libraries.all_libraries('colorama', 'Colors', 'colorama_dec', 'colorama_exm', 'https://github.com/tartley/colorama')

        if colorama.upper() == 'I':
            colorama_info.AllLibs_install()
            again_1()

        elif colorama.upper() == 'D':
            colorama_info.AllLibs_dec()
            again_1()

        elif colorama.upper() == 'E':
           colorama_info.AllLibs_exm()
           again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif colors_lib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/termcolor/')
        print()
        termcolor = input(Fore.YELLOW +'PyLe ~$ ')
        termcolor_info = libraries.all_libraries('termcolor', 'Colors', 'termcolor_dec', 'termcolor_exm', 'http://pypi.python.org/pypi/termcolor')
        if termcolor.upper() == 'I':
            termcolor_info.AllLibs_install()
            again_1()

        elif termcolor.upper() == 'D':
            termcolor_info.AllLibs_dec()
            again_1()

        elif termcolor.upper() == 'E':
           termcolor_info.AllLibs_exm()
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
        close_time()

    else:
        print(Fore.RED+'[!]──# Wrong Value')
        again_1()


# Machine Learning & DataAnalysis
def machine_learning():
    print (random_color [0] + '''   
   __     __)                              _                           
  (, /|  /|         /)   ,             ___/__)                ,        
    / | / |  _   _ (/     __    _     (, /    _  _   __ __     __   _  
 ) /  |/  |_(_(_(__/ )__(_/ (__(/_      /   _(/_(_(_/ (_/ (__(_/ (_(_/_
(_/   '                                (_____                     .-/  
                                              )                  (_/                                        
''')                             

    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Welcome to the Python Machine Learning & DataAnalysis Libraries.')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' You can get various information from this section')
    print (Fore.YELLOW + '[#]' + Fore.MAGENTA+ ' Such as installing libraries and descriptions about them.')
    print (Fore.GREEN + '[#]' + Fore.MAGENTA+ " Now Choose Your Library... ")

    print (Fore.LIGHTBLUE_EX +'''
{-------------}
[1] => Scikit-learn
[2] => Keras 
[3] => Xgboost
[4] => Statsmodels
[5] => Tensorflow
[6] => Numpy
[7] => SciPy
[8] => Matplotlib
[9] => Seaborn
[10] => PyTorch
[11] => PyCaret 

[1000] About Author && Contact Author
[100] Update
[99] Main Menu
[0] Exit
{-------------}''')

    machine_lib = int(input(Fore.YELLOW +'PyLe ~$ '))
    
    # scikit-learn
    if machine_lib == 1:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/scikit-learn/')
        print()
        scikit = input(Fore.YELLOW +'PyLe ~$ ')
        if scikit.upper() == 'I':
            machinlearning_class.scikit_install()
            again_1()

        elif scikit.upper() == 'D':
            machinlearning_class.scikit_dec()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # keras
    elif machine_lib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/keras/')
        print()
        keras = input(Fore.YELLOW +'PyLe ~$ ')
        keras_info = libraries.all_libraries('keras', 'Machin_Learning', 'keras_dec', 'keras_exm', 'https://keras.io/examples/')
        
        if keras.upper() == 'I':
            keras_info.AllLibs_install()
            again_1()

        elif keras.upper() == 'D':
            keras_info.AllLibs_dec()
            again_1()

        elif keras.upper() == 'E':
            keras_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # xgboost
    elif machine_lib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.GREEN + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html')
        print()
        xgboost = input(Fore.YELLOW +'PyLe ~$ ')
        xgboost_info = libraries.all_libraries('xgboost', 'Machin_Learning', 'xgboost_dec', 'xgboost_exm', 'https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html')
        
        if xgboost.upper() == 'I':
            xgboost_info.AllLibs_install()
            again_1()

        elif xgboost.upper() == 'D':
            xgboost_info.AllLibs_dec()
            again_1()

        elif xgboost.upper() == 'E':
            xgboost_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # statsmodels
    elif machine_lib == 4:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/statsmodels/')
        print()
        statsmodels = input(Fore.YELLOW +'PyLe ~$ ')
        statsmodels_info = libraries.all_libraries('statsmodels', 'Machin_Learning', 'statsmodels_dec', 'statsmodels_exm', 'https://www.statsmodels.org/stable/')
        
        if statsmodels.upper() == 'I':
            statsmodels_info.AllLibs_install()
            again_1()

        elif statsmodels.upper() == 'D':
            statsmodels_info.AllLibs_dec()
            again_1()

        elif statsmodels.upper() == 'E':
            statsmodels_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Tensorflow
    elif machine_lib == 5:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.tensorflow.org/tutorials')
        print()
        tensorflow = input(Fore.YELLOW +'PyLe ~$ ')
        tensorflow_info = libraries.all_libraries('tensorflow', 'Machin_Learning', 'tensorflow_dec', 'tensorflow_exm', 'https://rubikscode.net/2018/02/05/introduction-to-tensorflow-with-python-example/')
        
        if tensorflow.upper() == 'I':
            tensorflow_info.AllLibs_install()
            again_1()

        elif tensorflow.upper() == 'D':
            tensorflow_info.AllLibs_dec()
            again_1()

        elif tensorflow.upper() == 'E':
            tensorflow_info.AllLibs_exm()
            again_1()
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Numpy
    elif machine_lib == 6:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://numpy.org/doc/stable/user/whatisnumpy.html')
        print()
        numpy = input(Fore.YELLOW +'PyLe ~$ ')
        numpy_info = libraries.all_libraries('numpy', 'Machin_Learning', 'numpy_dec', 'numpy_exm', 'https://numpy.org/doc/stable/user/quickstart.html')
        
        if numpy.upper() == 'I':
            numpy_info.AllLibs_install()
            again_1()

        elif numpy.upper() == 'D':
            numpy_info.AllLibs_dec()
            again_1()
        
        elif numpy.upper() == 'E':
            numpy_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # SciPy
    elif machine_lib == 7:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.scipy.org/doc/scipy/reference/tutorial/general.html')
        print()
        SciPy = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        SciPy_info = libraries.all_libraries('scipy', 'Machin_Learning', 'scipy_dec', 'scipy_exm', 'https://docs.scipy.org/doc/scipy/reference/tutorial/index.html')
        
        if SciPy.upper() == 'I':
            SciPy_info.AllLibs_install()
            again_1()
        
        elif SciPy.upper() == 'D':
            SciPy_info.AllLibs_dec()
            again_1()
        
        elif SciPy.upper() == 'E':
            SciPy_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Matplotlib
    elif machine_lib == 8:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://matplotlib.org/stable/contents.html')
        print()
        Matplotlib = input(Fore.YELLOW +'PyLe ~$ ')
        Matplotlib_info = libraries.all_libraries('matplotlib', 'Machin_Learning', 'matplotlib_dec', 'matplotlib_exm', 'https://matplotlib.org/stable/gallery/index.html')
        
        if Matplotlib.upper() == 'I':
            Matplotlib_info.AllLibs_install()
            again_1()
        
        elif Matplotlib.upper() == 'D':
            Matplotlib_info.AllLibs_dec()
            again_1()
        
        elif Matplotlib.upper() == 'E':
            Matplotlib_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
        
    # Seaborn
    elif machine_lib == 9:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://seaborn.pydata.org/introduction.html')
        print()
        Seaborn = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Seaborn_info = libraries.all_libraries('seaborn', 'Machin_Learning', 'seaborn_dec', 'seaborn_exm', 'https://seaborn.pydata.org/examples/index.html')
        
        if Seaborn.upper() == 'I':
            Seaborn_info.AllLibs_install()
            again_1()
        
        elif Seaborn.upper() == 'D':
            Seaborn_info.AllLibs_dec()
            again_1()
        
        elif Seaborn.upper() == 'E':
            Seaborn_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # PyTorch
    elif machine_lib == 10:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pytorch.org/get-started/locally/')
        print()
        PyTorch = input(Fore.YELLOW +'PyLe ~$ ')
        PyTorch_info = libraries.all_libraries('torch', 'Machin_Learning', 'PyTorch_dec', 'PyTorch_exm', 'https://pytorch.org/tutorials/beginner/pytorch_with_examples.html')
        
        if PyTorch.upper() == 'I':
            PyTorch_info.AllLibs_install()
            again_1()
        
        elif PyTorch.upper() == 'D':
            PyTorch_info.AllLibs_dec()
            again_1()
        
        elif PyTorch.upper() == 'E':
            PyTorch_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # PyCaret
    elif machine_lib == 11:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pycaret.org/')
        print()
        PyCaret = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if PyCaret.upper() == 'I':
            machinlearning_class.pycaret_install()
            again_1()
        
        elif PyCaret.upper() == 'D':
            machinlearning_class.pycaret_dec()
            again_1()
        
        elif PyCaret.upper() == 'E':
            # using all_libraries.py
            machinlearning_class.pycaret_exm1()
            PyCaret_exm2 = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
            # show example 2 
            if PyCaret_exm2.upper() == 'Y':
                machinlearning_class.pycaret_exm2()
                again_1()  

            elif PyCaret_exm2.upper() == 'N':
                again_1()

            else:
                print(Fore.RED + '[!] Wrong Value')
                again_1()     

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # Menu
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
        close_time()

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
    print()
    python_telegram_bot = input(Fore.YELLOW +'PyLe ~$ ')
    python_telegram_bot_info = libraries.all_libraries('python-telegram-bot', 'Telegram_bots', 'python_telegram_bot_dec', 'python_telegram_bot_exm', 'https://python-telegram-bot.readthedocs.io/en/stable/')
    
    if python_telegram_bot.upper() == 'I':
      python_telegram_bot_info.AllLibs_install()
      again_1()

    elif python_telegram_bot.upper() == 'D':
      python_telegram_bot_info.AllLibs_dec()
      again_1()

    elif python_telegram_bot.upper() == 'E':
      python_telegram_bot_info.AllLibs_exm()
      again_1()
      
    else:
      print(Fore.RED + '[!] Wrong Value')
      again_1()


  elif robots_lib == 2:
    print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
    print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/Pyrogram/')
    print()
    pyrogram = input(Fore.YELLOW +'PyLe ~$ ')
    if pyrogram.upper() == 'I':
      telegrambots_class.Pyrogram_install()
      again_1()
          
    elif pyrogram.upper() == 'D':
      telegrambots_class.Pyrogram_dec()
      again_1()
      
    elif pyrogram.upper() == 'E':
      telegrambots_class.Pyrogram_exm()
      again_1()

    else:
      print(Fore.RED + '[!] Wrong Value')
      again_1()


  elif robots_lib == 3:
    print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
    print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://telegrampy.readthedocs.io/en/latest/?badge=latest')
    print()
    telegram_py = input(Fore.YELLOW +'PyLe ~$ ')
    telegram_py_info = libraries.all_libraries('telegram.py', 'Telegram_bots', 'telegram_dec', 'telegram_exm', 'https://telegrampy.readthedocs.io/en/latest/quickstart.html')
    
    if telegram_py.upper() == 'I':
        telegram_py_info.AllLibs_install()
        again_1()
          
    elif telegram_py.upper() == 'D':
        telegram_py_info.AllLibs_dec()
        again_1()
      
    elif telegram_py.upper() == 'E':
      telegram_py_info.AllLibs_exm()
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
    close_time()

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
        print()
        pygame = input(Fore.YELLOW +'PyLe ~$ ')
        pygame_info = libraries.all_libraries('pygame', 'game_devel', 'pygame_dec', 'pygame_exm', 'https://www.pygame.org/docs/ref/examples.html')
        
        if pygame.upper() == 'I':
            pygame_info.AllLibs_install()
            again_1()
        
        elif pygame.upper() == 'D':
            pygame_info.AllLibs_dec()
            again_1()

        elif pygame.upper() == 'E':
            pygame_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    
    elif g_dev == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Examples 'E.'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/turtle.html')
        print()
        turtles = input(Fore.YELLOW +'PyLe ~$ ')
        turtles_info = libraries.all_libraries('turtles', 'game_devel', 'turtles_dec', 'turtles_exm', 'https://michael0x2a.com/blog/turtle-examples')
        
        if turtles.upper() == 'I':
            turtles_info.AllLibs_install()
            again_1()

        elif turtles.upper() == 'D':
            turtles_info.AllLibs_dec()
            again_1()

        elif turtles.upper() == 'E':
            turtles_info.AllLibs_exm()
            again_1()
      
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif g_dev == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Examples 'E.'")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' http://pyopengl.sourceforge.net/documentation/index.html')
        print()
        pyopengl = input(Fore.YELLOW +'PyLe ~$ ')
        pyopengl_info = libraries.all_libraries('PyOpenGL', 'game_devel', 'pyopengl_dec', 'pyopengl_dec', 'https://noobtuts.com/python/opengl-introduction')
        
        if pyopengl.upper() == 'I':
            pyopengl_info.AllLibs_install()
            again_1()

        elif pyopengl.upper() == 'D':
            pyopengl_info.AllLibs_dec()
            again_1()

        elif pyopengl.upper() == 'E':
            pyopengl_info.AllLibs_exm()
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
        close_time()

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
        print()
        cryptography = input(Fore.YELLOW +'PyLe ~$ ')
        cryptography_info = libraries.all_libraries('cryptography', 'file_enc', 'cryptography_dec', 'cryptography_exm', 'https://cryptography.io/en/latest/')
        
        if cryptography.upper() == 'I':
            cryptography_info.AllLibs_install()
            again_1()
            
        elif cryptography.upper() == 'D':
            cryptography_info.AllLibs_dec()
            again_1()

        elif cryptography.upper() == 'E':
            cryptography_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif ft_en == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pypi.org/project/pycrypto/')
        print()
        pycrypto = input(Fore.YELLOW +'PyLe ~$ ')
        pycrypto_info = libraries.all_libraries('pycrypto', 'file_enc', 'pycrypto_dec', 'pycrypto_exm', 'https://www.dlitz.net/software/pycrypto/')
        
        if pycrypto.upper() == 'I':
            pycrypto_info.AllLibs_install()
            again_1()

        elif pycrypto.upper() == 'D':
            pycrypto_info.AllLibs_dec()
            again_1()

        elif pycrypto.upper() == 'E':
            pycrypto_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif ft_en == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.aescrypt.com/pyaescrypt.html')
        print()
        pyaescrypt = input(Fore.YELLOW +'PyLe ~$ ')
        pyaescrypt_info = libraries.all_libraries('pyAesCrypt', 'file_enc', 'pyaescrypt_dec', 'pyaescrypt_exm', 'https://pypi.org/project/pyAesCrypt/')
        
        if pyaescrypt.upper() == 'I':
            pyaescrypt_info.AllLibs_install()
            again_1()

        elif pyaescrypt.upper() == 'D':
            pyaescrypt_info.AllLibs_dec()
            again_1()

        elif pyaescrypt.upper() == 'E':
            pyaescrypt_info.AllLibs_exm()
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
        close_time()

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
        print()
        SQLite = input(Fore.YELLOW +'PyLe ~$ ')
        SQLite_info = libraries.all_libraries('pysqlite3', 'sqllib', 'sqlite_dec', 'sqlite_exm', 'https://www.tutorialspoint.com/sqlite/sqlite_python.htm')
        
        if SQLite.upper() == 'I':
            SQLite_info.AllLibs_install()
            again_1()

        elif SQLite.upper() == 'D':
            SQLite_info.AllLibs_dec()
            again_1()

        elif SQLite.upper() == 'E':
            SQLite_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    elif sql_plib == 2:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html')
        print()
        MySQL = input(Fore.YELLOW +'PyLe ~$ ')
        MySQL_info = libraries.all_libraries('mysql-connector-python', 'sqllib', 'mysql_dec', 'mysql_exm', 'https://www.w3schools.com/python/python_mysql_select.asp')
        
        if MySQL.upper() == 'I':
            MySQL_info.AllLibs_install()
            again_1()

        elif MySQL.upper() == 'D':
            MySQL_info.AllLibs_dec()
            again_1()

        elif MySQL.upper() == 'E':
            MySQL_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    elif sql_plib == 3:
        print (Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.tutorialspoint.com/postgresql/postgresql_python.htm')
        print()
        postgres = input(Fore.YELLOW +'PyLe ~$ ')
        postgres_info = libraries.all_libraries('postgres', 'sqllib', 'postgres_dec', 'postgres_exm', 'https://stackabuse.com/working-with-postgresql-in-python/')
        
        if postgres.upper() == 'I':
            postgres_info.AllLibs_install()
            again_1()

        elif postgres.upper() == 'D':
            postgres_info.AllLibs_dec()
            again_1()

        elif postgres.upper() == 'E':
            postgres_info.AllLibs_exm()
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
        close_time()

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


# Other Libraries
def other():
    print(random_color [0] + '''
 ____, ____,__, _,____,____,   __,  __, ____ ____, 
(-/  \(-|  (-|__|(-|_,(-|__)  (-|  (-| (-|__|-(__  
 _\__/,_|,  _|  |,_|__,_|  \,  _|__,_|_,_|__)____) 
(     (    (     (    (       (    (   (    (                                                         
    ''')
    print()
    print(Fore.LIGHTWHITE_EX + '[#]' + Fore.LIGHTBLUE_EX + ' Here i prepared a list of someother Python Libraries.')
    print(Fore.LIGHTWHITE_EX + '[#]' + Fore.LIGHTGREEN_EX + ' I wish it can helps you :)')
    print(Fore.LIGHTMAGENTA_EX + '''
::::::::::::::::::::::::::::::::::::::::::
: |_1_| ~>  Os (Operating System)        :
: |_2_| ~>  Subprocess                   :
: |_3_| ~>  Urllib Request               :
: |_4_| ~>  Requests                     :
: |_5_| ~>  Tkinter                      :
: |_6_| ~>  PyQt                         :
: |_7_| ~>  MoviePy                      :
: |_8_| ~>  datetime                     :
: |_9_| ~>  Pendulum                     :
: |_10_| ~> Pillow                       :
: |_11_| ~> OpenCV Python                :
: |_12_| ~> Theano                       :                      
: |_13_| ~> Fire                         :
: |_14_| ~> Arrow                        :
: |_15_| ~> FlashText                    :
: |_16_| ~> wxPython                     :
: |_17_| ~> Cirq                         :
: |_18_| ~> Json                         :
: |_19_| ~> Sys                          :
: |_20_| ~> InstaPy                      :
: |_21_| ~> Cython                       :
: |_22_| ~> pytube                       :
: |_23_| ~> Typer                        :
: |_24_| ~> Rich                         :
: |_25_| ~> Dear PyGui                   :
: |_26_| ~> PrettyErrors                 :
: |_27_| ~> Diagrams                     :                                                                         
: |_28_| ~> HiPlot                       :                                                                              
: |_29_| ~> Selenium                     :                                                                              
: |_30_| ~> Pandas                       :                                                                              
: |_31_| ~> Delorean                     :                                                                              
: |_32_| ~> sh                           :                                                                              
: |_33_| ~> PyMC                         :                                                                              
: |_34_| ~> fuzzywuzzy                   :                                                                              
: |_35_| ~> progressbar                  :
:                                        :                                                                              
:                                        :
: |_99_| ~> Main Menu                    :
: |_100_| ~> Update                      :
: |_0_| ~> Exit                          :
::::::::::::::::::::::::::::::::::::::::::''')

    print()
    other_list = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
    # Os
    if other_list == 1:
        print (Fore.MAGENTA + "(Os dosen't need Installation), Description 'D', Example 'E'.")
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/os.html')
        print()
        Os = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if Os.upper() == 'D':
            other_class.Os_dec()
            again_1()
        
        elif Os.upper() == 'E':
            other_class.Os_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')            
            again_1()
    
    # Subprocess
    elif other_list == 2:
        print(Fore.MAGENTA + "(Subprocess dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/asyncio-subprocess.html')
        print()
        Subprocess = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if Subprocess.upper() == 'D':
            other_class.subprocess_dec()
            again_1()
        
        elif Subprocess.upper() == 'E':
            other_class.subprocess_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # Urllib Request
    elif other_list == 3:
        print(Fore.MAGENTA + "(Urllib Request dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/urllib.request.html#module-urllib.request')
        print()
        urllib_request = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if urllib_request.upper() == 'D':
            other_class.UrllibRequest_dec()
            again_1()
        
        elif urllib_request.upper() == 'E':
            other_class.UrllibRequest_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()


    # Requests
    elif other_list == 4:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python-requests.org/en/master/')
        print()
        Requests = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Requests_info = libraries.all_libraries('requests', 'other', 'requests_dec', 'requests_exm', 'https://docs.python-requests.org/en/master/user/quickstart/')
        if Requests.upper() == 'I':
            Requests_info.AllLibs_install()
            again_1()
        
        elif Requests.upper() == 'D':
            Requests_info.AllLibs_dec()
            again_1()
        
        elif Requests.upper() == 'E':
            Requests_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # Tkinter
    elif other_list == 5:
        print(Fore.MAGENTA + "(Tkinter dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/tkinter.html')
        print()
        tkinter = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if tkinter.upper() == 'D':
            other_class.Tkinter_dec()
            again_1()
        
        elif tkinter.upper() == 'E':
            other_class.Tkinter_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # PyQt
    elif other_list == 6:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://riverbankcomputing.com/software/pyqt/')
        print()
        pyqt = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if pyqt.upper() == 'I':
            other_class.PyQt5_installtion()
            again_1()
        
        elif pyqt.upper() == 'D':
            other_class.PyQt5_dec()
            again_1()
        
        elif pyqt.upper() == 'E':
            other_class.PyQt5_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # MoviePy
    elif other_list == 7:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://zulko.github.io/moviepy/')
        print()
        moviepy = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        moviepy_info = libraries.all_libraries('moviepy', 'other', 'moviepy_dec', 'moviepy_exm', 'https://zulko.github.io/moviepy/examples/examples.html')
        if moviepy.upper() == 'I':
            moviepy_info.AllLibs_install()
            again_1()
        
        elif moviepy.upper() == 'D':
            moviepy_info.AllLibs_dec()
            again_1()

        elif moviepy.upper() == 'E':
            moviepy_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # datetime
    elif other_list == 8:
        print(Fore.MAGENTA + "(datetime dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/datetime.html')
        print()
        datetime = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if datetime.upper() == 'D':
            other_class.datetime_dec()
            again_1()
        
        elif datetime.upper() == 'E':
            other_class.datetime_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Pendulum
    elif other_list == 9:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pendulum.eustace.io/docs/')
        print()
        Pendulum = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Pendulum_info = libraries.all_libraries('pendulum', 'other', 'pendulum_dec', 'pendulum_exm', 'https://pendulum.eustace.io/')
        if Pendulum.upper() == 'I':
            Pendulum_info.AllLibs_install()
            again_1()
        
        elif Pendulum.upper() == 'D':
            Pendulum_info.AllLibs_dec()
            again_1()
        
        elif Pendulum.upper() == 'E':
            Pendulum_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Pillow
    elif other_list == 10:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://python-pillow.org/')
        print()
        Pillow = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Pillow_info = libraries.all_libraries('Pillow', 'other', 'pillow_dec', 'pillow_exm', 'https://pillow.readthedocs.io/en/stable/reference/Image.html#examples')
        if Pillow.upper() == 'I':
            Pillow_info.AllLibs_install()
            again_1()
        
        elif Pillow.upper() == 'D':
            Pillow_info.AllLibs_dec()
            again_1()

        
        elif Pillow.upper() == 'E':
            Pillow_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # OpenCV Python
    elif other_list == 11:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.opencv.org/master/d6/d00/tutorial_py_root.html')
        print()
        opencv = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        opencv_info = libraries.all_libraries('opencv-python', 'other', 'opencvpython_dec', 'opencvpython_exm', 'https://docs.opencv.org/master/dc/d4d/tutorial_py_table_of_contents_gui.html')
        if opencv.upper() == 'I':
            opencv_info.AllLibs_install()
            again_1()

        elif opencv.upper() == 'D':
            opencv_info.AllLibs_dec()
            again_1()

        elif opencv.upper() == 'E':
            opencv_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Theano
    elif other_list == 12:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.tutorialspoint.com/theano/index.htm')
        print()
        Theano = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Theano_info = libraries.all_libraries('Theano', 'other', 'theano_dec', 'theano_exm', 'https://docs.python-requests.org/en/master/user/quickstart/')
        if Theano.upper() == 'I':
            Theano_info.AllLibs_install()
            again_1()
        
        elif Theano.upper() == 'D':
            Theano_info.AllLibs_dec()
            again_1()
        
        elif Theano.upper() == 'E':
            Theano_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # Fire
    elif other_list == 13:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://google.github.io/python-fire/')
        print()
        Fire = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Fire_info = libraries.all_libraries('fire', 'other', 'fire_dec', 'fire_exm', 'https://google.github.io/python-fire/guide/#hello-world')
        if Fire.upper() == 'I':
            Fire_info.AllLibs_install()
            again_1()

        elif Fire.upper() == 'D':
            Fire_info.AllLibs_dec()
            again_1()

        elif Fire.upper() == 'E':
            Fire_info.AllLibs_exm()    
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Arrow
    elif other_list == 14:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://arrow.readthedocs.io/en/latest/')
        print()
        Arrow = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Arrow_info = libraries.all_libraries('arrow', 'other', 'arrow_dec', 'arrow_exm', 'https://arrow.readthedocs.io/en/latest/#example-usage')
        if Arrow.upper() == 'I':
            Arrow_info.AllLibs_install()
            again_1()
        
        elif Arrow.upper() == 'D':
            Arrow_info.AllLibs_dec()
            again_1()
        
        elif Arrow.upper() == 'E':
            Arrow_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
        
    # FlashText
    elif other_list == 15:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://flashtext.readthedocs.io/en/latest/')
        print()
        FlashText = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        FlashText_info = libraries.all_libraries('flashtext', 'other', 'flashtext_dec', 'flashtext_exm', 'https://flashtext.readthedocs.io/en/latest/#usage')
        if FlashText.upper() == 'I':
            FlashText_info.AllLibs_install()
            again_1()
        
        elif FlashText.upper() == 'D':
            FlashText_info.AllLibs_dec()
            again_1()
        
        elif FlashText.upper() == 'E':
            FlashText_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # wxPython
    elif other_list == 16:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://wxpython.org/')
        print()
        wxPython = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        wxPython_info = libraries.all_libraries('wxPython', 'other', 'wxpython_dec', 'wxpython_exm', 'https://docs.wxpython.org/')
        if wxPython.upper() == 'I':
            wxPython_info.AllLibs_install()
            again_1()
        
        elif wxPython.upper() == 'D':
            wxPython_info.AllLibs_dec()
            again_1()
        
        elif wxPython.upper() == 'E':
            wxPython_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Cirq
    elif other_list == 17:
        print(Fore.MAGENTA + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://quantumai.google/cirq/install')
        print()
        Cirq = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Cirq_info = libraries.all_libraries('cirq', 'other', 'cirq_dec', 'cirq_exm', 'https://quantumai.google/cirq/start')
        if Cirq.upper() == 'I':
            Cirq_info.AllLibs_install()
            again_1()

        elif Cirq.upper() == 'D':
            Cirq_info.AllLibs_dec()
            again_1()
        
        elif Cirq.upper() == 'E':
            Cirq_info.AllLibs_exm()
            again_1()
        
        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # Json
    elif other_list == 18:
        print(Fore.MAGENTA + "(Json dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/json.html#basic-usage')
        print()
        JSON = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if JSON.upper() == 'D':
            other_class.JSON_dec()
            again_1()
        
        elif JSON.upper() == 'E':
            other_class.JSON_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()
    
    # Sys
    elif other_list == 19:
        print(Fore.MAGENTA + "(Sys dosen't need Installation), Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://docs.python.org/3/library/sys.html')
        print()
        Sys = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if Sys.upper() == 'D':
            other_class.Sys_dec()
            again_1()
        
        elif Sys.upper() == 'E':
            other_class.Sys_exm()
            again_1()

        else:
            print(Fore.RED + '[!] Wrong Value')
            again_1()

    # InstaPy
    elif other_list == 20:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://instapy.org/')
        print()
        instapy = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        instapy_info = libraries.all_libraries('instapy', 'other', 'instapy_dec', 'instapy_exm', 'https://instapy.org/actions')
        if instapy.upper() == 'I':
            instapy_info.AllLibs_install()
            again_1()

        elif instapy.upper() == 'D':
            instapy_info.AllLibs_dec()
            again_1()

        elif instapy.upper() == 'E':
            instapy_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Cython
    elif other_list == 21:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://cython.org/')
        print()
        Cython = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Cython_info = libraries.all_libraries('Cython', 'other', 'cython_dec', 'cython_exm', 'https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html')
        if Cython.upper() == 'I':
            Cython_info.AllLibs_install()
            again_1()

        elif Cython.upper() == 'D':
            Cython_info.AllLibs_dec()
            again_1()

        elif Cython.upper() == 'E':
            Cython_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # pytube
    elif other_list == 22:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://cython.org/')
        print()
        pytube = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        pytube_info = libraries.all_libraries('pytube', 'other', 'pytube_dec', 'pytube_exm', 'https://pytube.io/en/latest/user/streams.html')
        if pytube.upper() == 'I':
            pytube_info.AllLibs_install()
            again_1()

        elif pytube.upper() == 'D':
            pytube_info.AllLibs_dec()
            again_1()

        elif pytube.upper() == 'E':
            pytube_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Typer
    elif other_list == 23:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://typer.tiangolo.com/')
        print()
        Typer = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Typer_info = libraries.all_libraries('typer', 'other', 'typer_dec', 'typer_exm', 'https://typer.tiangolo.com/#example')
        if Typer.upper() == 'I':
            Typer_info.AllLibs_install()
            again_1()

        elif Typer.upper() == 'D':
            Typer_info.AllLibs_dec()
            again_1()

        elif Typer.upper() == 'E':
            Typer_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Rich
    elif other_list == 24:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://rich.readthedocs.io/en/stable/introduction.html')
        print()
        Rich = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Rich_info = libraries.all_libraries('rich', 'other', 'rich_dec', 'rich_exm', 'https://rich.readthedocs.io/en/stable/console.html')        
        if Rich.upper() == 'I':
            Rich_info.AllLibs_install()
            again_1()

        elif Rich.upper() == 'D':
            Rich_info.AllLibs_dec()
            again_1()

        elif Rich.upper() == 'E':
            Rich_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Dear PyGui
    elif other_list == 25:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://github.com/hoffstadt/DearPyGui/wiki')
        print()
        DearPyGui = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        DearPyGui_info = libraries.all_libraries('dearpygui', 'other', 'dearpygui_dec', 'dearpygui_exm', 'https://github.com/hoffstadt/DearPyGui/wiki/Creating-Widgets')
        if DearPyGui.upper() == 'I':
            DearPyGui_info.AllLibs_install()
            again_1()

        elif DearPyGui.upper() == 'D':
            DearPyGui_info.AllLibs_dec()
            again_1()

        elif DearPyGui.upper() == 'E':
            DearPyGui_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # PrettyErrors
    elif other_list == 26:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://github.com/onelivesleft/PrettyErrors')
        print()
        PrettyErrors = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        PrettyErrors_info = libraries.all_libraries('pretty_errors', 'other', 'prettyErrors_dec', 'prettyErrors_exm', 'https://github.com/onelivesleft/PrettyErrors#scraping-stderr')
        if PrettyErrors.upper() == 'I':
            PrettyErrors_info.AllLibs_install()
            again_1()

        elif PrettyErrors.upper() == 'D':
            PrettyErrors_info.AllLibs_dec()
            again_1()

        elif PrettyErrors.upper() == 'E':
            PrettyErrors_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Diagrams
    elif other_list == 27:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://diagrams.mingrammer.com/docs/getting-started/installation')
        print()
        Diagrams = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Diagrams_info = libraries.all_libraries('diagrams', 'other', 'diagrams_dec', 'diagrams_exm', 'https://diagrams.mingrammer.com/docs/guides/diagram')
        if Diagrams.upper() == 'I':
            Diagrams_info.AllLibs_install()
            again_1()

        elif Diagrams.upper() == 'D':
            Diagrams_info.AllLibs_dec()
            again_1()

        elif Diagrams.upper() == 'E':
            Diagrams_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # HiPlot
    elif other_list == 28:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://facebookresearch.github.io/hiplot/index.html')
        print()
        HiPlot = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        HiPlot_info = libraries.all_libraries('hiplot', 'other', 'hiplot_dec', 'hiplot_exm', 'https://facebookresearch.github.io/hiplot/tuto_webserver.html')
        if HiPlot.upper() == 'I':
            HiPlot_info.AllLibs_install()
            again_1()

        elif HiPlot.upper() == 'D':
            HiPlot_info.AllLibs_dec()
            again_1()

        elif HiPlot.upper() == 'E':
            HiPlot_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Selenium
    elif other_list == 29:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://facebookresearch.github.io/hiplot/index.html')
        print()
        Selenium = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Selenium_info = libraries.all_libraries('selenium', 'other', 'selenium_dec', 'selenium_exm', 'https://selenium-python.readthedocs.io/getting-started.html')
        if Selenium.upper() == 'I':
            Selenium_info.AllLibs_install()
            again_1()

        elif Selenium.upper() == 'D':
            Selenium_info.AllLibs_dec()
            again_1()

        elif Selenium.upper() == 'E':
            Selenium_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Pandas
    elif other_list == 30:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://pandas.pydata.org/')
        print()
        Pandas = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Pandas_info = libraries.all_libraries('pandas', 'other', 'pandas_dec', 'pandas_exm', 'https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html')
        if Pandas.upper() == 'I':
            Pandas_info.AllLibs_install()
            again_1()

        elif Pandas.upper() == 'D':
            Pandas_info.AllLibs_dec()
            again_1()

        elif Pandas.upper() == 'E':
            Pandas_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Delorean
    elif other_list == 31:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://delorean.readthedocs.io/en/latest/')
        print()
        Delorean = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        Delorean_info = libraries.all_libraries('Delorean', 'other', 'delorean_dec', 'delorean_exm', 'https://delorean.readthedocs.io/en/latest/#getting-started')
        if Delorean.upper() == 'I':
            Delorean_info.AllLibs_install()
            again_1()

        elif Delorean.upper() == 'D':
            Delorean_info.AllLibs_dec()
            again_1()

        elif Delorean.upper() == 'E':
            Delorean_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # Sh
    elif other_list == 32:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' http://amoffat.github.io/sh/')
        print()
        Sh_lib = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        ShLib_info = libraries.all_libraries('sh', 'other', 'sh_dec', 'sh_exm', 'http://amoffat.github.io/sh/usage.html')
        if Sh_lib.upper() == 'I':
            ShLib_info.AllLibs_install()
            again_1()

        elif Sh_lib.upper() == 'D':
            ShLib_info.AllLibs_dec()
            again_1()

        elif Sh_lib.upper() == 'E':
            ShLib_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # PyMC
    elif other_list == 33:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' http://pymc-devs.github.io/pymc/')
        print()
        PyMC = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        PyMC_info = libraries.all_libraries('pymc', 'other', 'pymc_dec', 'pymc_exm', 'http://pymc-devs.github.io/pymc/tutorial.html')
        if PyMC.upper() == 'I':
            PyMC_info.AllLibs_install()
            again_1()

        elif PyMC.upper() == 'D':
            PyMC_info.AllLibs_dec()
            again_1()

        elif PyMC.upper() == 'E':
            PyMC_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # fuzzywuzzy
    elif other_list == 34:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/')
        print()
        fuzzywuzzy = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        fuzzywuzzy_info = libraries.all_libraries('fuzzywuzzy', 'other', 'fuzzywuzzy_dec', 'fuzzywuzzy_exm', 'https://github.com/seatgeek/fuzzywuzzy#usage')
        if fuzzywuzzy.upper() == 'I':
            fuzzywuzzy_info.AllLibs_install()
            again_1()

        elif fuzzywuzzy.upper() == 'D':
            fuzzywuzzy_info.AllLibs_dec()
            again_1()

        elif fuzzywuzzy.upper() == 'E':
            fuzzywuzzy_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()

    # progressbar
    elif other_list == 35:
        print(Fore.LIGHTMAGENTA_EX + "For Installation type 'I', Description 'D', Example 'E'.")
        print(Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://progressbar-2.readthedocs.io/en/latest/')
        print()
        progressbar = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        progressbar_info = libraries.all_libraries('progressbar2', 'other', 'progressbar_dec', 'progressbar_exm', 'https://progressbar-2.readthedocs.io/en/latest/#usage')
        if progressbar.upper() == 'I':
            progressbar_info.AllLibs_install()
            again_1()

        elif progressbar.upper() == 'D':
            progressbar_info.AllLibs_dec()
            again_1()

        elif progressbar.upper() == 'E':
            progressbar_info.AllLibs_exm()
            again_1()

        else:
            print(Fore.LIGHTRED_EX + '[!] Wrong Value')
            again_1()


    # Main Menu
    elif other_list == 99:
        system('clear')
        start()
    
    elif other_list == 100:
        system('clear')
        update()

    elif other_list == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')
        close_time()

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()

# Books
def Books_func():
    print(random_color [0] + """    
            .-'''-.        .-'''-.                            
           '   _    \     '   _    \                          
/|       /   /` '.   \  /   /` '.   \     .                   
||      .   |     \  ' .   |     \  '   .'|                   
||      |   '      |  '|   '      |  '.'  |                   
||  __  \    \     / / \    \     / /<    |                   
||/'__ '.`.   ` ..' /   `.   ` ..' /  |   | ____         _    
|:/`  '. '  '-...-'`       '-...-'`   |   | \ .'       .' |   
||     | |                            |   |/  .       .   | / 
||\    / '                            |    /\  \    .'.'| |// 
|/\'..' /                             |   |  \  \ .'.'.-'  /  
'  `'-'`                              '    \  \  \.'   \_.'   
                                     '------'  '---'             
""")
    print()
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
                Books_func()

            except:
                print(Fore.LIGHTRED_EX + 'No Internet !')
                print(Fore.LIGHTGREEN_EX + 'Trying...')
                sleep(3.0)
                PythoninOne()
        PythoninOne()

    elif books == 2:
        print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Python Programming for Beginners.')
        print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
        print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (9.89 MB)')
        def Python_Programming():
            try:
                urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/Python%20Programming%20for%20Beginners.pdf', 'Python Programming for Beginners (PyLe).pdf')
                print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                Books_func()

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
                Books_func()

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
                Books_func()

            except:
                print(Fore.LIGHTRED_EX + 'No Internet !')
                print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                sleep(3.0)
                Blackhat()
        Blackhat()
        

    elif books == 5:
        print(Fore.LIGHTGREEN_EX + '[*]' + Fore.LIGHTCYAN_EX + ' You Choose Mastering Machine Learning with Python in Six Steps.')
        print(Fore.WHITE + '[#]' + Fore.LIGHTGREEN_EX + ' Well, Plese Wait' + Fore.LIGHTGREEN_EX + '...')
        print(Fore.RED + '[~]' + Fore.LIGHTMAGENTA_EX + ' Downloading...' + Fore.YELLOW + ' (9.60 MB)')
        def MasteringMachine():
            try:
                urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/Mastering%20Machine%20Learning%20with%20Python%20in%20Six%20Steps.pdf', "Mastering Machine Learning with Python in Six Steps (PyLe).pdf")
                print(Fore.LIGHTRED_EX + '[!]' + ' Done !')
                sleep(1.0)
                system('clear')
                Books_func()

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
                Books_func()

            except:
                print(Fore.LIGHTRED_EX + 'No Internet !')
                print(Fore.LIGHTGREEN_EX + '[#] Trying...')
                sleep(3.0)
                Automate()
        Automate()

    elif books == 1000:
        system('clear')
        contact()
        again_1()

    elif books == 100:
        system('clear')
        update()

    elif books == 99:
        system('clear')
        start()

    elif books == 0:
        print(Fore.YELLOW+'[-]──# Se You Later :)')
        close_time()

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

    whs_python = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
    if whs_python == 1:
        print()
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://www.python.org/')
        print()
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        print(Fore.WHITE + json.loads( data )['what_is_python']['whs_py'])
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        again_1()

    elif whs_python == 2:
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://en.wikipedia.org/wiki/Python_(programming_language)#History')
        print()
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        print(Fore.WHITE + json.loads( data )['what_is_python']['woh_wrote'])
        print(Fore.LIGHTMAGENTA_EX + '{--------------}')
        again_1()

    elif whs_python == 3:
        print (Fore.YELLOW + 'Pay attention' + Fore.WHITE + ' For More Details =>' + Fore.BLUE + ' https://en.wikipedia.org/wiki/Python_(programming_language)#History')
        print()
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
        close_time()

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
    
    apps_var = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
    # download Python 3
    if apps_var == 1:
        system('clear')
        print(Fore.LIGHTYELLOW_EX + '[#]' + Fore.LIGHTMAGENTA_EX + 'Windows,Unix|Linux,Mac (W/U/M)')
        print()
        py3 = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if py3.upper() == 'W':
            print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
            py3WV = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
            py3M = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
        py2 = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
        if py2.upper() == 'W':
            print(Fore.LIGHTBLUE_EX + 'Which one ? 32bit, 64bit (32/64)')
            py2WV = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
        atom = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
        notepad = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
        sublime = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
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
        close_time()
    
    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()
    

# GUI Ver
def gui_ver():
    print(Fore.LIGHTCYAN_EX + '~> This is GUI Version of PyLe v2.0 .')
    print(Fore.LIGHTGREEN_EX + '~> If there is any bug, please Let me know about it.')
    print(Fore.LIGHTYELLOW_EX + '~> Now Choose, Download Exe File, Download Python Source or Both. (E/P/B/ exit)')
    print()
    gui_pyle = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
    if gui_pyle.upper() == 'E':
        print(Fore.LIGHTMAGENTA_EX + '~> Ok, Downloading please Wait... (Exe File)')
        try:
            urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/apps/PyLeGUI/PyLeGUI2.0.zip', 'PyLeGUI2.0.zip')
            print(Fore.LIGHTBLUE_EX + 'Done !')
            again_1()
        except:
            print(Fore.LIGHTRED_EX + '[!] Connection Lost')
            sleep(1)
            again_1()
    elif gui_pyle.upper() == 'P':
        print(Fore.LIGHTMAGENTA_EX + '~> Ok, Downloading please Wait... (Python Source)')
        try:
            urllib.request.urlretrieve('https://github.com/AnonC0DER/PyLe/raw/main/PyLeGUI/PyLeGUI-2.0(PythonSource).zip', 'PyLeGUI-2.0(PythonSource).zip')
            print(Fore.LIGHTBLUE_EX + 'Done !')
            again_1()
        except:
            print(Fore.LIGHTRED_EX + '[!] Connection Lost')
            sleep(1)
            again_1()
    elif gui_pyle.upper() == 'B':
        print(Fore.LIGHTMAGENTA_EX + '~> Ok, Downloading please Wait... (Exe File)')
        try:
            urllib.request.urlretrieve('https://pyle-pythonlearning.ir/downloads/apps/PyLeGUI/PyLeGUI2.0.zip', 'PyLeGUI2.0.zip')
            print(Fore.LIGHTBLUE_EX + 'Exe File Downloaded, wait for Python Source...')
            urllib.request.urlretrieve('https://github.com/AnonC0DER/PyLe/raw/main/PyLeGUI/PyLeGUI-2.0(PythonSource).zip', 'PyLeGUI-2.0(PythonSource).zip')
            print(Fore.LIGHTGREEN_EX + 'Download Completed !')
            again_1()
        except:
            print(Fore.LIGHTRED_EX + '[!] Connection Lost')
            sleep(1)
            again_1()
    
    elif gui_pyle.lower() == 'exit':
        print(Fore.LIGHTCYAN_EX + '#___GOOD___LUCK___#')

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


# Send Email
def Feedback():
    print(random_color [0] + '''
 _______  _______  _______  ______   ______   _______  _______  _       
(  ____ \(  ____ \(  ____ \(  __  \ (  ___ \ (  ___  )(  ____ \| \    /\\
| (    \/| (    \/| (    \/| (  \  )| (   ) )| (   ) || (    \/|  \  / /
| (__    | (__    | (__    | |   ) || (__/ / | (___) || |      |  (_/ / 
|  __)   |  __)   |  __)   | |   | ||  __ (  |  ___  || |      |   _ (  
| (      | (      | (      | |   ) || (  \ \ | (   ) || |      |  ( \ \ 
| )      | (____/\| (____/\| (__/  )| )___) )| )   ( || (____/\|  /  \ \\
|/       (_______/(_______/(______/ |/ \___/ |/     \|(_______/|_/    \/
                                                                                                                                               
    ''')
    print()
    print(Fore.LIGHTMAGENTA_EX + 'Here, You can send Feedback and bug reports for me.')
    print(Fore.LIGHTGREEN_EX + 'There are two way for sending emails, Send Email with your own Email Address or with PyLeSend-Emails Address.')
    print(Fore.LIGHTWHITE_EX + 'Send Email with your own account Or Send Email with PyLeSend-Emails account')
    print('(Your Own Account : O / PyLeSend-Emails : P / Main Menu : M)')
    print()
    mails_varible = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
    
    # Send Email With user's account
    if mails_varible.upper() == 'O':
        print(Fore.LIGHTWHITE_EX + 'If you wanna send email with your own email address,')
        print(Fore.LIGHTRED_EX + 'You have to > Allow less secure apps: ON')
        print(Fore.LIGHTMAGENTA_EX + 'You can make turn On it with this link : ' + Fore.LIGHTCYAN_EX + 'https://myaccount.google.com/lesssecureapps')
        # get email address, password and message
        print()
        email_address = input(Fore.LIGHTGREEN_EX + 'After turning On it, Give Your Email Address : ')
        if '@' not in email_address:
            print(Fore.LIGHTRED_EX + '[!] Wrong Email Address')
            sleep(1.3)
            system('clear')
            Feedback()

        else:    
            email_password = input(Fore.LIGHTMAGENTA_EX + 'Now, Enter your Password : ')
            user_message = input(Fore.LIGHTYELLOW_EX + 'Message : ')
            send_Message = Emails.yourOwn_email(email_address, email_password, user_message)
            try :
                send_Message.send_email()
                print(Fore.LIGHTGREEN_EX + 'Done !')
                print()
                again_1()

            except:
                print(Fore.LIGHTRED_EX + '''
    Something Went Wrong !
    Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)
                ''')
                again_1()
        

    # Send Email with PyLeSend-Emails account
    elif mails_varible.upper() == 'P':
        print(Fore.LIGHTCYAN_EX + 'Well, Enter Your Message')
        print()
        message_PyLeEmail = input(Fore.LIGHTWHITE_EX + 'Message : ')
        Message_sender = Emails.withPyLe_email(message_PyLeEmail)
        try:
            Message_sender.send_PyLeEmail()
            print(Fore.LIGHTGREEN_EX + 'Done !')
            print()
            again_1()

        except:
            print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)
            ''')
            again_1()
        
    
    elif mails_varible.upper() == 'M':
        start()

    else:
        print(Fore.RED + '[!] Wrong Value')
        again_1()


#Update
def update():
    print(Fore.RED + '[#]' + Fore.WHITE + ' This is 4.0 version')
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


# Show License
def License():
    print(random_color [0] + '''
        GNU GENERAL PUBLIC LICENSE
           Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

More Details = https://github.com/AnonC0DER/PyLe/blob/main/LICENSE
            ''')


# Search
def Search():
    print(random_color [0] + '''
 ,-.                  .     
(   `                 |     
 `-.  ,-. ,-: ;-. ,-. |-.   
.   ) |-' | | |   |   | |   
 `-'  `-' `-` '   `-' ' '   
        ''')

    print()
    print(Fore.LIGHTGREEN_EX + 'You can search for libraries here.')
    FirstValue = input(Fore.LIGHTCYAN_EX + 'Enter your library name (For Main Menu (M)) : ')
    if FirstValue.upper() == 'M':
        print()
        start()

    elif len(FirstValue) <= 0:
        print(Fore.LIGHTRED_EX + '[!] Wrong Value')
        print()
        again_1()

    else:
        SendValue = search.Search(FirstValue)
        SendValue.search()
        again_1()


# Close time
def close_time():
    now = datetime.now()
    print()
    print(Fore.LIGHTGREEN_EX + 'Quit time -> ' + Fore.LIGHTCYAN_EX + now.strftime("%m/%d/%Y %H:%M:%S"))
    print()

#start
def start():
    system('clear')
    # for faster working, PyLe will type if it was the first time runing program 
    # (First Time you run script, you will see typing)
    try:
        f = open('database/First.json', 'r')
        Data = f.read()
        f.close()
    # if script couldn't find First.json     
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + '''
Error !
Can not Find 'First.json' File
            ''')    
    # Start    
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
| Version 4.0 |
 -------------
 ~~~~~~~~~~~~~~~~~~~~~~~~~
| PyLe-PythonLearning.ir  |
 ~~~~~~~~~~~~~~~~~~~~~~~~~
 =================================
| Telegram : @PyLe_PythonLearning |
 =================================
''')

    # If the program was first run
    FirstTime_data = json.loads( Data )['FirstTime']
    if FirstTime_data == 'True':
        # Typing...
        typer_oop = typer.text_type('[$] Learn Python Libraries by a Python script.')
        typer_oop.printer()
        # change data in First.json
        Data = {'FirstTime' : 'False'}
        with open('database/First.json', 'w') as outfile:
            json.dump(Data, outfile)

    # If it wasn't the first time PyLe was run
    elif FirstTime_data == 'False':
        # dosen't type
        print(random_color [0] + '[$] Learn Python Libraries by a Python script.')

    # Continue the Program
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' PyLe helps you know new python libraries.')
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' The first Python script to help you progress in Python.')
    print (Fore.RED + '[$]' + Fore.LIGHTCYAN_EX+ " So, Let's Start !")

    print (random_color [0] +'''
01011011001101001110110011010100101110011010011001100
1  print('Libraries')                               1
1        [1] > Colors                               0
0        [2] > Machine Learning & DataAnalysis      1
1        [3] > Telegram Robots                      1
0        [4] > Game Development                     0
0        [5] > File & Text Encryption               1
1        [6] > Python SQL Libraries                 0
0        [7] > Other                                1
1                                                   0
0        [19] ~> Search (Search in Libraries)       1
0                                                   0
1  echo "Biginners & Professionals";                1                              
1        [10] ~> What Is Python ?                   0    
1        [11] ~> Apps                               0
0                                                   1
1  cout << "Tutorials" << endl;                     0
0         [90] >> Books                             0
1         [91] >> Free Courses                      1                                                            
1                                                   0                                                    
0  [20] ~> GUI Version Of PyLe                      1                                                   
1  [100] ~> Update                                  1
0  [110] ~> Feedback                                0  
0  [1000] ~> About & Contact                        1
1  [1001] ~> License                                0
1  [0] Exit                                         1
0                                                   0
10110110100110010010101001101101101001100010010100101''')

    print()
    try:
        pyle_start = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')) 

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
        
        elif pyle_start == 7:
            system('clear')
            other()

        elif pyle_start == 10:
            system('clear')
            wip()

        elif pyle_start == 11:
            system('clear')
            apps()
        
        elif pyle_start == 19:
            system('clear')
            Search()

        elif pyle_start == 20:
            system('clear')
            gui_ver()

        elif pyle_start == 1000:
            system('clear')
            contact()
            again_1()

        elif pyle_start == 1001:
            system('clear')
            License()
            again_1()

        elif pyle_start == 100:
            system('clear')
            update()
        
        elif pyle_start == 110:
            system('clear')
            Feedback()

        elif pyle_start == 90:
            system('clear')
            Books_func()
        
        elif pyle_start == 91:
            system('clear')
            Courses.FreeCourses()

        elif pyle_start == 0:
            print(Fore.YELLOW+'[-]──# Se You Later :)')
            close_time()

        else:
            print(Fore.RED+'[!]──# Wrong Value')
            again_1()
    
    except:
        print(Fore.RED+'[!]──# Wrong Value')
        again_1()

start()
#################################
# <------CoDed By AnonCODER------>
# <------v4.0----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>
