# Write a program that reads from the console an integer n and draws a Christmas hat
# with a width of 4 * n + 1 columns and a height of 2 * n + 5 rows, as in the examples below.

# ......./|\.......
# .......\|/.......
# .......***.......
# ......*-*-*......
# .....*--*--*.....
# ....*---*---*....
# ...*----*----*...
# ..*-----*-----*..
# .*------*------*.
# *-------*-------*
# *****************
# *.*.*.*.*.*.*.*.*
# *****************

def draw_christmas_hat():
    n = int(input())


    dots_count = 2 * n - 1
    dots = '.' * dots_count

    print(f"{dots}/|\\{dots}")
    print(f"{dots}\\|/{dots}")


    for i in range(2 * n):
        current_dots = '.' * (2 * n - 1 - i)
        dashes = '-' * i
        print(f"{current_dots}*{dashes}*{dashes}*{current_dots}")


    width = 4 * n + 1

    print('*' * width)
    print('*' + '.*' * (2 * n))
    print('*' * width)



if __name__ == "__main__":
    draw_christmas_hat()
    