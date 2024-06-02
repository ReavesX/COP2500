# Donald Jackson - movies.py - Calculates the cost of tickets (y) for (x)
# number of moviegoers, with a lower rate for groups over size 25.

# Initializing variables
partySize = int(input("Please enter the number of moviegoers:"))
ticketCost = 12
totalCost = ((partySize -1)  * ticketCost) + 9.50


# Conditionals to check for party size
if partySize >= 26:
    ticketCost = 7.25
    totalCost = partySize * ticketCost
    print("The price of the tickets will be:  $",totalCost)
elif partySize <= 25 and partySize > 1:
    ticketCost = 12
    print("The price of the tickets will be:  $",totalCost)
elif partySize == 1:
    print("The price of the tickets will be:  $",totalCost)
elif partySize == 0:
    print("Are you sure nobody is going?")
    partySize = int(input("Please enter the number of moviegoers:"))
    # Asks the user if they meant to input 0, and reruns the prior set of
    # conditionals.
    if partySize >= 26:
            ticketCost = 7.25
            totalCost = partySize * ticketCost
            print("The price of the tickets will be:  $",totalCost)
    elif partySize <= 25 and partySize > 1:
            ticketCost = 12
            print("The price of the tickets will be:  $",totalCost)
    elif partySize == 1:
            print("The price of the tickets will be:  $",totalCost)
    elif partySize <= 0:
            print("Alright, we're done here")
elif partySize < 0:
    print("Sorry but I don't believe that you have a party with",partySize,"people. Please confirm your number")
    partySize = int(input("Please enter the number of moviegoers:"))
    # Asks the user to confirm their input a negative response, and reruns the prior set of
    # conditionals.
    if partySize >= 26:
            ticketCost = 7.25
            totalCost = partySize * ticketCost
            print("The price of the tickets will be:  $",totalCost)
    elif partySize <= 25 and partySize > 1:
            ticketCost = 12
            print("The price of the tickets will be:  $",totalCost)
    elif partySize == 1:
            print("The price of the tickets will be:  $",totalCost)
    elif partySize <= 0:
            print("Alright, we're done here")
