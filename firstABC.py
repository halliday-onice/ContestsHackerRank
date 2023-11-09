stringLen = int(input())
str = input()


#print("Quantidade de A: ", countA)
#
#
countA = 0
countB = 0
countC = 0
#print("string len", range(stringLen))
for i in range(stringLen):
    #print("i",i)
    if(str[i] == 'A'):
      countA = str.count('A')
    if(str[i] == 'B'):
      countB = str.count('B')
    if(str[i] == 'C'):
      countC = str.count('C')
    if(countA and countB and countC >=1):
      break
print(i + 1)

#print("countA",countA)
#print("countB",countB)
#print("countC",countC)