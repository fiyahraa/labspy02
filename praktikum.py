a = int (input ("masukan bilangan ke 1 : "))
b = int (input("masukan bilangan ke 2 : "))
c = int (input ("masukan bilangan ke 3 : "))

print ("bilangan ke 1 = ", a)
print ("bilangan ke 2 = ", b)
print ("bilangan ke 3 = ", c)

if a > b > c :
    print ("urutan bilangan : ",a,b,c)

if a > b < c :
    print ("urutan bilangan :" ,a,c,b)


if a < b > c > a :
    print ("urutan bilangan :" ,b,c,a)    

if a < b > c < a :
    print ("urutan bilangan :" ,b,a,c) 



if a < b < c > a :
    print ("urutan bilangan :" , c,b,a) 

if c > a > b :
    print ("urutan bilangan :", c,a,b)




if a > b == c :
    print ("urutan bilangan = ", a,b,c)

if b > a == c :
     print ("urutan bilangan = ", b,a,c)

if c > a == b :
    print ("urutan bilangan = ", c,a,b)
    

