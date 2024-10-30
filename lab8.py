##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random


def print_student_info():
    print("Name: Pratham Khatri ")
    print("Student ID: 219447424")
    print("Section A ")
    print("Email: vedansh.patel@outlook.com")

# class for task 2
class virus:
    def __init__(self,DNAinput=""):
        self.DNA=DNAinput
        valid_char=['A','G','T','C']
        Everything_is_fine=False
        if len(DNAinput)!=0:
            for item in DNAinput:
                if len(DNAinput) == 50:
                    if item in valid_char:
                        Everything_is_fine=True
                if not Everything_is_fine:
                    print("string is either not exactly 50 characters long or every item in string is not in the valid character set.")
        if len(DNAinput) == 0:
            self.DNA =''.join(random.choice('AGTC') for i in range(50))

    def getDNA(self):
        return self.DNA

    def replicate(self):
        MutatedDNA = self.getDNA()
        rand_num= random.randint(0,100)
        if(rand_num> 94):
            rand_id_x = random.randint(0,49)
            MutatedDNA = MutatedDNA[:rand_id_x] + random.choice('AGTC') + MutatedDNA[rand_id_x+1:]
            x = virus(MutatedDNA)
        else:
            x = virus(self.DNA)
        return x

def find_mutation(virus1,virus2):
    virus1_DNA=virus1.getDNA()
    virus2_DNA=virus2.getDNA()
    new_string=''
    for i in range(len(virus1_DNA)):
        if(virus1_DNA[i] != virus2_DNA[i]):
            new_string = new_string + "^"
        else:
            new_string = new_string + " "
    return new_string

def lotto_draw():
    x=set()
    while len(x)!=5:
        num=random.randint(1,20)
        x.add(num)
    return x

# class for task 1
class lotto_ticket:
    ticket_count = 1

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_count
        lotto_ticket.ticket_count = lotto_ticket.ticket_count + 1
        rand_num = lotto_draw()
        self.numbers = rand_num

    def print_ticket(self):
        print("\nTicket #[{:3d}]".format(self.ticket_id) ,end= ' ')
        for item in self.numbers:
            print("  {:2d}".format(item),end='  ')


    def print_and_return_win(self, lotto_numbers):
        count = 0
        print("\nTicket #[{:3d}]".format(self.ticket_id) ,end= ' ')
        common_set = set()
        for item1 in self.numbers:
            for item2 in lotto_numbers:
                if item1 == item2:
                    common_set.add(item1)
                    count = count + 1
        matched = 0
        for item1 in self.numbers:
            for item2 in common_set:
                if item1 == item2:
                    matched = matched + 1
            if matched != 0:
                print(" *{:02d}*".format(item1), end=' ')
            if matched == 0:
                print("  {:02d}".format(item1), end='  ')
            matched = 0
        Win_amount = 0
        if count >= 0 and count <= 2:
            Win_amount = 0
        elif count == 3:
            Win_amount = 2
        elif count == 4:
            Win_amount = 20
        elif count == 5:
            Win_amount = 100
        print(" [{} matches, ${}]".format(count, Win_amount))
        return Win_amount
    pass


def task0():
    print_student_info()

def task1():
    amount = 100
    Do_again = True
    print(f"You have {amount}.")
    while Do_again:
        ticket = int(input("How many lotto tickets do you want [$2 each]? "))
        price = ticket * 2
        if price > amount or ticket < 0:
            print(f"You have {amount}.")
        elif ticket == 0:
            print(f"You have {amount}.")
            Do_again = False
        else:
            amount = amount - price
            list_object = []
            for i in range(0, ticket):
                item = 'a' * i
                list_object.append(item)
            for i in range(0, len(list_object)):
                list_object[i] = lotto_ticket()
                list_object[i].print_ticket()
            lotto_numbers = lotto_draw()
            print("\n--LOTTO DRAW--")
            for item in lotto_numbers:
                print(item, end=' ')
            input("\n---Press enter to check your winnings--- ")
            Sum_win_amount = 0
            for i in range(0, len(list_object)):
                Win_amount1 = list_object[i].print_and_return_win(lotto_numbers)
                Sum_win_amount += Win_amount1
            amount = amount + Sum_win_amount
            print(f"You have {amount}.")
            if amount < 2:
                Do_again = False
pass

def task2():
    Do_again = True
    while Do_again:
        name = input("Name Of Virus: ")
        my_virus = virus()
        original_virus = my_virus
        print("Original DNA Sequence:", original_virus.getDNA())
        n = int(input("How many times to replicate? "))
        for i in range(n):
            my_virus = my_virus.replicate()
            print("Replica [{:3d}] DNA Sqeuence:".format(i+1), my_virus.getDNA())
        new_string = find_mutation(original_virus, my_virus)
        print(f"Comparing latest {name} to the original {name}.")
        A = my_virus.getDNA()
        B = original_virus.getDNA()
        print(A)
        print(B)
        num_of_mutaion = new_string.count("^")
        if (num_of_mutaion != 0):
            print(new_string)
        if (num_of_mutaion == 0):
            print("No Mutation Found")
        elif (num_of_mutaion <= 5):
            print(f"{new_string.count('^')} mutations -- virus is the same.")
        else:
            print(f"{new_string.count('^')} mutations -- a *new* virus has been created.")
        ask = input("Try again?").upper()
        if ask != 'Y':
            Do_again = False
    pass

def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
    main()