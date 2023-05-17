from bardapi import Bard
import os
import sys
import threading
import time
import itertools


def display_help():
    print("Commands:")
    print("  help: Displays this help message")
    print("  exit: Exits the program")
    print("To ask a question, simply type it in and press Enter.")
    print("To enter a multiline question, end each line with '\\' until the final line.")

class Spinner:
    def __init__(self, message, delay=0.1):
        self.spinner = itertools.cycle(['-', '/', '|', '\\'])
        self.delay = delay
        self.busy = False
        self.spinner_visible = False
        sys.stdout.write(message)

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
        if self.spinner_visible:
            sys.stdout.write('\b')
            sys.stdout.flush()

def main():
    try:
        bard = Bard()
    except KeyError:
        print("The _BARD_API_KEY environment variable is not set.")
        sys.exit(1)
    print("Welcome to the Bard REPL! Type 'help' for a list of commands.")

    while True:
        try:
            user_input = input("(Bard) ").strip()
            while user_input.endswith("\\"):
                user_input = user_input[:-1] + "\n" + input("... ")

            if user_input.lower() == "help":
                display_help()
            elif user_input.lower() == "exit":
                print("Goodbye!")
                sys.exit(0)
            elif user_input:
                spinner = Spinner("Fetching answer... ")
                spinner.start()
                try:
                    answer = bard.get_answer(user_input)
                finally:
                    spinner.stop()
                content = answer['content']
                sys.stdout.write('\r')
                sys.stdout.flush()
                print(content)

            else:
                print("Please enter a question or a command.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()