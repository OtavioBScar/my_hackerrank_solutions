if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range (n):
        list.append(i)
    for i in list:
        print(list[i]**2)