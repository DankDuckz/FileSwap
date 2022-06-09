def swapFile(file1,file2):
    fileA = open(file1)
    fileB = open(file2)

    dataA = fileA.read()
    dataB = fileB.read()

    fileAWrite = open(file1,'w')
    fileBWrite = open(file2,'w')

    fileAWrite.write(dataB)
    fileBWrite.write(dataA)

input1 = input("Which file would you like to swap?")
input2 = input("Which file would you like to swap that file with?")

swapFile(input1,input2)
#\Users\singgurung\Documents\Coding\project98\text1.txt
#\Users\singgurung\Documents\Coding\project98\text2.txt