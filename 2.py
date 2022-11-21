def findNumberOfOccurances(inputStr, char):
    occurance_count = 0 
    for i in inputStr:
        if i == char:
            occurance_count += 1 
    return occurance_count 

if __name__ == "__main__":
    inputString1 = input()
    inputString2 = input()
    count = findNumberOfOccurances(inputString1, inputString2[-1])
    print(count)