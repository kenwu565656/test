total_num_in_shop = input()
total_size_in_shop = input()
total_request_num = input()
total_request_size = input()


def getValue(mylist):
    value = 0
    for i in mylist:
        if i.find("S", -1) != -1:
            value += 0.9 ** len(i)
        elif i.find("M", -1) != -1:
            value += 1
        else:
            value += 1.1 ** len(i)
    return value


if int(total_request_num) > int(total_num_in_shop):
    print("No")
else:
    total_size_in_shop = total_size_in_shop.split(" ")
    total_request_size = total_request_size.split(" ")
    shopValue = getValue(total_size_in_shop)
    resquestValue = getValue(total_request_size)
    if shopValue >= resquestValue:
        print("Yes")
    else:
        print("No")


