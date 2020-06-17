import random
import sys

# A sript that simulates the Monty Hall paradox for a certain number of tries.
# When called, the script must receive one number as a command line argument - the number of tests to be simulated.
# All other command line arguments are optional.
#
# Examples of use:
#
#   $ python3 mh_sim.py 10 -lc                  # runs 10 tests with log messages and while changing picks every time
#   $ python3 mh_sim.py 500                     # runs 500 tests without logs and without changing picks
#   $ python3 mh_sim.py -c -l 10000 > log.txt   # runs 10000 tests with changing picks and log messages
#
# The last example of use will fill the terminal with text so it's recommended to redirect output to a file                                                         

class MontyHall():

    def __init__(self, n_tests : int, show_log : bool, changing : bool):
        self.NUM_TESTS = n_tests
        self.options = [1, 0, 0]
        self.show_log = show_log
        self.changing = changing

    # runs all tests and calculates the win percentage at the end
    def play(self):
        self.wins = 0
        print("_"*80)
        print(f"\t\t\t[RUNNING {self.NUM_TESTS} TESTS]")
        for x in range(self.NUM_TESTS):
            self.test_case(x)
        win_ratio = 100.0 * self.wins / self.NUM_TESTS
        print(f"\t\t\tWIN RATIO: %5.2f %% "%(win_ratio), end='',)
        if self.changing:
            print("(WHEN CHANGING PICKS)")
        else:
            print("(WHEN NOT CHANGING PICKS)")

    # method that runs a single test case
    def test_case(self, index : int):
        if(self.show_log):
            print(f"[TEST #{index}]", end='')
        self.shuffle()
        self.pick_option()
        self.open_incorrect_option()
        self.change_option()
        if(self.show_log):
            if(self.options[self.pick] == 1):
                print("\t\tYou won!\n")
            else:
                print("\t\tYou lost :(\n")
        self.wins += self.options[self.pick]
          
    # shuffles the list of picks
    def shuffle(self):
        self.available_picks = set(range(len(self.options)))
        random.shuffle(self.options)
        if(self.show_log):
            print(f"\tOptions:",end='')
            for op in self.options:
                if op == 1:
                    print(" WIN ",end='')
                else:
                    print(" LOSS ", end='')
            print()

    # searches for an unpicked incorrect option to be opened
    def open_incorrect_option(self):
        for option in range(len(self.options)):
            if self.pick != option and self.options[option] == 0:
                self.open(option)
                break

    # opens an option
    def open(self, option : int):
        self.available_picks.remove(option)
        if(self.show_log):
            print("\t\tOpenning one of the wrong options: ")
            print("\t\t",end='')
            for x in range(len(self.options)):
                if x == option:
                    print(" [_] ", end='')
                elif x == self.pick:
                    print(f"<[{x}]>",end='')
                else:
                    print(f" [{x}] ", end='')
            print()   

    # simulates the picking of a random option by the player
    def pick_option(self):
        self.pick = random.randrange(0,2)
        if(self.show_log):
            print(f"\t\tYou picked index: <[{self.pick}]>")
        self.available_picks.remove(self.pick)

    # changes the player's pick if self.changing flag is True
    def change_option(self):
        if(self.changing):
            self.pick = self.available_picks.pop()
            if(self.show_log):
                print(f"\t\tYou changed the pick to {self.pick}")

  

if __name__=="__main__":
    # flags for command line arguments
    num_tests = 0
    log_flag = False
    changing_flag = False
    for arg in sys.argv[1:]:
        if 'l' in arg:
            log_flag = True
        if 'c' in arg:
            changing_flag = True
        if arg.isnumeric():
            num_tests = int(arg)

    monty_hall_obj = MontyHall(n_tests=num_tests, show_log=log_flag, changing=changing_flag)
    monty_hall_obj.play()