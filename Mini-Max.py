def miniMaxSum(array):
    max_sum = sum(array[1:])
    min_sum = sum(array[:-1])
    print(min_sum, max_sum)

if __name__ == '__main__':
    array = sorted(list(map(int, input().strip().split())))
    miniMaxSum(array)
