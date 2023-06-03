def print_formatted(number):
    # your code goes here
    for value in range(1, number+1):
        padding = len(f'{number:b}')
        print(f'{value:>{padding}} {value:>{padding}o} {value:>{padding}X} {value:>{padding}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)