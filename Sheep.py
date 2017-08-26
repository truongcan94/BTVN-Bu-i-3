items = [5,7,300,90,24,50,75]
 # 2.1
print("Hello,my name is Hiep and these are my sheep size", items)
 # 2.2
sheep_biggest = 1
for item in [5,7,300,90,24,50,75] :
    if sheep_biggest < item :
        sheep_biggest = item
print('now my bigest sheep has size ',sheep_biggest,"let's shear it")
 # 2.3
item_no = 0
for item in items:
    if item == sheep_biggest:
        items[item_no] = 8
    item_no += 1
print("after shearing ,here is my flock")
print(items)
 # 2.4
new_item = [item + 50 for item in items]
print('one month has passed,now here is my flock')
print(new_item)
 # 2.5
month = int(input("Enter number month: "))
print('START :')
print("Hello,my name is Hiep and here is my flock")
print(items)
print()


for n in range (month):
    print("MONTH",n+1)
    new_item = [item + 50 for item in items]
    print('one month has passed,now here is my flock')
    print(new_item)

    sheep_biggest = 1
    for item in [5, 7, 300, 90, 24, 50, 75]:
        if sheep_biggest < item:
            sheep_biggest = item
    print('now my bigest sheep has size ', sheep_biggest, "let's shear it")

    item_no = 0
    for item in items:
        if item == sheep_biggest:
            items[item_no] = 8
        item_no += 1
    print("after shearing ,here is my flock")
    print(items)
 # 2.6
totalsize = sum(item for item in items)
print("My flock has total size of :", totalsize)
money = totalsize * 2
print("I would get ",totalsize,"* 2$","=",money,"$")




