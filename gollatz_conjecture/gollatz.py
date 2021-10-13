# 3x + 1 problem, Gollatz conjecture

num = int(input())
start_num = num
counter = 0
with open("gollatz_output.txt", 'w') as file:
    file.write('-------------------')
    file.write(f'The start number is: {str(start_num)}  ')
    file.write('-------------------')
    file.write('\n')
    while not num == 1:
        if num % 2 == 1:
            file.write(f'{num} Odd: {num} * 3 + 1 =')
            file.write('\n')
            num = num * 3 + 1
            # print(f'Odd: Number * 3 +1 {num}')
            counter += 1
        elif num % 2 == 0:
            file.write(f'{num} Even: {num} / 2 =')
            file.write('\n')
            num = num // 2
            # print(f'Even: Division into 2: {num}')
            counter += 1
    file.write(f'{num} Odd: {num} * 3 + 1 = 4!!!')
    file.write('\n')
    file.write('-------------------')
    file.write(f'The start number was: {str(start_num)}  ')
    file.write('-------------------')

print(f'Iterations to reach 1: {counter}')
