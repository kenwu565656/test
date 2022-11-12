total_num = input()
mylist = []
for i in range(int(total_num)):
    item = input()
    mylist.append(item.split(" "))
allValid = True
errorCodes = []

for record in mylist:
    if allValid:
        if record[1] == "false":
            allValid = False
    if record[1] == "false":
        errorCodes.append(record[2])
if allValid:
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))
