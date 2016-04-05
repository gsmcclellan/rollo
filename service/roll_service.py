

def roll_single_die(numberOfSides):
    """
    Takes a single integer as input. Simulates rolling a die with that
    many sides. Example, an input of 6 would return a random number from
    1 to 6.
    """
    pass


def roll_multiple_dice(numberOfDice, numberOfSides):
    """
    Takes two inputs. The first is an integer for the number of times to 
    simulate rolling a die. The second is how many sides each of those dice should have.
    Returns a list of single die results
    """
    pass


def calculate_total(diceResults):
    """
    Takes input from roll_multiple_dice.
    calculates total dice rolls to return a single integer value
    """
    pass

if __name__ == "__main__":
    print "hello"



for number in range(1, 100):
    assert roll_single_die(number) <= number
    for num in range(1, 5):
        assert calculate_total(roll_multiple_dice(num, number)) <= num * number