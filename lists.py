# create a list

epic_programmer_list = ["Tim Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

# print to console
print "An epic programmer: " + epic_programmer_list[1]


''' all entries '''

#print to console
print "An epic programmer: " +epic_programmer_list[0]
print "An epic programmer: " +epic_programmer_list[1]
print "An epic programmer: " +epic_programmer_list[2]
print "An epic programmer: " +epic_programmer_list[3]
print "An epic programmer: " +epic_programmer_list[4]

#add myself

epic_programmer_list.append("Me")

#add this to show myself in the console

print "An epic programmer: " +epic_programmer_list[5]

#loop through each item in the list epic_programmer_list

for programmer in epic_programmer_list:
    #print the programmer's name to console
    print programmer

# with title:

for programmer in epic_programmer_list:
    print "An epic programmer: " + programmer



'''#number example:
number_list = [1,2,3,4,5]

for x in number_list:

    # print each number to the power of 2

    print x**2

empty_list = []
empty_number_list = []

#append each number to the power of 2 to the empty_number_list

empty_number_list.append(x**2)'''

number_list = [1,2,3,4,5]
empty_number_list = []

for x in number_list:empty_number_list.append(x**2)
print empty_number_list


