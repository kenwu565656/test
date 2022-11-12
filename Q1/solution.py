total_num_in_shop = input()
total_size_in_shop = input()
total_request_num = input()
total_request_size = input()

if int(total_request_num) > int(total_num_in_shop):
    print("No")
else:
    total_size_in_shop = total_size_in_shop.split(" ")
    total_size_in_shop = set(total_size_in_shop)
    total_request_size = total_request_size.split(" ")
    total_request_size = set(total_request_size)
    if total_request_size.issubset(total_size_in_shop):
        print("Yes")
    else:
        print("No")
