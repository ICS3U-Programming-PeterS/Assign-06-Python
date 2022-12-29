#!/usr/bin/env python3


# Created by: Peter Sobowale
# Created on: Dec 25 2022
# This program split a list of numbers
# in the middle and store the two halves
# in separate lists.
import math  # import the math module


# split list function
def split_list(lst, first_half, second_half):
    middle = int(len(lst) / 2)  # calculate the middle index of the list

    middle = math.ceil(middle)  # round up to the nearest integer

    # iterate over the first half of the list and append the elements
    # to the first_half list
    for i in range(middle):
        from_list = lst[i]
        first_half.append(from_list)

    # iterate over the second half of the list and append the elements
    # to the second_half list
    for i in range(middle, len(lst)):
        from_list = lst[i]
        second_half.append(from_list)


def main():

    # Read a list of numbers from a text file or get the input
    # from the user, split it in the middle, and print the two
    # halves.

    print(
        "This program reads a list of elements from a text file "
        + "or gets the input from user. Then splits it in the middle "
        + "and stores the elements in two different lists"
        + " using pass by reference\n"
    )

    # ask the user whether they want to input the list or read it from a file
    fileInput = input("Do you want to input or " + "read from a file (Input, File): ")

    if fileInput.upper() == "FILE":  # if the user wants to read from a file
        try:
            # open the file in read mode
            with open("test.txt", "r") as f:
                # read the first line of the file
                list_string = f.readline()
                # split the line into a list of numbers
                lst = list(map(int, list_string.split()))
                # create empty lists to store the two halves of the list
                half_1 = []
                half_2 = []

                # call the split_list function to split the list in the middle
                split_list(lst, half_1, half_2)

                # print the two halves of the list
                print("First half: ", half_1)
                print("Second half: ", half_2)

        except Exception:
            print("There was an error reading the file or parsing the list.")

    else:  # if the user wants to input or they just input incorrectly
        try:
            # get list of numbers
            list_string = input("Enter a list of elements (separated by spaces): ")

            # split the line into a list of numbers
            lst = list_string.split()

            # create empty lists to store the two halves of the list
            half_1 = []
            half_2 = []

            # call the split_list function to split the list in the middle
            split_list(lst, half_1, half_2)

            # print the two halves of the list
            print("First half: ", half_1)
            print("Second half: ", half_2)

        # display exception
        except Exception:
            print("There was an error parsing the list.")


# call main
if __name__ == "__main__":
    main()
