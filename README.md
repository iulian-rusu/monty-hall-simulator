# Monty Hall Simulator
### A short Python script that simulates the Monty Hall problem.

The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. 
The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. 

**_Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?_**

Vos Savant's response was that the contestant should switch to the other door. Under the standard assumptions, contestants who switch have a 
2
/
3
 chance of winning the car, while contestants who stick to their initial choice have only a 
1
/
3
 chance.
 
 The script must receive a command line argument representing the number of tests to be simulated.
 Other command line arguments are optional:
 * __-c__ - specifies that the script will always simulate switching the pick.
 * __-l__ - prints some extra log messages for each test case.
 
 Examples of use:
 * ``` $ python3 mh_sim.py 1000 ``` to run 1000 test cases (by default, the script will simulate not changing the pick)
 * ``` $ python3 mh_sim.py -l 15 ``` to run 15 test cases and to print extra log mesages
 * ``` $ python3 mh_sim.py -c 200 ``` to run 200 test cases and to always change the initial pick
 * ``` $ python3 mh_sim.py 100 -lc > test_results.txt ``` to run 100 test cases with log messages and while changing the pick, the results being written to a file
