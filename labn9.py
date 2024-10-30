###########################################
# EECS1015 - Practice Final Exam
# Fall 2022, York University
# Starting code
#
###########################################
import random

def student_info():
    print("Name: Pratham Khatri")
    print("Student ID: 219447424")
    print("Email: khatri26@my.yorku.ca")
    print("Section: A")
    print("Lab: 9 ")

def task0():
    student_info()

def task1():
    Do_again=True
    while Do_again:
        a=input("Type in a long sentence: ")
        b=input("Remove words containing: ")
        l=a.split(" ")
        p1=[]
        p2=[]
        for element in l:
            if b in element:
                p1.append(element)
            else:
                p2.append(element)
        j=' '
        p11=j.join(p1)
        p22=j.join(p2)
        print(f"With substring: '{p11}'")
        print(f"W/O substring: '{p22}'")
        ask=input("Try again? [Y/N]").upper()
        if ask!='Y':
            Do_again=False
# write randomlist and reshape for task2 below

def randomlist(N):
    a = []
    for i in range(0,N):
        rand_num = random.randint(0,9)
        a.append(rand_num)
        return a

def reshape(a_list, num_rows, num_cols):
    l1=[]
    l2 = []
    x=0
    for i in range(num_rows):
        l2=[]
        for j in range(num_cols):
            l2.append(a_list[x])
            x+=1
        l1.append(l2)
    return l1

def task2():
    run_again = True
    while run_again:
        N = int(input("List length: "))
        r1 = randomlist(N)
        print(r1)
        rows = int(input("Rows: "))
        cols = int(input("cols: "))
        while (rows * cols) != N:
            print(f"Error: {rows}*{cols} != {N}")
            rows = int(input("Rows: "))
            cols = int(input("cols: "))
        l = reshape(r1, rows, cols)
        print("Reshaped List")
        print(l)
        ask = input("Try again? [Y/N]").lower()
        if ask == "n":
            break




# write function find_duplicates() for task 3 below


def find_duplicates(a_dict):
    dict={}
    for key1 in a_dict:
        l = []
        for key2 in a_dict:
            if a_dict[key1]==a_dict[key2]:
                l.append(key2)
        if len(l)>1:
            dict[a_dict[key1]]=l
    return dict


def task3():
    Do_again=True
    while Do_again:
        print("Input words, press enter to end.")
        a_dict = {}
        user_in=None
        inp=1
        while user_in!="":
            user_in=input("[Input %2d] Word: " % inp)
            if user_in!="":
                a_dict[inp]=user_in
            inp = inp+1
        print("Dictionary")
        print(a_dict)
        b=find_duplicates(a_dict)
        print("Duplicates")
        print(b)
        ask=input("Try again? ").upper()
        if ask!="Y":
            Do_again=False



# write class rangeChecker for task4 below
class rangeChecker():
    range_counter=1
    def __init__(self,name, min, max):
        assert max>min, f"Max ({max}) must be greater than min ({min})"
        self.id=rangeChecker.range_counter
        rangeChecker.range_counter+=1
        self.name=name
        self.min_value=int(min)
        self.max_value=int(max)
    def within_range(self,number):
        if self.min_value<=number and self.max_value>=number:
            return True
        else:
            return False
    def outside_range(self,number):
        if number<self.min_value or number>self.max_value:
            return True
        else:
            return False
    def print(self):
        print(f"rangeChecker [{self.id:2d}] '{self.name:10s}' - {self.min_value:8.2f} <= num <= {self.max_value:8.2f}  ")



def task4():
    range_objects = []
    Do_again=True
    while Do_again:
        for i in range(3):
            objects = input(f"Range {i} Name, Min, Max: ").replace(" "," ").split(",")
            range_objects.append(rangeChecker(objects[0], float(objects[1]), float(objects[2])))
        list_of_numbers = input("Input list of numbers x1,x2,..,xn: ").replace(" ", "").split(",")
        for i in range(2):
            for object_range in range_objects:
                object_range.print()
                if i == 0:
                    for item in list_of_numbers:
                        item = float(item)
                        print(f"Inside range [{item:8.2f}]: {object_range.within_range(item)}")
                else:
                    for item in list_of_numbers:
                        item = float(item)
                        print(f"Outside range [{item:8.2f}]: {object_range.outside_range(item)}")
        ask=input("Try again? ").upper()
        if ask!="Y":
            Do_again=False



def main():
    task0()
    '''print("--- Task 1 ---")
    task1()
    print("\n--- Task 2 ---")
    task2()'''
    print("\n--- Task 3 ---")
    task3()
    print("\n--- Task 4 ---")
    task4()

if __name__ == "__main__":
    main()



