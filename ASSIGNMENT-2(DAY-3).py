# ASSIGNMENT-2(DAY-3)
# USING FOR LOOP PLEASE PRINT ALL THE PRIME NUMBERS BETWEEN 1-200
# USING FOR LOOP AND RANGE FUNCTION:

lower=1
upper=200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
