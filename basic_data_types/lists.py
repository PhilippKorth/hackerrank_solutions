if __name__ == '__main__':
    N = int(input())

    value_list = []

    for _ in range(N):

        command, *params = input().split()
        params = list(map(int,params))

        match command:
            case 'insert':
                value_list.insert(params[0], params[1])

            case 'remove':
                value_list.remove(params[0])

            case 'append':
                value_list.append(params[0])

            case 'sort':
                value_list.sort()

            case 'pop':
                value_list.pop()

            case 'reverse':
                value_list.reverse()

            case _:
                print(value_list)