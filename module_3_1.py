calls = 0 #счетчик
def count_calls ():
    global calls
    calls +=1
    return calls

def string_info (string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains (string, list_to_search):
    string = string.upper()
    list_to_search = [i.upper() for i in list_to_search]
    count_calls()
    return string in list_to_search

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
