import time

numbers_49 = [int(el) for el in range(1, 50)]

def current_milli_time():
    return round(time.time() * 1000)

miliseconds_last_two_digits = current_milli_time() % 100
print(f'{int(miliseconds_last_two_digits)}')

