from re import X


def plusMinus(arr):
    positive = [num for num in arr if num > 0]
    zero = [num for num in arr if num == 0]
    negative = [num for num in arr if num < 0]
    def divide(x):
        return f"{len(x)/len(arr):.6f}"
    print(f"{divide(positive)}\n{divide(negative)}\n{divide(zero)}")   

if __name__ == '__main__':
    arr_size = int(input().strip())
    arr = list(map(int, input().strip().split()))
    plusMinus(arr)