######################################
# EECS1015 - Fall 2022
# Lab
#####################################

def print_student_info():
    print("Name: Pratham Khatri")
    print("ID: ")
    print("Section A")
    print("email: khatri26@my.yorku.ca")


def task0():
    print_student_info()


# Functions for task 1
# Write the function average_num() outside your task1() function.



def avg_num(*nums):

    sum = 0
    count = 0

    for item in nums:
        count = count + 1
        sum = sum + int(item)

    if count!=0:
        return sum/len(nums)

    else:
        return 0

def task1():
    while True:
        while True:
            in1 = int(input("Input 4 or 5 numbers? "))
            if (in1 == 4 or in1 ==5 ):
                break
        list1 = []

        if (in1 == 4):
            list1 = input("Input 4 numbers [x1, x2, x3, x4]:   ").split(',')
            if (len(list1) == 4):
                avg = avg_num(*list1)
                print("Average is {:.2f} ".format(avg))
            elif(len(list1) != 4):
                while len(list1) != 4:
                    list1 = input("Input 4 numbers [x1, x2, x3, x4]:   ").split(',')
                avg = avg_num(*list1)
                print("Average is {:.2f} ".format(avg))

        else:
            list1 = input("Input 5 numbers [x1, x2, x3, x4, x5]:   ").split(',')
            if (len(list1)==5):
                avg = avg_num(*list1)
                print("Average is {:.2f} ".format(avg))
            else:
                while len(list1) != 5:
                    list1 = input("Input 5 numbers [x1, x2, x3, x4, x5]:   ").split(',')
                avg = avg_num(*list1)
                print("Average is {:.2f} ".format(avg))

        yn = input("Try again? ").upper()
        if yn != 'Y':
            break




    pass


# Task 2
# Write function build_stock_dict() here.

# This function is provided for you.
def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-" * 31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}")
        # stock_dict[k][1]
        # ^^^^^^^^^^^^^    <- this gets the list for the key k
        #              ^^^ <- this retrieves item [1] in the list (price of stock)
        #
    print()  # <- an extra empty print to make it look nice


def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    stock_dict2={}
    space_Remove=stock_list_string.split(" ")
    #print(space_Remove)
    for n in space_Remove:
        smallList=[]
        find1=n.find(":")
        finding2=n.find(".")
        name=n[:find1]
        price=float(n[find1+1:finding2+3])
        symbol=n[finding2+4:]
        smallList.append(name)
        smallList.append(price)
        stock_dict2[symbol]=smallList
    print_stock_dict(stock_dict2)
    # uncomment code for task4
    #stock_dict2 = build_stock_dict(stock_list_string)
    #print_stock_dict(stock_dict2)



# Task 3 functions create_rand_list(), delete_list_item(), print_list() here ourside task3()
import random
def create_rand_list():
    num_of_elements=random.randint(5,15)
    min_value=random.randint(5,10)
    max_value=random.randint(20,50)
    randomList=[]
    for n in range(num_of_elements):
        i=random.randint(min_value,max_value)
        randomList.append(i)
    return randomList

def print_list(a_list):
    if len(a_list)!=0:
        print("--list--")
        for i in a_list:
            print(f"({i})->",end="")
        print("(end)")
    else:
        print("--list--")
        print("(empty)")

def delete_item_for_list(a_list,item):
    if item in a_list:
        for index in range(len(a_list)):
            if a_list[index]==item:
                return index
    else:
        return -1
# Task 3 functions create_rand_list(), delete_list_item(), print_list() here ourside task3()
def task3():
    rlist = create_rand_list()
    print_list(rlist)
    a = True
    while a == True:
        print_list(rlist)
        itemDelete = int(input("Item to delete: "))
        if delete_item_for_list(rlist, itemDelete) >= 0:
            print(f"Item {itemDelete} successfully deleted at position {delete_item_for_list(rlist, itemDelete)}.")
        else:
            print(f"Item {itemDelete} could not be deleted.")
        Ditem = input("Delete item [Y/N]? ").upper()
        if Ditem == "Y":
            a = True
            rlist.remove(rlist[delete_item_for_list(rlist, itemDelete)])
        else:
            a = False

    pass


# Task 4
# Write functions print_image and uncompress_rle_image() here
def print_image(image):
    for i in image:
        print(i)



def uncompress_rle_image(rle_image):
    listy = []
    for u in rle_image:
        sum = ""
        for q in range(len(u)):
            sum = sum + (u[q][0] * u[q][1])
        listy.append(sum)
    return(listy)

def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')],
                  [(9, ' '), (3, '8'), (1, 'l')],
                  [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
                  [(6, ' '), (1, '.'), (8, '8'), (1, '.')],
                  [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
                  [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')],
                  [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
                  [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
                  [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'),
                   (1, "'")],
                  [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'),
                   (1, '-'),
                   (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '),
                   (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')],
                  [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'),
                   (3, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'),
                   (7, '.'), (7, ' '), (3, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'),
                   (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'),
                   (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'),
                   (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')],
                  [(52, '.')]]

    # uncomment code for task4
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)



def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    task1()
    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")


if __name__ == '__main__':
    main()