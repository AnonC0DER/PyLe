# <------CoDed By AnonCODER------>
# <------First Version : v1.0------>
# <------Help me improve it :)------>


#imports
from os import system
from colorama import Fore
from time import sleep
import random
import urllib.request

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


#Colors menu
def colors_menu():
    pass


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
            print (Fore.WHITE + '''
Very simple Python library for color and formatting in terminal. 
Collection of color codes and names for 256 color terminal setups. 
The following is a list of 256 colors for Xterm, containing an example of the displayed color, Xterm Name, Xterm Number and HEX.
            ''') 
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif colord.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + '''
How to use the module in your own python code:

>>> from colored import fg, bg, attr
>>>
>>> print ('%s Hello World !!! %s' % (fg(1), attr(0)))
 Hello World !!!
>>>
>>> print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(0)))
 Hello World !!!
Use description:

>>> print ('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))
 Hello World !!!
>>>
>>> print ('%s%s Hello World !!! %s' % (fg('orchid'), attr('bold'), attr('reset')))
 Hello World !!!
>>>
>>> color = bg('indian_red_1a') + fg('white')
>>> reset = attr('reset')
>>> print (color + 'Hello World !!!' + reset)
Hello World !!!
Or use HEX code:

>>> color = fg('#C0C0C0') + bg('#00005f')
>>> res = attr('reset')
>>> print (color + "Hello World !!!" + res)
Hello World !!!
            ''')          
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
            print (Fore.WHITE + '''
ANSI escape character sequences have long been used to produce colored terminal text and cursor positioning on Unix and Macs. 
Colorama makes this work on Windows, too, by wrapping stdout, stripping ANSI sequences it finds (which would appear as gobbledygook in the output), and converting them into the appropriate win32 calls to modify the state of the terminal. On other platforms, Colorama does nothing.
This has the upshot of providing a simple cross-platform API for printing colored terminal text from Python, and has the happy side-effect that existing applications or libraries which use ANSI sequences to produce colored output on Linux or Macs can now also work on Windows, simply by calling colorama.init()
An alternative approach is to install ansi.sys on Windows machines, which provides the same behaviour for all applications running in terminals. 
Colorama is intended for situations where that isn’t easy (e.g., maybe your app doesn’t have an installer.)
''') 
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif colorma.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + '''
Colored Output
Cross-platform printing of colored text can then be done using Colorama’s constant shorthand for ANSI escape sequences:

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

…or, Colorama can be used in conjunction with existing ANSI libraries such as the venerable Termcolor or the fabulous Blessings. This is highly recommended for anything more than trivial coloring:

from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))''')
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
            print (Fore.WHITE + 'Termcolor is a python module for ANSII Color formatting for output in terminal.') 
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif termcolor.upper() == 'E':
           print('')
           print(Fore.YELLOW + '<---Example--->')
           print (Fore.WHITE + '''
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)''')
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
            print (Fore.WHITE + '''
Scikit-learn is a Python module for machine learning built on top of SciPy and is distributed under the 3-Clause BSD license.
The project was started in 2007 by David Cournapeau as a Google Summer of Code project, and since then many volunteers have contributed.
See the About us page for a list of core contributors.
It is currently maintained by a team of volunteers.''')
            print('')
            print(Fore.GREEN + '''
Scikit-learn requires:

. Python (>= 3.6)
. NumPy (>= 1.13.3)
. SciPy (>= 0.19.1)
. joblib (>= 0.11)
. threadpoolctl (>= 2.0.0)''')
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
            print (Fore.WHITE + '''
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. 
It was developed with a focus on enabling fast experimentation. 
Being able to go from idea to result as fast as possible is key to doing good research.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif keras.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://keras.io/examples/')
            print(Fore.WHITE + '''
Setup
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers
Prepare the dataset
In this example, we will be using the FashionMNIST dataset. But this same recipe can be used for other classification datasets as well.

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_train = np.reshape(x_train, (-1, 28, 28, 1))
y_train = tf.one_hot(y_train, 10)

x_test = x_test.astype("float32") / 255.0
x_test = np.reshape(x_test, (-1, 28, 28, 1))
y_test = tf.one_hot(y_test, 10)
Define hyperparameters
AUTO = tf.data.AUTOTUNE
BATCH_SIZE = 64
EPOCHS = 10
Convert the data into TensorFlow Dataset objects
# Put aside a few samples to create our validation set
val_samples = 2000
x_val, y_val = x_train[:val_samples], y_train[:val_samples]
new_x_train, new_y_train = x_train[val_samples:], y_train[val_samples:]

train_ds_one = (
    tf.data.Dataset.from_tensor_slices((new_x_train, new_y_train))
    .shuffle(BATCH_SIZE * 100)
    .batch(BATCH_SIZE)
)
train_ds_two = (
    tf.data.Dataset.from_tensor_slices((new_x_train, new_y_train))
    .shuffle(BATCH_SIZE * 100)
    .batch(BATCH_SIZE)
)
# Because we will be mixing up the images and their corresponding labels, we will be
# combining two shuffled datasets from the same training data.
train_ds = tf.data.Dataset.zip((train_ds_one, train_ds_two))

val_ds = tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(BATCH_SIZE)

test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(BATCH_SIZE)''')

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
            print (Fore.WHITE + '''
That XGBoost is a library for developing fast and high performance gradient boosting tree models. 
That XGBoost is achieving the best performance on a range of difficult machine learning tasks.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif xgboost.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://xgboost.readthedocs.io/en/latest/tutorials/input_format.html')
            print(Fore.WHITE + '''
# First XGBoost model for Pima Indians dataset
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# load data
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
''')

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
            print (Fore.WHITE + '''
Statsmodels is a Python package that provides a complement to scipy for statistical computations 
including descriptive statistics and estimation and inference for statistical models.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif statsmodels.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.statsmodels.org/stable/' + Fore.GREEN + ' &  https://datatofish.com/statsmodels-linear-regression/')
            print(Fore.WHITE + '''
The Python Code using Statsmodels
The following Python code includes an example of Multiple Linear Regression, where the input variables are:

Interest_Rate
Unemployment_Rate
These two variables are used in the prediction of the dependent variable of Stock_Index_Price.

Here is the complete syntax to perform the linear regression in Python using statsmodels (for larger datasets, you may consider to import your data):

from pandas import DataFrame
import statsmodels.api as sm

Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
                }

df = DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price']) 

X = df[['Interest_Rate','Unemployment_Rate']] # here we have 2 variables for the multiple linear regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example
Y = df['Stock_Index_Price']

X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 

print_model = model.summary()
print(print_model)
''')
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
            print (Fore.WHITE + '''
TensorFlow is an open source software library for high performance numerical computation. 
Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), 
and from desktops to clusters of servers to mobile and edge devices.
Originally developed by researchers and engineers from the Google Brain team within Google's AI organization, 
it comes with strong support for machine learning and deep learning and the flexible numerical computation core is used across many other scientific domains.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif tensorflow.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://rubikscode.net/2018/02/05/introduction-to-tensorflow-with-python-example/')
            print(Fore.WHITE + '''
Example :
In the code below, we defined two constant tensors and add one value to another:

import tensorflow as tf

const1 = tf.constant([[1,2,3], [1,2,3]]);
const2 = tf.constant([[3,4,5], [3,4,5]]);

result = tf.add(const1, const2);

with tf.Session() as sess:
  output = sess.run(result)
  print(output)
''')

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
      print (Fore.WHITE + '''
This library provides a pure Python interface for the Telegram Bot API. It’s compatible with Python versions 3.6+. PTB might also work on PyPy, though there have been a lot of issues before. Hence, PyPy is not officially supported.

In addition to the pure API implementation, this library features a number of high-level classes to make the development of bots easy and straightforward. These classes are contained in the telegram.ext submodule.''')
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()

    elif python_telegram_bot.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.CYAN + 'More Details : https://python-telegram-bot.readthedocs.io/en/stable/')
      print(Fore.WHITE + '''
                  
This library uses the logging module. To set up logging to standard output, put:

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
at the beginning of your script.

You can also use logs in your application by calling logging.getLogger() and setting the log level you want:

logger = logging.getLogger()
logger.setLevel(logging.INFO)
If you want DEBUG logs instead:

logger.setLevel(logging.DEBUG)''')

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
      print (Fore.WHITE + '''
Pyrogram is a modern, elegant and easy-to-use Telegram client library framework written from the ground up in Python and C. It enables you to easily create custom Telegram client applications for both user and bot identities (bot API alternative) via the MTProto API.''')
      print('''
Requirements

-Python 3.6 or higher.
-A Telegram API key.''')
      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()
      
    elif pyrogram.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.CYAN + 'More Details : https://docs.pyrogram.org/start/examples/')
      print(Fore.WHITE + '''
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")


app.run()''')

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
      print (Fore.WHITE + '''
An async API wrapper for Telegram bot API in Python
Python 3.7+ is required to install and use telegram.py''')

      print('')
      print(Fore.YELLOW + '<---Description--->')
      print('')
      again_1()
      
    elif pyrogram.upper() == 'E':
      print('')
      print(Fore.YELLOW + '<---Example--->')
      print(Fore.WHITE + '''
import logging

import telegrampy
from telegrampy.ext import commands

logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s", datefmt="%m/%d/%y - %H:%M:%S %Z")
logger = logging.getLogger("telegrampy")

bot = commands.Bot("token here")

@bot.command()
async def hi(ctx):
    await ctx.send("Hello")

bot.run()''')

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
            print (Fore.WHITE + '''
Pygame is a free and open-source cross-platform library for the development of multimedia applications
like video games using Python. It uses the Simple DirectMedia Layer library and
several other popular libraries to abstract the most common functions, 
making writing these programs a more intuitive task.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pygame.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.pygame.org/docs/ref/examples.html')
            print(Fore.WHITE + '''
# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()''')

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
            print (Fore.WHITE + '''
Turtle graphics is a popular way for introducing programming to kids. 
It was part of the original Logo programming language developed by Wally Feurzeig, 
Seymour Papert and Cynthia Solomon in 1967.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif turtles.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://michael0x2a.com/blog/turtle-examples')
            print(Fore.WHITE + '''
                  
import turtle 

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()''')

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
            print (Fore.WHITE + '''
PyOpenGL is the most common cross platform Python binding to OpenGL and related APIs. 
The binding is created using the standard ctypes library, 
and is provided under an extremely liberal BSD-style Open-Source license.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pyopengl.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://noobtuts.com/python/opengl-introduction')
            print(Fore.WHITE + '''
                  
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400                               # window size

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
   
    # ToDo draw rectangle
   
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything''')

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
            print (Fore.WHITE + '''
Cryptography is a package which provides cryptographic recipes and primitives to Python developers. 
Our goal is for it to be your “cryptographic standard library”. 
It supports Python 3.6+ and PyPy3 7.2+.
Cryptography includes both high level recipes and low level interfaces to common cryptographic 
algorithms such as symmetric ciphers, message digests, 
and key derivation functions.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif cryptography.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://cryptography.io/en/latest/')
            print(Fore.WHITE + '''
>>> from cryptography.fernet import Fernet
>>> # Put this somewhere safe!
>>> key = Fernet.generate_key()
>>> f = Fernet(key)
>>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
>>> token
b'...'
>>> f.decrypt(token)
b'A really secret message. Not for prying eyes.' ''')

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
            print (Fore.WHITE + '''
This is a collection of both secure hash functions (such as SHA256 and RIPEMD160), 
and various encryption algorithms (AES, DES, RSA, ElGamal, etc.). 
The package is structured to make adding new modules easy. This section is essentially complete, 
and the software interface will almost certainly not change in an incompatible way in the future; 
all that remains to be done is to fix any bugs that show up.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pycrypto.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.dlitz.net/software/pycrypto/')
            print(Fore.WHITE + '''
>>> from Crypto.Cipher import AES
>>> obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> message = "The answer is no"
>>> ciphertext = obj.encrypt(message)
>>> obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> obj2.decrypt(ciphertext)
'The answer is no'' ''')
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
            print (Fore.WHITE + '''
pyAesCrypt is a Python 3 file-encryption module and script that 
uses AES256-CBC to encrypt/decrypt files and binary streams.
pyAesCrypt is compatible with the AES Crypt file format (version 2).
It is Free Software, released under the Apache License, Version 2.0.
pyAesCrypt is brought to you by Marco Bellaccini - marco.bellaccini(at!)gmail.com.
IMPORTANT SECURITY NOTE: version 2 of the AES Crypt file format does not authenticate the “file size modulo 16” byte. 
This implies that an attacker with write access to the encrypted file may 
alter the corresponding plaintext file size by up to 15 bytes.
there is no low-level memory management in Python, hence it is not possible to wipe 
memory areas were sensitive information was stored.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif pyaescrypt.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://pypi.org/project/pyAesCrypt/')
            print(Fore.WHITE + '''
import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)''')
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
            print (Fore.WHITE + '''
SQLite is a C library that provides a lightweight disk-based database that doesn’t require 
a separate server process and allows accessing the database using a nonstandard 
variant of the SQL query language. Some applications can use SQLite for internal data storage. 
It’s also possible to prototype an application using SQLite and then port the code 
to a larger database such as PostgreSQL or Oracle.
The sqlite3 module was written by Gerhard Häring. It provides a SQL interface 
compliant with the DB-API 2.0 specification described by PEP 249.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif SQLite.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.tutorialspoint.com/sqlite/sqlite_python.htm')
            print(Fore.WHITE + """
import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()""")
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
            print (Fore.WHITE + '''
MySQL Connector/Python enables Python programs to access MySQL databases, 
using an API that is compliant with the Python Database API Specification v2.0 (PEP 249).''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif MySQL.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://www.w3schools.com/python/python_mysql_select.asp')
            print(Fore.WHITE + '''
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")''')
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
            print (Fore.WHITE + '''
PostgreSQL is one of the most advanced and widely used relational database management systems. 
It's extremely popular for many reasons, a few of which include it being open source, 
its extensibility, and its ability to handle many different types of applications and varying loads.
With Python, you can easily establish a connection to your PostgreSQL database. 
There are many Python drivers for PostgreSQL, with "psycopg" being the most popular one. 
Its current version is psycopg2.
In this article, we'll be discussing how to access a PostgreSQL database 
in Python using the psycopg2 driver.''')
            print('')
            print(Fore.YELLOW + '<---Description--->')
            print('')
            again_1()

        elif postgres.upper() == 'E':
            print('')
            print(Fore.YELLOW + '<---Example--->')
            print(Fore.CYAN + 'More Details : https://stackabuse.com/working-with-postgresql-in-python/')
            print(Fore.WHITE + '''
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="Kaliakakya", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()

cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");

con.commit()
print("Records inserted successfully")
con.close()''')
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


#Update
def update():
    print(Fore.RED + '[#]' + Fore.WHITE + ' This is 1.0 version')
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
|     # Or NoobsFather                       |       
|       # My real name is Hesam              |         
| # if you have any idea for this appliction |
|        # or you wanna talk to me           |
|       # Contact Me : @NoobsFather          |
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
| Version 1.1 |
 -------------
''')

    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' Learn Python Libraries by Python script.')
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' PyLe helps you know new python libraries.')
    print (Fore.YELLOW + '[$]' + Fore.LIGHTCYAN_EX+ ' The first Python script to help you progress in Python.')
    print (Fore.RED + '[$]' + Fore.LIGHTCYAN_EX+ " So, Let's Start !")

    print (Fore.LIGHTYELLOW_EX+'''
{-------------}
[1] > Colors
[2] > Machine Learning
[3] > Telegram Robots
[4] > Game Development
[5] > File & Text Encryption
[6] > Python SQL Libraries

[1000] About Author && Contact Author
[100] Update
[0] Exit
{-------------}''')

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

        elif pyle_start == 1000:
            system('clear')
            contact()
            again_1()

        elif pyle_start == 100:
            system('clear')
            update()

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
# <------First Version : v1.0------>
# <------Help me improve it :)------>
