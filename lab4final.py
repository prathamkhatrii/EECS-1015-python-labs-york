################################
# EECS1015 York Univresity
# Lab 4 - Starter Code
# Name: Pratham Khatri
# Section A/B: A
# Student id:219447424
# Email: Khatri26@my.yorku.ca
################################
'''
print("Name: Pratham Khatri ")
print("Section A/B: A")
print("Student id: 219447424")
print("Email: khatri26@my.yorku.ca ")
'''

print(" ")
import time, random

jumps = 0
def get_int_input(prompt, min_val, max_val):
    num = int(input(prompt))
    while not num in range(min_val, max_val + 1):
        num = int(input(prompt))
    return num


def stat_yes(prompt):
    ask = input(prompt)
    ask = ask.upper()
    while not ask == 'Y' or not ask == 'N':
        if (ask == 'Y'):
            return True
        if (ask == 'N'):
            return False
        ask = input(prompt)
        ask = ask.upper()


pass

eye1 = '{o,o}'
eye2 = '{-,o}'
eye3 = '{o,-}'
body = '/)_) '
legs = ' " " '
def draw_owl(i, randomize):
    if (randomize == False):
        print(i * ' ', eye1)
        print(i * ' ', body)
        print(i * ' ', legs)
    else:
        number = random.randint(1, 3)
        if (number == 1):
            print(i * ' ', eye1)
            print(i * ' ', body)
            print(i * ' ', legs)
        if (number == 2):
            print(i * ' ', eye2)
            print(i * ' ', body)
            print(i * ' ', legs)
        if (number == 3):
            print(i * ' ', eye3)
            print(i * ' ', body)
            print(i * ' ', legs)
pass


def get_float_input(prompt, min_val, max_val):
    num1 = float(input(prompt))
    while (num1 < min_val or num1 > max_val):
        num1 = float(input(prompt))
    return num1
pass


def get_return(amount, rate, years):
    i = 0
    amount_new = 0
    while (i < years):
        amount_new = amount + (amount * rate)
        amount = amount_new
        i = i + 1
    return i, amount_new
pass

    #MAIN PROGRAM


def main():

#TASK 1
    def task1():
        print("\n---- Task 1: The Owl ----")
        N = get_int_input("How many times to move [2-20]? ", 2, 20)
        T = get_int_input("How long to delay [1-1000]? ", 1, 1000)
        work2 = stat_yes("Randomize [Y/N]? ")
        i = 0
        while (i < N):
            draw_owl(i, work2)
            time.sleep(T / 1000)
            i = i + 1



    #TASK 2
    def task2():
        print("\n---- Task 2: Compound investment ---")
        while True:
            int_amount = get_float_input("Input initial investment amount [1, 10000]? ", 1, 10000)
            ret_rate = get_float_input("Annual return rate [0-1]? ", 0, 1)
            year_cnt = get_int_input("How many years [1-10]? ", 1, 10)
            return_intst = get_return(int_amount, ret_rate, year_cnt)
            if (year_cnt == 1):
                print("Return in %d year is: $ %10.2f" % (return_intst))
            else:
                print("Return in %d years is: $ %10.2f" % (return_intst))
            ques = stat_yes("Compute new investment [Y/N]? ")
            if (ques == False):
                break


    #TASK 3
    def task3():
        print("\n---- Task 3: Max odd number ----")
        j = 0
        odd = 1
        while (j < 5):
            prompt = ("%d/5    Enter a number [1-100] " % (j + 1))
            user = get_int_input(prompt, 1, 100)
            if (user % 2 != 0 and user > odd):
                odd = user
            j = j + 1
        print("Final max odd number: %d" % (odd))



    #TASK 4
    def task4():
        print("\n---- Task 4: Jumping Jacks ----")
        fig1 = "  o   \n /|\  \n | |  "
        fig2 = " \o/  \n  |   \n / \  "
        jumps = odd

        input("Press enter to perform %d jumping jacks " % (jumps))
        k = 0
        for l in range(jumps):
            k = k+1
            if k > jumps:
                break
            print(fig2, "[ %d]" % (k))
            time.sleep(0.3)
            k = k + 1
            if k > jumps:
                break
            print(fig1, "[ %d]" % (k))
            print(' ')
            time.sleep(0.3)


    task1()
    task2()
    task3()
    task4()



if __name__ == "__main__":
    main()


#Press 'ENTER' to end lab4!
#THANK YOU!