##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 7 starter code
##################################


def print_student_info():
    print("Name: Pratham Khatri")
    print("Student ID: 219447424")
    print("Section A")
    print("Email: khatri26@my.yorku.ca")


def task0():
    print_student_info()


def is_sorted(a_list):
    sort = 0
    l = len(a_list)
    for i in range(0, l - 1):
        if a_list[i] <= a_list[i + 1]:
            sort = sort + 1
    if l == 0 or sort == l - 1:
        return True
    else:
        return False


def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    l1 = is_sorted(x1)
    l2 = is_sorted(x2)
    l3 = is_sorted(x3)
    print(l1)
    print(l2)
    print(l3)


def merge_dict(dict1, dict2):
    for key in dict2:
        if key not in dict1:
            dict1.update({f"{key}": dict2[key]})


def task2():
    dict1 = {8: "Exercise", 9: "Breakfast", 12: "Lunch", 3: "Study", 6: "Netflix"}
    dict2 = {8: "Sleep", 10: "Lab", 12: "Class", 4: "Call Mom"}
    print("dict1")
    print(dict1)
    print("dict2")
    print(dict2)
    merge_dict(dict1, dict2)
    print("dict2 merged into dict1")
    print(dict1)


def invert_dict(a_dict):
    dic = {}
    for key in a_dict:
        dic.update({f"{a_dict[key]}": key})
    return dic


def task3():
    dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print(dict1)
    dic = invert_dict(dict1)
    print(dic)


def list_to_dict(a_list):
    l = len(a_list)
    dic = {}
    for i in range(0, l):
        dic.update({f'{i}': a_list[i]})
    return dic


def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1: "1", 2: "2"}]
    print(my_list)
    dic = list_to_dict(my_list)
    print(dic)


def str_list_to_num_list(a_list):
    for i in range(0, len(a_list)):
        a_list[i] = int(a_list[i])


def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(x)
    str_list_to_num_list(x)
    print(x)

def merge_lists(list1, list2):
    l1=is_sorted(list1)
    l2=is_sorted(list2)
    assert l1!=False, "List 1 is not sorted!"
    assert l2!=False,"List 2 is not sorted!"
    l=[]
    l1=len(list1)
    l2=len(list2)
    i=0
    j=0
    while i<l1 and j<l2:
        if list1[i]<=list2[j]:
            l.append(list1[i])
            i+=1
        else:
            l.append(list2[j])
            j+=1
    if i<l1:
        l.extend(list1[i:])
    if j<l2:
        l.extend(list2[j:])
    return l

def task6():
    DoAgain=True
    while DoAgain:
        list1=input("Input 1st sorted list of numbers [x1 x2 ...]: ").split()
        list2=input("Input 2nd sorted list of numbers [x1 x2 ...]: ").split()
        input1_list=[int(item) for item in list1]
        input2_list=[int(item) for item in list2]
        print("Merged list")
        merged_list=merge_lists(input1_list,input2_list)
        print(merged_list)
        ask=input("Try again [Y/N]?").upper()
        if ask!='Y':
            DoAgain=False

def main():
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()


if __name__ == "__main__":
    main()