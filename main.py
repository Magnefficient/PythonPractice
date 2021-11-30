choiceGroup = []
studentGroup =[]
mispelled = 0
choiceOfWord = input("ask the other user what  they want to type")
for x in choiceOfWord:
    choiceGroup.append(x)

#make sure that the students guess is the same size   as  the  correct word

letter = input("type the word your teacher wants you to spell")
for s in letter:
    studentGroup.append(s)


for t in range(len(choiceGroup)):
    if choiceGroup[t] != studentGroup[t]: 
        mispelled += 1


        """ changed to  plus equal 1 from plus 1 
        so the computer would stop to evaluate the variable and not say 
        """





print(mispelled , "letter(s) mispelled")



"""# fixed the problem in which the incorect number of letters mispelled wwas displayed by linking the current  
                                          value of t to the index of the two list this  allowed both letters to be analyzed by the computer  at the same time """


