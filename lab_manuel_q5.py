n=int(input("Enter number of rows:"))
mat=[]
for i in range(n):
    row=[int(x) for x in input(f"Enter row{i+1}:").split()]
    mat.append(row)
k=int(input("Enter k:"))
mat[k-1]=mat[k-1][::-1]
print("Modified Matrix:")
for row in mat:
    print(row)