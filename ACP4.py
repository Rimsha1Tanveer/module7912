num = int(input("Enter a number: "))

# Count the number of digits
digits = len(str(num))

# Store the original number
original = num

total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if total == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")