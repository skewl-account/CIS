# small little minigame doohickey
# for class. error prone in 
# one certain case.

# python.exe <path/to/lab>.py to execute.
# exports naturally as a module as well.
# made by me (Clueless)

import time;
import os;

TAX_PERCENTAGE = 6;
ORDERED_ITEMS = {};

MENU = {
    "the dawg": 16.00,
    "coffee": 5.00,
    "muffin": 4.00,
};

# this isn't cumulative but honestly 
# these are the most generic npc 
# responses so c:
FINISHED_KEYWORDS = ["done", "that"]


# functionality changes
# depending on the operating system (obviously)
# for UNIX-based systems (maybe BSD), 'clear'
# is the console command
#
# unsure if this can trigger rebound functions,
# i.e. on some system 'clear' exceutes 'clear' 
# and a fetcher program like 'neofetch'
# than just 'clear'

def clear():
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");

def introduce():
    clear();
    print("Welcome to the Coffee Shop.");
    print("What would you like?");

def calculateCumulativePrice():
    out = 0;
    for item in ORDERED_ITEMS.keys():

        out += ORDERED_ITEMS[item];

    return out + calculateTax(out);

def generateFilterList(sequence, searchQuery = None):
    return filter(lambda ligma: (not searchQuery) or (ligma == searchQuery), sequence.keys())

def generateReceipt(of, receiptLengthChars = 40):
    stars = "*" * receiptLengthChars
    out = [stars];
    for item in generateFilterList(of):

        # iirc format strings are much less performant
        # but i don't care
        out.append(f"{item.capitalize()} ({int(ORDERED_ITEMS[item] / MENU[item])}) - ${ORDERED_ITEMS[item]:.2f}");

    if (len(out) == 0):

        out.append("None")

    else: 

        # seems me that the reference on the assignment
        # page is 39 but i increased by one, dashes 
        # are also 9 characters long. adding one
        # to both makes a clear proportion
        out.append(f"Tax: {TAX_PERCENTAGE:.2f}%")
        out.append("-" * (receiptLengthChars // 10))
        out.append(f"Total: ${calculateCumulativePrice():.2f}")

    out.append(stars);
    return out;

def numericTransformer(maybeNumber, default):
    maybeNumber = default if maybeNumber == "" or maybeNumber == None else maybeNumber;

    if (str(maybeNumber).isnumeric()):

        return int(maybeNumber);

    else:

        return maybeNumber;

def calculateTax(number):
    return 0.06 * number;

def prompt(text, transformer = lambda x: x):
    print(text)
    return transformer(input());

def pluralize(count): 
    return "s" if count > 1 else ""

def execute_minigame():
    introduce()
    while (True):
        userInput = input().lower();
        if (userInput in FINISHED_KEYWORDS):
            cumulativePrice = calculateCumulativePrice();
            print(f"\nOkay. Your total will be ${cumulativePrice:.2f}.");

            break;

        isInMenu = userInput in MENU;
        if isInMenu:
            # unsure what variable declaration overhead
            # is in python but surely its less than 
            # two array indices

            # but then again why am i perf gouging for
            # a school project lmaoaoaoao
            itemCount = prompt(f"{userInput.capitalize()}, correct?\nHow many do you want? (1)", lambda input: numericTransformer(input, 1));
            # this is error-prone if you mix a string and an integer (just don't)
            cumulativeItemPrice = MENU[userInput] * itemCount;

            # unsure if a short-circuit is more performant than a ternary but ideally they should be the same
            # if lazily evaluated?
            ORDERED_ITEMS[userInput] = cumulativeItemPrice if (userInput in ORDERED_ITEMS) else cumulativeItemPrice;
            print(f"Got it; that's {itemCount} {userInput}{pluralize(itemCount)}.");
            time.sleep(0.125);
            print("Anything else?");

        else:
            if (userInput.strip() == ""):

                print("You've gotta buy something, man.");

            else: 

                print("That's not on the menu.");

            time.sleep(1);

    print("Here your receipt:");
    for line in generateReceipt(ORDERED_ITEMS):
        
        print(line);

    print("Thank you for your patronage! See you next time!");

if (__name__ == "__main__"):

    execute_minigame();

