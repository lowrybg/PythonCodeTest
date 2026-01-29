def concat(*args,**kwargs):
    result = "-".join(args)
    for key, value in kwargs.items():
        result = result.replace(key,value)

    return result

print(concat("one","two","three"))
print(concat("one","two","three","four","five"))
