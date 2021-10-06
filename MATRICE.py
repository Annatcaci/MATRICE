A=[[2,3,6,7,9],
   [4,7,1,3,8],
   [6,0,3,2,6],
   [5,3,7,1,3],
   [3,5,1,7,8]]
print(A)
print("Suma primului rand:", sum(A[0]))
print("Suma al doilea rand:", sum(A[1]))
print("Suma al treilea rand:", sum(A[2]))
print("Suma al patrule rand:", sum(A[3]))
print("Suma al cincilea rand:", sum(A[4]))


col1=[]
for i in A:
    col1.append(i[0])
col2=[]
for i in A:
    col2.append(i[1])
col3=[]
for i in A:
    col3.append(i[2])
col4=[]
for i in A:
    col4.append(i[3])
col5=[]
for i in A:
    col5.append(i[4])
print("Suma primei coloane:", sum(col1))
print("Suma coloanei a doua:", sum(col2))
print("Suma coloanei a treia:", sum(col3))
print("Suma coloanei a patra:", sum(col4))
print("Suma coloanei a cincia:", sum(col5))

diagonala_p=[A[i][i] for i in range(len(A))]
diagonala_s=[A[len(A)-1-i][i] for i in range(len(A)-1,-1,-1)]
print("Diagonala principala: ",diagonala_p)
print("Diagonala secundara: ",diagonala_s)

