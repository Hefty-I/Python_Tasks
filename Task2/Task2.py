City = {
}

# for i in range(3):
#         x = input("Enter a city: ")
#         City[f"city{i}"] = x

with open("city.txt", 'w') as f:
    
    for i in range(3): # run loop 3 times
        x = input("Enter a city: ")
        City[f"city{i}"] = x # add the input city to dictionary

    for key, values in City.items(): 
        f.write(f"{key} "+ values +"\n") # write to the file key of dictionary along with the value

with open("city.txt",'r') as f:
        print(f.read())