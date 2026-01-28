def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [x for x in args[:-1] if x % 2 == 0]
    elif command == "odd":
        return [x for x in args[:-1] if x % 2 != 0]

print(even_odd(2,3,4,5,6,7,8,9, "even"))
print(even_odd(2,3,4,5,6,7,8,9, "odd"))
print(even_odd(2,3,4,5,6,7,8,9, "even"))