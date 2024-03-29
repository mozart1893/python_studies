# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


fname = input("Enter file name: ")
fh = open(fname)
alist = []
for line in fh:
    sline = line.split()
    # sorline = sline.sort()
    for word in sline:
        if word in alist:
            continue
        alist.append(word)
        alist.sort()
print(alist)


# lst = list()
# for line in fh:
# print(line.rstrip())


# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
