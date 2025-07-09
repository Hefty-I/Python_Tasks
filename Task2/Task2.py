City = {
}

for i in range(3):
        x = input("Enter a city: ")
        City[f"city{i}"] = x

with open("city.txt", 'w') as f:
    for key,values in City.items():
        f.write(f"{key} "+ x +"\n")

with open("city.txt",'r') as f:
        print(f.read())