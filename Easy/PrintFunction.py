if __name__ == '__main__':
    n = int(input())
    values = [i for i in range(1, n+1)]
    print(*values, sep='', end='\n')