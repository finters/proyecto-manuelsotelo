class pagos_y_ventas:
    def __init__(self):
        pass

    def registrar_pagos(clientes:list):
        x=input("ingrese el nombre el cliente quien hizo un pago")
        busqueda=False
        for i in clientes:
            if x==i[0]:
                busqueda=True
        if busqueda ==False:
            print("no se encontro el cliente")
            pass
        