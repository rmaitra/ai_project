import time
import sys
import os


def welcome_message():
    print "loading Raj's A.I.",
    print_ellipse(10)
    print ""
    print ""
    print "Raj's A.I. > Raj Arificial Intelligence (A.I.) at your service!"
    print "Raj's A.I. > Please ask me to do something!"

def exit_message():
    print "Raj's A.I. > I'm glad to be of service. Goodbye!"


def print_ellipse(number):
    for i in range(0,number):
        time.sleep(0.5)
        print ".",
        sys.stdout.flush()

def print_thinking(number):
    print "Raj's A.I. > One sec, I'm thinking",
    for i in range(0,number):
        time.sleep(0.2)
        print ".",
        sys.stdout.flush()

def print_ai_response(text):
    print ""
    print ""
    print text

def verify_response(question):
    print ""
    print ""
    if(question == 'exit'):
        exit_message()

    #if(response == 'exit')
    #    print_ai_response()

    else:
        print_thinking(4)
        print "I did not understand, please ask again."
        input_command()

def input_command():
    print ""
    print ""
    question = raw_input('> ')
    verify_response(question)

def main():
    input_command()

if __name__ == "__main__":
    os.system('clear')
    welcome_message()
    main()
