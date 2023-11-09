# there are N people numbered from 1 to N
#there is a schedule for the following D days
#essa escala eh representada por uma String Si de tamanho D
#Se o j-esimo caractere de Si eh o, a pessoa i esta livre no j-esimo dia
#se tiver x entao a pessoa esta ocupada naquele dia

#basicamente recebe a linha e a coluna de uma matriz

n, d = map(int, input().split())
#d = int(input()) #columns
#print(n, d)

#I want to use a numpy for better performance

matrix = []
for i in range(n):
   line = input()
   matrix.append(line)
#print(matrix)



countohs = 0
#varrer por colunas primeiro
consec_list = []
for j in range(d):
    check_Free = 1
    for i in range(len(matrix)):# o len(matrix) me devolve o numero de linhas
        occur = matrix[i][j]
        if occur == 'x':
            check_Free = 0
            break
    if check_Free == 1:
        #se o check Free for igual a 1, isso significa que toda a coluna eh 1
        consec_list.append(j + 1)
        #print(j)

if len(consec_list) == 0:
    print(0)
counter = 1
ultimate = 1
for i in range(len(consec_list) - 1):
    #o menos um eh pra percorrer corretamente as linhas
    occur = consec_list[i]
    next_occur = consec_list[i + 1]
    if occur + 1 == next_occur: # aqui estou checando se um eh consecutivo ao outro
        counter += 1
    else:
        counter = 1
    ultimate = max(counter, ultimate)
    #print("LISTALL OHS", isAllOhList)

print(ultimate)
