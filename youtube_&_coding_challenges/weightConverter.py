# weight_lbs = input("Enter Weight(lbs): ")
# weight_kg = float(weight_lbs) * 0.45
# print(f"{weight_kg} kg.")

# >-------------- this is creating new set of prices with no pair value -------------
prices = [10, 40, 10, 30, 20, 20, 30]
newPrice =[]

for i in prices:
 if i not in newPrice:
    newPrice.append(i)

newPrice.sort()
print(newPrice)





 
    




