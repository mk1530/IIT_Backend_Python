import itertools

#Returns all possible combinations of bits up to n digits
def per(n):
    lst = list(itertools.product([0, 1], repeat=n))
    return lst



#The current solution is a traditional brute force way to fulfil the requirement.
#Repeat the program until user choose to exit
while True:

    #Gently ask the user to provide the input
    print('Please enter your digits seperated by a comma (or) enter exit to end the program:')
    user_input=input()
    #Terminate the program if the user chooses to exit
    if user_input=='exit':
        break
    #Check if the user entered sequence is made of digits i.e., no letters or special characters
    if user_input.replace(',','').isnumeric():
        #Split the sentence into words based on the commas in between
        allnums=user_input.split(',')
        numberlist=[]
        #convert user input to integers
        for i in allnums:
            numberlist.append(int(i))
        #get (length of input number list -1) bit combinations (Equal to the number of signs required in our usecase)
        signs=per(len(numberlist)-1)
        #Empty list to hold all possible combinaitons of integers after applying the signs
        allpossibilities=[]

        #For every combination of signs/bits
        for thing in signs:
            #Build the expression based on the bit combinations. 0 gives a minus sign and 1 gives a plus sign
            expresion=numberlist[0]

            for num in range(1, len(numberlist)):
                if thing[num-1]==0:
                    expresion=expresion-numberlist[num]
                else:
                    expresion=expresion+numberlist[num]
            allpossibilities.append(expresion)
        #Find the value that is closest to 0 out of all possible values
        print('Value close to zero is '+str(min(allpossibilities, key=abs)))

    #Raise an error if the input contains other than numbers
    else:
        print('Only numbers please\n')
        print(' ')


