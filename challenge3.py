'''
Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

For example:
occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0
'''
def occurances(word,letters):
    count=0

    if len(letters) ==2:
        for ltr in range(3):
            if(word[ltr:ltr + 2] == letters): #take the letter and the character after it "from the stack overflow (sourse)[https://stackoverflow.com/questions/1162592/iterate-over-a-string-2-or-n-characters-at-a-time-in-python]"
                count +=1
                break


    for ltr in word:
        if(ltr==letters):
            count+=1
    print(count)


occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0