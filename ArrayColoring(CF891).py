#rule to change the parity
#par + par = par
#par + impar = impar => 2x + 2y + 1=> 2(x + y)+ 1=> 2z + 1
#impar + impar = par => 2x + 1 + 2y + 1=> 2z + 2 =>2(z + 1) 2w


#T teste de casos
#n is the array length
# the integers itself
#colorarr

t = int(input())
#colorarr = []
for test in t:
      n = int(input())
      sum = 0
      colorarr = list(map(int, input().split()))
      for v in colorarr: #l stands for len
            if v % 2 != 0: # se for impar, parity changes
                  sum += 1
      if sum % 2 == 0:
            print("yes")
      else:
            print("no")
