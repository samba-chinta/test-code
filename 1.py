def convertToBase3(number):
    base3_val = 0
    position = 1
    while number > 0:
        base3_val = base3_val + (number % 3) * position
        position = position * 10 
        number = number // 3 
    return base3_val 

if __name__ == "__main__":
    num = int(input())
    result = convertToBase3(num)
    print(result)