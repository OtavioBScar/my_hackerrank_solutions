if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maior = max(arr)
    newArr = []
    for num in arr:
        if num < maior:
            newArr.append(num)
    print(max(newArr))