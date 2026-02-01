def cat_assign(*args, **kwargs):
    person = {}
    for arg in args:
        person[arg] = kwargs[arg[0]]

    person = person.items()

    result = []
    for key, value in person:
        result.append(f"{key}: {value}")
    return "\n" .join(result)

print(cat_assign("Ivan", "Moni", M=3, I=8))

