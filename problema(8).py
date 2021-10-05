ope= input("ingrese la operacion: ")
a = int (input("ingrese el valor de a: "))
b = int (input("ingrese el valor de b: "))
if ope ==' s' :
    print("la suma es: ", a+b)
elif ope ==' r' :
    print("la resta es:", a-b )
elif ope == ' m'  :
       print("la multiplicacion es:", a*b )
elif ope == ' d'  and b !=0 :
       print("la division es:", a/b )       
else:
    print("error")


