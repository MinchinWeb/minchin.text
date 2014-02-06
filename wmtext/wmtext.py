'''WMText
v.4.0 - WM - Feb. 6, 2014

This is a helper file, containing formatting helps for creating command line
programs.
'''

import sys
import time
import re

import colorama

re_ansi_control_codes = re.compile(r'\033\[[017](;[034][0-9])*m|\x1b\[[034][0-9]*m') #term colour control codes

def length_no_ansi(mystring):
	'''Takes a string, strips out the ANSI escape codes
	(used for colouring terminal output, etc.), and returns
	the length of the resulting string'''
	newstring = re.sub(re_ansi_control_codes, "", mystring)
	return len(newstring)

def centered (mystring, linewidth=79, fill=" "):
	'''Takes a string, centres it, and pads it on both sides'''
	sides = (linewidth - length_no_ansi(mystring))/2
	sidestring = ""
	for i in range(sides):
		sidestring = sidestring + fill
	newstring = sidestring + mystring + sidestring
	while length_no_ansi(newstring) < linewidth:
		newstring = newstring + " "
	return newstring

def clock_on_right(mystring):
	'''Takes a string, and prints it with the clock right aligned'''
	taken = length_no_ansi(mystring)
	padding = 79 - taken - 5
	clock = time.strftime("%I:%M", time.localtime())
	print mystring + " "*padding + clock
	
def query_yes_no(question, default="yes"):
    '''Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    
	Copied from
	http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input
	'''
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")
							 
def query_yes_no_all(question, default="yes"):
    '''Ask a yes/no/all question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no", "all" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes", "no", or "all".
	'''
    valid = {"yes":1,  "y":1,  "ye":1,
             "no":0,   "n":0,
			 "all":2,  "a":2,  "al":2}
    if default == None:
        prompt = " [y/n/a] "
    elif default == "yes":
        prompt = " [Y/n/a] "
    elif default == "no":
        prompt = " [y/N/a] "
    elif default == "all":
        prompt = " [y/n/A] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes', 'no', or 'all' "\
                             "(or 'y', 'n' or 'a').\n")

def query_yes_quit(question, default="quit"):
    '''Ask a yes/quit question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "quit" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "quit".
	
	Modified from
	http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input
	'''
    valid = {"yes":True,   "y":True,  "ye":True,
             "quit":False,     "q":False}
    if default == None:
        prompt = " [y/q] "
    elif default == "yes":
        prompt = " [Y/q] "
    elif default == "quit":
        prompt = " [y/Q] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'quit' "\
                             "(or 'y' or 'q').\n")

def wait(sec):
	'''
	Prints a timer with the format 0:00 to the console,
	and then clears the line when the timer is done
	'''
	while sec > 0:
		sys.stdout.write('\r' + str(sec//60).zfill(1) + ":" + str(sec%60).zfill(2) + '     ')
		sec -= 1
		time.sleep(1)
		sys.stdout.write('\r' + '           ' + '\r')
		
def title(mytitle):
	print colorama.Style.BRIGHT + colorama.Fore.YELLOW + colorama.Back.BLUE + centered(mytitle) + colorama.Style.RESET_ALL
	
def subtitle(mysubtitle):
	print colorama.Style.BRIGHT + centered(mysubtitle) + colorama.Style.RESET_ALL
	
class progressbar:
	current = 0
	maximum = 100
	bar_color = colorama.Fore.GREEN
	reset_color = colorama.Style.RESET_ALL
	lenght = 79
	
	def __init__ (self, current=0, maximum=100, bar_color=colorama.Fore.GREEN):
		self.current = min(current, maximum)
		self.maximum = max(current, maximum)
		self.color = bar_color
		self.length = 79 - (len(str(self.maximum)) * 2 + 6)
	
	def update(self, currently=None):
		if currently == None:
			pass
		else:
			self.current = currently
		filled = float(self.current) / float(self.maximum) * float(self.length)
		filled = int(filled)
		unfilled = self.length - filled
		mystring = "[" + self.color + "="*filled + " "*unfilled + self.reset_color + "] " + str(self.current).rjust(len(str(self.maximum))) + " / " + str(self.maximum)
		sys.stdout.write('\r' + mystring + '\r')
	
	def reset(self):
		self.current = 0
	
	
'''To-Do:
* add a 'rainbow-ize function to make text a rainbow of colours!
'''
