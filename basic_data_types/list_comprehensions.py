import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a,b,c] for (a,b,c) in itertools.product([i for i in range(x+1)], [j for j in range(y+1)], [k for k in range(z + 1)]) if a + b +c != n])
    
