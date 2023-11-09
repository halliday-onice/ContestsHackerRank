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
lineperline = 0
ans = 0
get_bigger_by_col_list = [] #lista que guarda os itens da matrix
isAllOhList = [] * d
for j in range(d):
    countohs = 0 #precisa resetar a contagem dos ohs por coluna
    lineperline = 0 #precisa ser resetada para zero
    isAllOh = False
    print("column", j + 1)
    countColMax = 0
    for i in range(len(matrix)):# o len(matrix) me devolve o numero de linhas
        if matrix[i][j] == 'o': #verifica onde tem o
            countohs += 1
            countColMax += 1
            isAllOh = True #isso sempre vai a
            if isAllOh == True:
                isAllOhList.append(1)
            #print(matrix[lineperline][j])
            #print("line",lineperline)
            print("count ohs:",countohs)
        get_bigger_by_col_list.append(countohs)
        
    #print("CountColMax",countColMax)
    #print("LISTALL OHS", isAllOhList)
print("\n")

print(isAllOhList)

print("get max counts by column", max(get_bigger_by_col_list))


