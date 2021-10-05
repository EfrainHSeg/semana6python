monto = int (input("ingrese monto "))
if monto< 100:
    print("no hay comision ")
else: 
    if monto < 300:
        print("la comision es: " , monto *0.1) 
    else:
        print("la comision es: ", monto * 0.2)     