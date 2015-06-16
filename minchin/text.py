#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Minchin.Text
v.5.0.1 - WM - June 10, 2015

This is a helper file, containing formatting helps for creating command line
programs.
'''
from __future__ import division
import sys
import time
import re
import colorama

__version__ = '5.0.1'

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

#term colour control codes
re_ansi_control_codes = re.compile(r'\033\[[017](;[034][0-9])*m|\x1b\[[034][0-9]*m')

# The regex patterns are intended only to match web URLs -- http,
# https, and naked domains like "example.com".
# from https://gist.github.com/gruber/8891611
re_weburl = re.compile(r'(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))')

# The regex patterns is intended to match any URLs,
# including "mailto:foo@example.com", "x-whatever://foo", etc
re_allurl = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')

def length_no_ansi(mystring):
    '''Takes a string, strips out the ANSI escape codes
    (used for colouring terminal output, etc.), and returns
    the length of the resulting string'''
    newstring = re.sub(re_ansi_control_codes, "", mystring)
    return len(newstring)

def centered (mystring, linewidth=79, fill=" "):
    '''Takes a string, centres it, and pads it on both sides'''
    sides = (linewidth - length_no_ansi(mystring))//2
    extra = (linewidth - length_no_ansi(mystring))%2
    fill = fill[:1]
    sidestring = fill*sides
    extrastring = fill*extra
    newstring = sidestring + mystring + sidestring + extrastring
    return newstring

def clock_on_right(mystring):
    '''Takes a string, and prints it with the time right aligned'''
    taken = length_no_ansi(mystring)
    padding = 79 - taken - 5
    clock = time.strftime("%I:%M", time.localtime())
    print (mystring + " "*padding + clock)

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
        choice = input().lower()
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
        choice = input().lower()
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
        choice = input().lower()
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
    print (colorama.Style.BRIGHT + colorama.Fore.YELLOW + colorama.Back.BLUE + centered(mytitle) + colorama.Style.RESET_ALL)

def subtitle(mysubtitle):
    print (colorama.Style.BRIGHT + centered(mysubtitle) + colorama.Style.RESET_ALL)

class progressbar(object):
    current = 0
    maximum = 100
    bar_color = colorama.Fore.GREEN
    reset_color = colorama.Style.RESET_ALL
    lenght = 79

    def __init__ (self, current=0, maximum=100, bar_color=colorama.Fore.GREEN):
        self.current = max(min(current, maximum), 0)
        self.maximum = max(max(current, maximum), 0.000001)  # something slightly above zero
        self.color = bar_color
        self.length = 79 - (len(str(self.maximum)) * 2 + 6)

    def update(self, currently=None):
        if currently == None:
            pass
        else:
            self.current = max(currently, 0)
        filled = float(self.current) / float(self.maximum) * float(self.length)
        filled = int(filled)
        filled_str = ''
        if filled == self.length:
            filled_str = '='*filled
        elif filled > 0 :
            filled_str = '='*(filled-1) + '>'
        unfilled = self.length - filled
        mystring = "[" + self.color + filled_str + " "*unfilled + self.reset_color + "] " + str(self.current).rjust(len(str(self.maximum))) + " / " + str(self.maximum)
        sys.stdout.write('\r' + mystring + '\r')

    def reset(self):
        self.current = 0


'''
To-Do:
* add a 'rainbow-ize function to make text a rainbow of colours!
* add a 'align-righted' function (text on right)
'''
