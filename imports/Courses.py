# <------CoDed By AnonCODER------>
# <------v3.0----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>
##################################################################

# imports
import random
import urllib.request
from colorama import Fore
from time import sleep
from os import system

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

# FreeCourses
def FreeCourses():
    '''
    FreeCourses function
    English and Persian YouTube FreeCourses
    If You Wanna Copy this videos in your projects, Please put their YouTube Accounts in Your Project
    Good Luck everyone :)
    '''
    system('clear')
    print(random_color [0] + '''
███████ ██████  ███████ ███████      ██████  ██████  ██    ██ ██████  ███████ ███████ ███████ 
██      ██   ██ ██      ██          ██      ██    ██ ██    ██ ██   ██ ██      ██      ██      
█████   ██████  █████   █████       ██      ██    ██ ██    ██ ██████  ███████ █████   ███████ 
██      ██   ██ ██      ██          ██      ██    ██ ██    ██ ██   ██      ██ ██           ██ 
██      ██   ██ ███████ ███████      ██████  ██████   ██████  ██   ██ ███████ ███████ ███████ 
''')

    print(Fore.LIGHTGREEN_EX + '[+]' + Fore.LIGHTMAGENTA_EX + ' You can see Download and see Free YouTube Courses.')
    print(Fore.LIGHTRED_EX + '[~] Pay Attention' + Fore.LIGHTCYAN_EX+ ' To support free tutoring teachers, subscribe to their YouTube account.')
    print(Fore.LIGHTWHITE_EX + '[*]' + Fore.LIGHTYELLOW_EX + ' First choose your language for Courses (-Persian (P), English(E), Exit(exit)-)')
    print()

    courses = input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ ')
    if courses.upper() == 'P':
        print(Fore.LIGHTMAGENTA_EX + '''
1 = Make A Simple Python Keylogger*
2 = WhatsApp Bot With Python *
3 = Write a simple RAT with Python*
4 = Complete tutorial on making a floppy bird game with Pygame
5 = The best programming tools, install Python on Linux and Windows
6 = Learn how to convert a Python program to an exe file
7 = Random Number in Python
8 = Get a WiFi password with Python

100 => FreeCourses Menu
        ''')
        persian_courses = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
        # Make A Simple Python Keylogger
        if persian_courses == 1:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to make a useful Keylogger with python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Qadir Yolme  |  Size : 273Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/channel/UCO8iviFPYxykxTG1M7XdMKw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/XUkRU5zE04w')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/qadir_yolme_Keylogger.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            download_Keylogger = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if download_Keylogger.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try :
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/qadir_yolme_Keylogger.mp4', 'qadir_yolme_Keylogger.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()
                    
            elif download_Keylogger.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()

        # WhatsApp Bot With Python
        elif persian_courses == 2:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to make a WhatsApp Bot With Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : Part1 = 62Mb / Part2 = 58Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/c/Nabegheha")
            print(Fore.LIGHTWHITE_EX + 'Video Links (2 Part) => p1 = (https://youtu.be/VLxnPdJS1HE) / p2 = (https://youtu.be/hgwTZfw7ciY)')
            print(Fore.LIGHTBLUE_EX + 'Direct download link (part 1) : https://dl.pyle-pythonlearning.ir/videos/per/01.WhatsApp_Bot_Using_Python.mp4')
            print(Fore.LIGHTBLUE_EX + 'Direct download link (part 2) : https://dl.pyle-pythonlearning.ir/videos/per/02.WhatsApp_Bot_Using_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            WhatsApp_Bot = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if WhatsApp_Bot.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading... (2 Parts)')
                try :
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/01.WhatsApp_Bot_Using_Python.mp4', '01.WhatsApp_Bot_Using_Python.mp4')
                    print(Fore.LIGHTGREEN_EX + 'Part 1 Downloaded. Downloading... (Part 2)')
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/02.WhatsApp_Bot_Using_Python.mp4', '02.WhatsApp_Bot_Using_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif WhatsApp_Bot.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()

        # Write a simple RAT with Python
        elif persian_courses == 3:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to Write a simple RAT with Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Qadir Yolme  |  Size : 126Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/channel/UCO8iviFPYxykxTG1M7XdMKw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/H55t7Fa-ftQ')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/Write_a_simple_RAT_with_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            RAT_with_Python = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if RAT_with_Python.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/Write_a_simple_RAT_with_Python.mp4', 'Write_a_simple_RAT_with_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif RAT_with_Python.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()

        # Complete tutorial on making a floppy bird game with Pygame
        elif persian_courses == 4:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to make a floppy bird game with Pygame.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : 324Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/c/Nabegheha")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/feFDkcUHA9Y')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/Pygame_Tutorial_floppy_bird.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            floppy_bird = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if floppy_bird.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/Pygame_Tutorial_floppy_bird.mp4', 'Pygame_Tutorial_floppy_bird.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif floppy_bird.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()
            
        # The best programming tools, install Python on Linux and Windows
        elif persian_courses == 5:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to install Python on Linux and Windows and know about the best programming tools.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : 68Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/c/Nabegheha")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/HYr2ic1_5tA')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/best_programming_tools.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            programming_tools = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if programming_tools.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/best_programming_tools.mp4', 'best_programming_tools.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif programming_tools.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()

        # Learn how to convert a Python program to an exe file
        elif persian_courses == 6:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to convert a Python program to an exe file.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : 44Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/c/Nabegheha")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/CkiwlO8kVRI')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/convert_a_Python_program_to_an_exe_file.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            convert_Python = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if convert_Python.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/convert_a_Python_program_to_an_exe_file.mp4', 'convert_a_Python_program_to_an_exe_file.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif convert_Python.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()
        
        # Random Number in Python
        elif persian_courses == 7:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to make Random Numbers in Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : 28Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/c/Nabegheha")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/5O4fSbrKAKA')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/Random_Number_in_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Random_Number = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Random_Number.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/Random_Number_in_Python.mp4', 'Random_Number_in_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Random_Number.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()
        
        # Get a WiFi password with Python
        elif persian_courses == 8:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to make Random Numbers in Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : AmirHossein Moalemi  |  Size : 51Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://youtube.com/channel/UCO8iviFPYxykxTG1M7XdMKw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/5ArbYwhV60Y')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/per/Get_a_WiFi_password_with_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            WiFi_password = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if WiFi_password.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/per/Get_a_WiFi_password_with_Python.mp4', 'Get_a_WiFi_password_with_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif WiFi_password.upper() == 'N':
                sleep(0.5)
                FreeCourses()
            
            else:
                print(Fore.RED + '[!] Wrong Value')
                sleep(1.0)
                FreeCourses()

        # FreeCourses Menu
        elif persian_courses == 100:
            FreeCourses()

    
    elif courses.upper() == 'E':
        print(Fore.LIGHTGREEN_EX + '''
1 = Python NumPy Tutorial for Beginners
2 = Scikit Learn Course Machine Learning in Python Tutorial 
3 = Keras with TensorFlow Course Python Deep Learning
4 = Coding Telegram Bot using Python
5 = How To Create A Telegram Bot With Python
6 = Complete Python Turtle Graphics Overview
7 = Python Game Development Course
8 = Step-by-Step Python and Postgres Tutorial with psycopg2
9 = Matplotlib Crash Course
10 = Learn Python - Full Course for Beginners

100 => FreeCourses Menu
''')

        english_courses = int(input(Fore.LIGHTYELLOW_EX + 'PyLe ~$ '))
        # Python NumPy Tutorial for Beginners
        if english_courses == 1:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn the basics of the NumPy library in this tutorial for beginners.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Keith Galli  |  Size : 85Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/QUT1VHiLmmI')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Python_NumPy_Tutorial_for_Beginners.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            numpy_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if numpy_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Python_NumPy_Tutorial_for_Beginners.mp4', 'Python_NumPy_Tutorial_for_Beginners.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()
                    
            elif numpy_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # Scikit Learn Course Machine Learning in Python Tutorial
        elif english_courses == 2:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn about machine learning using scikit-learn in this full course..')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : freeCodeCamp  |  Size : 279Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/pqNCD_5r0IU')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Scikit_Learn_Course_Machine_Learning_in_Python_Tutorial.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Scikit_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Scikit_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Scikit_Learn_Course_Machine_Learning_in_Python_Tutorial.mp4', 'Scikit_Learn_Course_Machine_Learning_in_Python_Tutorial.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Scikit_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()

        # Keras with TensorFlow Course Python Deep Learning
        elif english_courses == 3:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can learn how to prepare and process data for artificial neural networks, build and train artificial neural networks from scratch, build and train convolutional neural networks.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : freeCodeCamp  |  Size : 266Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/qFJeN9V1ZsI')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Keras_with_TensorFlow_Course_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Keras_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Keras_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Keras_with_TensorFlow_Course_Python.mp4', 'Scikit_Learn_Course_Machine_Learning_in_Python_Tutorial.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Keras_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()

        # Coding Telegram Bot using Python
        elif english_courses == 4:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn Coding Telegram Bot using Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Sumanjay  |  Size : 240Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC_AlIxCSFvOnYw5k6HAKmjg")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/wdiWGmg_IRM')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Coding_Telegram_Bot_using_Python.mkv')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            TelegramBot_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if TelegramBot_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Coding_Telegram_Bot_using_Python.mkv', 'Coding_Telegram_Bot_using_Python.mkv')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif TelegramBot_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # How To Create A Telegram Bot With Python
        elif english_courses == 5:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn how to make a Telegram bot with Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : CS Dojo  |  Size : 93Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UCxX9wt5FWQUAAz4UrysqK9A")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/NwBWW8cNCP4')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/How_To_Create_A_Telegram_Bot_With_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Create_A_TelegramBot_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Create_A_TelegramBot_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/How_To_Create_A_Telegram_Bot_With_Python.mp4', 'How_To_Create_A_Telegram_Bot_With_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Create_A_TelegramBot_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()

        # Complete Python Turtle Graphics Overview
        elif english_courses == 6:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, he walks through the Turtle Graphics library of Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Keith Galli  |  Size : 98Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/pxKu2pQ7ILo')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Complete_Python_Turtle.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Turtle_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Turtle_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Complete_Python_Turtle.mp4', 'Complete_Python_Turtle.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Turtle_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()

        # Python Game Development Course
        elif english_courses == 7:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn how to use Pygame to code games with Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : freeCodeCamp  |  Size : 218Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/FfWpgLFMI7w')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Pygame_Tutorial_for_Beginners_Python.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            GameDevelopment_vide = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if GameDevelopment_vide.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Pygame_Tutorial_for_Beginners_Python.mp4', 'Pygame_Tutorial_for_Beginners_Python.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif GameDevelopment_vide.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # Step-by-Step Python and Postgres Tutorial with psycopg2
        elif english_courses == 8:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you will go through the basic steps on how to write a python script to read and write data on a Postgres database.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Hussein Nasser  |  Size : 38Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC_ML5xP23TOWKUcc-oAE_Eg")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/2PDkXviEMD0')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Step_by_Step_Python_and_Postgres_Tutorial_with_psycopg2.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            StepByStep_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if StepByStep_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Step_by_Step_Python_and_Postgres_Tutorial_with_psycopg2.mp4', 'Step_by_Step_Python_and_Postgres_Tutorial_with_psycopg2.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif StepByStep_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # Matplotlib Crash Course
        elif english_courses == 9:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'In this video, you can Learn the basics of Matplotlib in this crash course tutorial. Matplotlib is an amazing data visualization library for Python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : freeCodeCamp  |  Size : 232Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/3Xc3CA655Y4')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Step_by_Step_Python_and_Postgres_Tutorial_with_psycopg2.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            Matplotlib_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if Matplotlib_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Matplotlib_Crash_Course.mp4', 'Matplotlib_Crash_Course.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif Matplotlib_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # Learn Python - Full Course for Beginners
        elif english_courses == 10:
            system('clear')
            print(Fore.LIGHTGREEN_EX + '[@] ' + Fore.LIGHTCYAN_EX + 'This course will give you a full introduction into all of the core concepts in python.')
            print(Fore.LIGHTYELLOW_EX + '[#] ' + Fore.LIGHTMAGENTA_EX + 'Teacher / Academy : Mike Dane  |  Size : 278Mb')
            print(Fore.LIGHTRED_EX + "To support free tutoring teachers, See and subscribe teachers's YouTube account :")
            print(Fore.LIGHTWHITE_EX + "Teacher's / Academy's Youtube : Account = https://www.youtube.com/channel/UCvmINlrza7JHB1zkIOuXEbw")
            print(Fore.LIGHTWHITE_EX + 'Video Link = https://youtu.be/rfscVS0vtbw')
            print(Fore.LIGHTBLUE_EX + 'Direct download link : https://dl.pyle-pythonlearning.ir/videos/eng/Learn_Python_Full_Course_for_Beginners_Tutorial.mp4')
            print(Fore.LIGHTCYAN_EX + '------------------------------')
            # Download the Video
            LearnPython_video = input(Fore.LIGHTGREEN_EX + 'Do You Wanna Download the video? (Y / N) : ')
            
            if LearnPython_video.upper() == 'Y':
                print(Fore.LIGHTGREEN_EX + 'Please Wait, Downloading...')
                try:
                    urllib.request.urlretrieve('https://dl.pyle-pythonlearning.ir/videos/eng/Learn_Python_Full_Course_for_Beginners_Tutorial.mp4', 'Learn_Python_Full_Course_for_Beginners_Tutorial.mp4')
                    print(Fore.LIGHTMAGENTA_EX + 'Done !')
                    sleep(0.5)
                    FreeCourses()
                # if there is any problems like, No internet connection or server problems :
                except :
                    print(Fore.LIGHTRED_EX + '''
Something Went Wrong !
Error Details : No internet connection, Server problems Or KeyboardInterrupt(Ctrl + C)                    
                    ''')
                    sleep(1.7)
                    FreeCourses()

            elif LearnPython_video.upper() == 'N':
                sleep(0.5)
                FreeCourses()
        
        # FreeCourses Menu
        elif english_courses == 100:
            FreeCourses()


    # Close the script
    elif courses.lower() == 'exit':
        print(Fore.LIGHTCYAN_EX + '- Good Luck :)')
    
    else:
        print(Fore.RED + '[!] Wrong Value')
        sleep(1.0)
        FreeCourses()

##################################
# <------CoDed By AnonCODER------>
# <------v3.0----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>
