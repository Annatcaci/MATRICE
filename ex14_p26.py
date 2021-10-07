A=[]
n=int(input("Introduceti numarul inclus intre(sau egal) 2 si 10 de randuri si coloane: "))
if 2<=n<=10:
    print("Introduceti elementele matricei:")
    for rand in range(0,n):
        rand=[]
        for i in range(0,n):
            i=int(input())
            rand.append(i)
        A.append(rand)
    print(A)

    diagonala_s=[A[len(A)-1-i][i] for i in range(len(A)-1,-1,-1)]
    diagonala_p=[A[i][i] for i in range(len(A))]
    
    maisusdedigonala_p=[]
    maijosdedigonala_p=[]
    maisusdedigonala_s=[]
    maijosdedigonala_s=[]
    for i in range(len(A)):
        
        for j in range(len(A[0])):
            if i<j:
                maisusdedigonala_p.append(A[i][j])
            if i>j:
                maijosdedigonala_p.append(A[i][j])
            if (i+j)<(len(A)-1):
                maisusdedigonala_s.append(A[i][j])
            if (i+j)>(len(A)-1):
                maijosdedigonala_s.append(A[i][j])

    print("Suma elementelor a diagonalei principale: ", sum(diagonala_p))      
    print("Suma elementelor a diagonalei secundare: ", sum(diagonala_s))
    print("Suma elementelor  de sus a diagonalei principale: ", sum(maisusdedigonala_p))
    print("Suma elementelor de jos a diagonalei principale: ", sum(maijosdedigonala_p))
    print("Suma elementelor de sus a diagonalei secundare: ", sum(maisusdedigonala_s))
    print("Suma elementelor de jos a diagonalei secundare: ",sum(maijosdedigonala_s))

else:
    print("Numarul introdus nu corespunde cerintelor. Verificati cerintele!")