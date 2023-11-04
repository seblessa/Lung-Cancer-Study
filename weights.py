weight = {1: 0.18745, 2: 0.34375, 3: 0.65625, 4: 1.28125, 5: 2.53125}

#weight = {1: 0.5, 2: 0.75, 3: 1, 4: 1.25, 5: 1.5}


print(weight.__getitem__(1))

exit(0)

total = 0
weight_total = 0
for i in range(1, 5):
    malignancy = int(input("Enter the " + str(i) + "º malignancy: "))

    for j in range(1, 6):
        if malignancy == j:
            total += malignancy * weight[j]
            weight_total += weight[j]
            print(str(malignancy) + " * " + str(weight[j]) + " = " + str(malignancy * weight[j]))

print(total / weight_total)
