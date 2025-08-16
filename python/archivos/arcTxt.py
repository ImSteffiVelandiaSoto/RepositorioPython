n=int(input('digite un numero del 1 al 10 para generar la tabla'))

nombre_fichero='tabla' + str(n)+ '.txt'

f=open(nombre_fichero,'w')

for i in range(1,11):
    f.write(str(n)+ 'x' + str(i) +'=' + str(n*i) +'\n')

f.close()