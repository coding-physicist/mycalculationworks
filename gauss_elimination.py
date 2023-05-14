import numpy as np
rows=int(input('Enter number of rows: '))
cols=int(input('Enter number of coloumns: '))
mat=np.zeros((rows,cols))
for i in range (0,rows):
    for j in range (0,cols):
        mat[i,j]=float(input('Enter element: '))

mat2=np.zeros((rows,1))
for i in range (0,rows):
    mat2[i,0]=float(input('Enter element on mat 2: '))

main_mat=np.hstack((mat,mat2))
if np.linalg.det(mat)==0:
  print("\n\n\n\t\t\t\tNO EXACT SOLUTION\n\n")
  exit()

print('main_mat= \n',main_mat)
def exchange(main_mat,x,y,z):
    rplc=np.zeros((1,y))
    k=cols+1-y
    for j in range (0,y):
        rplc[0,j]=main_mat[x,j+k]
        main_mat[x,j+k]=main_mat[z,j+k]
        main_mat[z,j+k]=rplc[0,j]

for l in range (0,rows):
  for m in range (l, rows):
    if abs(main_mat[l,l])<abs(main_mat[m,l]):
      exchange(main_mat=main_mat,x=l,y=cols+1-l,z=m)
  for k in range (l+1,rows):
    factor=main_mat[k,l]/main_mat[l,l]
    for i in range (l,cols+1):
     main_mat[k,i]=main_mat[k,i]-(main_mat[l,i]*factor)

xx=np.zeros((1,rows))
for i in range (0,cols):
 product=np.multiply(main_mat[rows-i-1,0:cols],xx)
 xx[0,cols-1-i]=(main_mat[rows-i-1,cols]-np.sum(product))/main_mat[rows-i-1,cols-i-1]
print(main_mat)
print('\nsolution=',xx)


