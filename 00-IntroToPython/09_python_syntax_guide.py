def main():
    #Isaiah Racey
    print("Python Syntax Guide")
    variables()
    strings()
    loops()
    sequences()
def variables():
    print("....Variables.......")
    x = 7
    b = "bob"
    print(x+3)
    print(b*3)
    print(type(x))
    print(type(b))

def strings():
    print("----------strings-----------")
    str1 = "can't"
    str2 = 'Dave'
    str3 = '''Can use ' or " or even seperate
    spaced lines'''
    print(str1)
    print(str2)
    print(str3)
    x = 42
    str4 = f"X equals {x}.fun"
    print (str4)

def loops():
    x = 0
    while True:
        x = x+1
        print(f"X is {x}")
        if x >= 5:
            break
    print(f"X is equal to {x}")

    for k in range(5):
        print(k)

    total = 1
    for k in range(1,101):
        total = total * k
        print(total)

def sequences():
    print("sequences----------------")
    my_list = [4, 5, 6, 7, 8, 9, 10]
    my_list[2] = 99
    print(my_list)
    my_list.append(1000)
    print(my_list)
    print(f"The length of the list is {len(my_list)}")
    for k in range(len(my_list)):
        my_list[k] = my_list[k] + 10
        my_list[k] += 10
    print(my_list)

    total = 1
    for k in range(len(my_list)):
        total *= my_list[k]
    print(total)
    my_list.
main()
