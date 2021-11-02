#
# Investment banking system
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

# option 3 
def avg_price(prices):
    """Returns the average price of a list of 1 or more prices."""
    storage = 0
    for x in range(len(prices)):
        storage = storage + prices[x]
    return storage/len(prices)

# option 4
def min_day(prices):
    """Returns the day of the minimum price."""
    minindex = 0
    minimum = prices[0]
    
    for x in range(len(prices)):
        if prices[x] < minimum:
            minimum = prices[x]
            minindex = x
    return minindex
    
# option 5
def max_change_day(prices):
    """Returns the day (index) of the maximum single day change in price."""
    diff_list = []
    for x in range(len(prices)-1):
        diff_list += [prices[x+1] - prices[x]]
    
    maxindex = 0
    maximum = diff_list[0]
    
    for x in range(len(diff_list)):
        if diff_list[x] > maximum:
            maximum = diff_list[x]
            maxindex = x + 1
    return maxindex

# option 6
def any_above(prices, threshold):
    """Determines if there are any prices above a threshold."""
    for x in prices:
        if x > threshold:
            return True
    return False

# option 7
def find_tts(prices):
    """Returns a list containing the buy day, sell day and resulting profit - finds the best days on which to buy and sell."""
    buyday = 0
    sellday = 0
    profit = 0
    for x in range(len(prices)):
        for y in range(x+1, len(prices)):
            if prices[x] < prices [y]:
                if prices[y] - prices[x] > profit:
                    profit = prices[y] - prices[x]
                    buyday = x
                    sellday = y
    return [buyday, sellday, profit]     

def tts():
    """The main user-interaction loop"""
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            minindex = min_day(prices)
            print(minindex)
        elif choice == 5:
            maxindex = max_change_day(prices)
            print(maxindex)
        elif choice == 6:
            threshold = int(input('Enter your threshold: '))
            print(any_above(prices, threshold))
        elif choice == 7:
            toprint = find_tts(prices)
            print(toprint)
        else:
            print('Invalid choice. Please try again.')
