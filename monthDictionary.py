import calendarTask
from datetime import datetime

sellDictionary = {'April': 200, 'may': 700, 'June': 700, 'july': 700, 'august': 500, 'September': 600, 'October': 175,
                  'November': 560, 'December': 300, 'January': 123, 'February': 500, 'March': 300}

"""    1st Sorting Monthwise Alphabetically    """
"""    4th Sorting By Upper and Lower Keys    """
monthByAlphabet = sorted(sellDictionary.items())
print(monthByAlphabet)

monthByAlphabetReverse = sorted(sellDictionary.items(), reverse=True)
print(monthByAlphabetReverse)

"""    2nd Sorting By Value    """
byValue = sorted(sellDictionary.items(), key=lambda key: key[1])
print(byValue)

byValueReverse = sorted(sellDictionary.items(), key=lambda key: key[1], reverse=True)
print(byValueReverse)

"""    3rd Key By Sorting Values    """
keyList = sorted(sellDictionary, key=sellDictionary.__getitem__)
print(keyList)

"""    5th Sort by Most Repeat Value    """


def repeats(ints):
    """
    func :- Counts occurrence of values in Dictionary
    param :- Values of SellDictionary
    returns :- Number of Occurrence
    """
    values = list(sellDictionary.values())
    counts = [values.count(ints)]
    return max(counts)


valueRepeat = sorted(sellDictionary.items(), key=lambda key: repeats(key[1]), reverse=True)
print(valueRepeat)

valueRepeat2 = sorted(sellDictionary.items(), key=lambda key: repeats(key[1]))
print(valueRepeat2)

"""    6th Sort by Even and Odd number of Month    """


def evenOdd(monthName):
    """
    func :- Check for number of month is Odd or Even using temporary dictionary
    param :- Keys of SellDictionary(Month names)
    returns :- Number for sorting Months
    """
    months = {'April': 4, 'may': 5, 'June': 6, 'july': 7, 'august': 8, 'September': 9, 'October': 10, 'November': 11,
              'December': 12, 'January': 1, 'February': 2, 'March': 3}
    num = months[monthName]
    if num % 2 == 0:
        return num
    else:
        return -num


def evenOddCalendar(monthName):
    """
    func :- Check for number of month is Odd or Even using Calendar.
    param :- Keys of SellDictionary(Month names)
    returns :- Number for sorting Months
    """
    for num in range(1, 13):
        if monthName.lower() == calendarTask.month_name[num].lower():
            if num % 2 == 0:
                return num
            else:
                return -num


oddMonths = sorted(sellDictionary.keys(), key=evenOdd)
print(oddMonths)

evenMonths = sorted(sellDictionary.keys(), key=evenOddCalendar, reverse=True)
print(evenMonths)

"""    7th Sort it By Number of Days of month    """


def daysOfMonth(monthName):
    """
    func :- Checks number of Days in a Month
    param :- Keys of SellDictionary
    returns :- Number for Day wise Sorting
    """
    for num in range(1, 13):
        if monthName.lower() == calendarTask.month_name[num].lower():
            days = calendarTask.monthrange(datetime.now().year, num)
            if days[1] == 31:
                return num
            elif days[1] == 30:
                return -num
            else:
                return num - 15


daywiseMonths = sorted(sellDictionary.keys(), key=daysOfMonth)
print(daywiseMonths)

"""    8th Sorting by subdictionary's key and value    """
quantityByMonths = {'April': {'quantity': 100}, 'may': {'quantity': 998}, 'June': {'quantity': 333},
                    'july': {'quantity': 200}, 'august': {'quantity': 470}, 'September': {'quantity': 490},
                    'October': {'quantity': 300}, 'November': {'quantity': 200}, 'December': {'quantity': 610},
                    'January': {'quantity': 544}, 'February': {'quantity': 900}, 'March': {'quantity': 780}}

subDictionaryByValue = sorted(quantityByMonths.items(), key=lambda key: key[1]['quantity'])
print(subDictionaryByValue)

quantityByDates = {'April': {2: 100}, 'may': {5: 998}, 'June': {30: 333}, 'july': {1: 200}, 'august': {27: 470},
                   'September': {16: 490}, 'October': {23: 300}, 'November': {9: 200}, 'December': {6: 610},
                   'January': {31: 544}, 'February': {14: 900}, 'March': {23: 780}}

subDictionaryByKey = sorted(quantityByDates.items(), key=lambda key: list(key[1].keys())[0])
print(subDictionaryByKey)
