import time
import sys
import os
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# this goes question : response
script = [
    ["What is the derivative of arcsin(x)?","What do YOU think the derivative of arcsin(x) is?"],
    ["...I don't know.","Well you wrote me, so how the hell do you expect me to know?"]
]

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def welcome_message():
    print ""
    print bcolors.OKBLUE + "Booting Nascent Artificial Sourced Intelligence Routine (NASIR)" + bcolors.ENDC,
    print_ellipse(5)
    print ""
    print ""
    print bcolors.WARNING + bcolors.BOLD + "What's good fam?" + bcolors.ENDC

def exit_message():
    print ""
    print "Adios."
    print_thinking(4)
    os.system('clear')

def delay_ai_print(s):
    print ""
    print bcolors.BOLD
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)
    print bcolors.ENDC

def delay_human_print(s):
    print bcolors.OKGREEN
    print "> ",
    sys.stdout.flush()
    time.sleep(2)

    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
	delay = 0.05 * randint(1, 6)
        time.sleep(delay)
    print bcolors.ENDC

def print_ellipse(number):
    for i in range(0,number):
        time.sleep(0.5)
        print ".",
        sys.stdout.flush()

def print_thinking(number):
    print ""
    spinner = spinning_cursor()
    for _ in range(number):
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.flush()

def main():
    for i in script:
        delay_human_print(i[0])
        print_thinking(4)
        delay_ai_print(i[1])
    delay_human_print("exit")
    exit_message()
        
      
if __name__ == "__main__":
    os.system('clear')
    welcome_message()
    main()

