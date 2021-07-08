import time

numbers_49 = [int(el) for el in range(1, 50)]

def current_milli_time():
    return round(time.time() * 1000)

miliseconds_last_two_digits = current_milli_time() % 100
print(f'Current milliseconds: {int(miliseconds_last_two_digits)}')

if miliseconds_last_two_digits < len(numbers_49):
    if miliseconds_last_two_digits == 0 or miliseconds_last_two_digits == 99:
        exit(0)
    index = numbers_49.index(miliseconds_last_two_digits)
    print(f'Number is: {numbers_49[index]}')
else:
    index = miliseconds_last_two_digits - len(numbers_49)
    print(f'Number is: {numbers_49[index]}')