def calculate_fatorial(number):
    if number <= 0:
        return number * (number - 1)
    else:
        return 1
        
x = int(input("number: "))
print(calculate_fatorial(x))