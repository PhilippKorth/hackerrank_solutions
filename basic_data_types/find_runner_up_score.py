if __name__ == '__main__':
    n = int(input())
    # make a set to remove duplicates
    arr = set(map(int, input().split()))

    # runner up is next to last
    print(sorted(list(arr))[-2])