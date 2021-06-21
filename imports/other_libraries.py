from colorama import Fore
import json

# Open The json Data 
fp = open('database/data.json', 'r')
data = fp.read()
fp.close()
# Machine Learning Classes
class machinlearning_class():

    def scikit_install():
        print ('')
        print(Fore.YELLOW + '<---Installation--->')
        print (Fore.WHITE + 'pip install scikit-learn')
        print(Fore.YELLOW + '<---Installation--->') 
        print('')
    
    def scikit_dec():
        print('')
        print(Fore.YELLOW + '<---Description--->')
        print (Fore.WHITE + json.loads( data )['Machin_Learning']['scikit_dec']) 
        print('')
        print (Fore.RED + json.loads( data )['Machin_Learning']['scikit_req']) 
        print(Fore.YELLOW + '<---Description--->')
        print('')
    
    # pycaret
    def pycaret_install():
        print()
        print(Fore.YELLOW + '<---Installation--->')
        print(Fore.WHITE + 'pip install pycaret')
        print(Fore.YELLOW + '<---Installation--->')
        print()
    
    def pycaret_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads(data)['Machin_Learning']['PyCaret_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def pycaret_exm1():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://pycaret.org/functions/')
        print(Fore.WHITE + json.loads(data)['Machin_Learning']['PyCaret_exm1'])            
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()
        print(Fore.LIGHTGREEN_EX + 'There is another example do you wanna see it too? (Y/N)')

    def pycaret_exm2():
        print()
        print(Fore.YELLOW + '<---Example2--->')
        print(Fore.WHITE + json.loads(data)['Machin_Learning']['PyCaret_exm2'])
        print()
        print(Fore.YELLOW + '<---Example2--->')
        print()


# Telegram Bots
class telegrambots_class():

    def Pyrogram_install():
        print ('')
        print(Fore.YELLOW + '<---Installation--->')
        print (Fore.WHITE + 'pip install Pyrogram')
        print(Fore.YELLOW + '<---Installation--->') 
        print('') 
    
    def Pyrogram_dec():
        print('')
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['Telegram_bots']['pyrogram_dec'])
        print(Fore.RED + json.loads( data )['Telegram_bots']['pyrogram_req'])
        print('')
        print(Fore.YELLOW + '<---Description--->')
        print('')
    
    def Pyrogram_exm():
        print('')
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.pyrogram.org/start/examples/')
        print(Fore.WHITE + json.loads( data )['Telegram_bots']['pyrogram_exm'])
        print('')
        print(Fore.YELLOW + '<---Example--->')
        print('')


# Other Class for other libraries, that i can't use libraries.py for them
class other_class():
        
    def Os_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['Os_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()

    def Os_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://www.tutorialsteacher.com/python/os-module')
        print(Fore.WHITE + json.loads( data )['other']['Os_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()

    # subprocess
    def subprocess_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['subprocess_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def subprocess_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://queirozf.com/entries/python-3-subprocess-examples')
        print(Fore.WHITE + json.loads( data )['other']['subprocess_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()

    # UrllibRequest
    def UrllibRequest_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['urllib_request_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def UrllibRequest_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.python.org/3/library/urllib.request.html#examples')
        print(Fore.WHITE + json.loads( data )['other']['urllib_request_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()

    
    # Tkinter
    def Tkinter_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['Tkinter_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def Tkinter_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program')
        print(Fore.WHITE + json.loads( data )['other']['Tkinter_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()


    # PyQt
    def PyQt5_installtion():
        print ('')
        print(Fore.YELLOW + '<---Installation--->')
        print(Fore.LIGHTGREEN_EX + 'PyQt5 :')
        print(Fore.WHITE + 'pip install PyQt5')
        print()
        print(Fore.LIGHTGREEN_EX + 'PyQt6 :')
        print(Fore.WHITE + 'pip install PyQt6')
        print(Fore.YELLOW + '<---Installation--->') 
        print()
    
    def PyQt5_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['PyQt_dec'])
        print(Fore.LIGHTRED_EX + 'PyQt4 and Qt v4 are no longer supported and no new releases will be made.')
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def PyQt5_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://www.riverbankcomputing.com/static/Docs/PyQt5/')
        print(Fore.WHITE + json.loads( data )['other']['PyQt_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()
    
    
    # datetime
    def datetime_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['Datetime_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def datetime_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta')
        print(Fore.WHITE + json.loads( data )['other']['Datetime_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()
    
    # Json
    def JSON_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['JSON_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()

    def JSON_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.python.org/3/library/json.html#basic-usage')
        print(Fore.WHITE + json.loads( data )['other']['JSON_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()
    
    # Sys
    def Sys_dec():
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )['other']['Sys_dec'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()

    def Sys_exm():
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + 'More Details : https://docs.python.org/3/library/sysconfig.html')
        print(Fore.WHITE + json.loads( data )['other']['Sys_exm'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()


