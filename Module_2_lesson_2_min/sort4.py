str1 = [27, 37, 109, 24, 4, 25, 4, 29, 0, 64, 25, 21, 3, 22, 3, 24, 33]
repeated_number = []
for j in range(0, len(str1)):
    for i in range(0, len(str1)):
        if i != j and str1[j] == str1[i]:
            repeated_number.append(str1[j])
print("First repeated number is :",repeated_number[0])

