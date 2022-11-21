valids = [0, 1, 2, 5, 6, 8, 9]

valid_lcd_numbers = [1, 2, 5, 6, 8, 9]

number = int(input())
if number <= 6:
    print(valid_lcd_numbers[number-1])
else:
    count = 7
    curr_element = 10
    while count <= number:
        isValid = True 
        value = curr_element
        while curr_element != 0:
            rem = curr_element % 10 
            if rem in valids:
                curr_element = curr_element // 10
            else:
                isValid = False 
                break 
        if isValid:
            valid_lcd_numbers.append(value)
            count += 1
        curr_element = value + 1
    print(valid_lcd_numbers[-1])
    