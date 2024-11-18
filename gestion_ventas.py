
class ventas:
 def __init__(self):
  pass

def registrar_venta(objetos:list,clientes:list):
    nombre_cliente=input("ingrese el nombre del cliente: ")
    for i in clientes:
        if i[0] == nombre_cliente:
            name=i[0]
            juri=i[5]
    while True:
        while True:
            print(" ")
            compra=input("ingrese el ID del objeto comprado o ingrese el numero 0 para finalizar: ")
            try:
                compra=int(compra)
                break
            except Exception:
                print("no es un numero")
        
        carrito=[]
        cantidad_obj=[]
        subtotal=0
        for i in objetos:
            if i[0]==compra:
                while True:
                    print(" ")
                    cantidad=input("cuantos se compraron?: ")
                    try:
                        cantidad=float(cantidad)
                        break
                    except Exception: print("no es un numero")
                i[5]-=cantidad
                subtotal+=i[3]*cantidad
                cantidad_obj.append([i[1],cantidad])
        break        
                
                
           
    [name,
    productos,
    
    ]
    
registrar_venta()