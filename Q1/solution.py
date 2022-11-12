total_num_in_shop = input()
total_size_in_shop = input()
total_request_num = input()
total_request_size = input()

def getValue(i):
    value = 0
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
    different = int(total_num_in_shop) - int(total_request_num)
    for i in total_size_in_shop:
        i = getValue(i)
    for x in total_request_size:
        x = getValue(x)
    total_size_in_shop.sort()
    total_request_size.sort()
    for i in range(int(total_request_num)):
        if total_size_in_shop[i + different] < total_request_size[i]:
            print("No")
            return
    print("Yes")


