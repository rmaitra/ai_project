import time
import sys
import os

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
script = {
    "What is the derivative of arcsin(x)?":"What do YOU think the derivative of arcsin(x) is?",
    "...I don't know.":"Well you wrote me, so how the hell do you expect me to know?"
}

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def welcome_message():
    print ""
    print ""
    print bcolors.OKBLUE + "loading N.A.S.I.R." + bcolors.ENDC,
    print_ellipse(10)
    print ""
    print ""
    print bcolors.WARNING + "Sup?" + bcolors.ENDC

def exit_message():
    print "Adios."
    print_thinking(4)
    os.system('clear')


def print_ellipse(number):
    for i in range(0,number):
        time.sleep(0.5)
        print ".",
        sys.stdout.flush()

def print_thinking(number):
    spinner = spinning_cursor()
    for _ in range(number):
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def print_ai_response(text):
    print ""
    print bcolors.WARNING + text + bcolors.ENDC

def verify_response(question):
    if(question == 'exit'):
        exit_message()

    if(question in script.keys()):
        print_thinking(15)
        sys.stdout.write('\b')
        print_ai_response(script[question])
        input_command()

    else:
        print_thinking(15)
        sys.stdout.write('\b')
        print bcolors.WARNING + "Um...I dunno." + bcolors.ENDC
        input_command()

def input_command():
    question = raw_input('> ')
    verify_response(question)

def main():
    input_command()

if __name__ == "__main__":
    os.system('clear')
    welcome_message()
    main()


