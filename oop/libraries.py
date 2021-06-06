# <------CoDed By AnonCODER------>
# <------v2.5----->
# <------Help me improve it :)------>

from colorama import Fore
import json

# Open json data here
fp = open('database/data.json', 'r')
data = fp.read()
fp.close()

# All libraries :)
class all_libraries():

    def __init__(self, install, lib, dec, exam, exam_site):
        self.install = install
        self.lib = lib
        self.dec = dec
        self.exam = exam
        self.exam_site = exam_site

    def AllLibs_install(self):
        print()
        print(Fore.YELLOW + '<---Installation--->')
        print(Fore.WHITE + f'pip install {self.install}')
        print(Fore.YELLOW + '<---Installation--->') 
        print()
    
    def AllLibs_dec(self):
        print()
        print(Fore.YELLOW + '<---Description--->')
        print(Fore.WHITE + json.loads( data )[f'{self.lib}'][f'{self.dec}'])
        print()
        print(Fore.YELLOW + '<---Description--->')
        print()
    
    def AllLibs_exm(self):
        print()
        print(Fore.YELLOW + '<---Example--->')
        print(Fore.CYAN + f'More Details : {self.exam_site}')
        print(Fore.WHITE + json.loads( data )[f'{self.lib}'][f'{self.exam}'])
        print()
        print(Fore.YELLOW + '<---Example--->')
        print()


# <------CoDed By AnonCODER------>
# <------v2.5----->
# <------Help me improve it :)------>
