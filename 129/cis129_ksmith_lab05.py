# Author: Kishamo Smith
# Helps you live slightly more comfortably in
# places like Germany by helping you calculate
# how much money one would get from tra-er, 
# recycling bottles.

import math;
DEFAULT_PAYOUT_PER_BOTTLE = 0.1;

def calcPayout(totalBottles: int, payoutPerBottle: float = DEFAULT_PAYOUT_PER_BOTTLE):
    return totalBottles * payoutPerBottle;
        
if (__name__ == "__main__"):
    userInput = "y";

    while userInput == "y":
        totalBottles = 0;
        totalPayout = 0;
        todayBottles = 0;
        counter = 0;

        while counter < 7:
            counter += 1;

            userInput = '';
            while userInput == '':
                userInput = input(f"Enter number of bottles for day #{counter} (numeric):").strip();
                if (userInput.isnumeric()):

                    totalBottles += math.floor(int(userInput));

                elif userInput != '':

                    raise Exception(f"You submitted '{userInput}'. That is not a numeric value.")

        print(f"The total number of bottles collected is ${totalBottles}.");
        print(f"The total paid out is ${calcPayout(totalBottles):.2f}");

        print("Do you want to enter another week's worth of data?")
        userInput = input("(Enter y or n): ")

    print("Goodbye!");
