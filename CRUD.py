items = ["T-Shirt","Sweater"]
loop_continue = True
while loop_continue:
    choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
    def print_items():
        item_no = 1
        for item in items:
            print("Our items: ")
            print("#", end="")
            print(item_no, end=". ")
            print(item)
            item_no += 1
    if choice == "c":
        new_item = input("You can enter new item: ")
        items.append(new_item)
        print_items()
    elif choice == "r":
        print_items()
    elif choice == "u":
        position = int(input("Enter update position: "))
        new_item_name = input("Enter new name position: ")
        items[position -1] = new_item_name
        print_items()
    elif choice == "d":
         position = int(input("Anh muốn xóa vị trí nào? "))
         items.pop(position - 1)
         print_items()
    else:
        loop_continue = False





