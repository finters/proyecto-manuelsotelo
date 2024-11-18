
class client:
    def __init__(self, cliente):
        self.cliente=cliente
    
    
    
    def add_client(lista_clientes:list): #añade un cliente a la lista

        
        while True:
            response=input("""¿el cliente usa cedula o RIF?
                    1. cedula de indentidad
                    2. RIF 
                    
                    ---->: """)
            juridico=None
            if response == "1":
                while True:
                    b=input("ingrese el numero de cédula sin puntos o espacios: ")
                    try:
                        int(b)
                        break
                    except Exception: print("siga las indicaciones por favor")
                b="V-"+b
                juridico=False
                break
            
            if response == "2":
                while True:
                    b=input("ingrese solo las cifras del RIF: ")
                    try:
                        int(b)
                        break
                    except Exception: print("siga las indicaciones por favor")
                b="J"+b
                juridico=True
                break
            
            else: print("""entradad inválida, ingrese 1 para indicar si usa 
                       cédula o 2 si usa su RIF""")    
            
        data=[ #data=[nombre, cedula o rif, correo, direccion, telefono,(contactos)]
            input("ingrese el nombre o Razon social del cliente: "),
            b,    
            input("correo electronico del cliente :"),
            input("direccion de envio: "),
            input("Numero de telefono: "),
            juridico,
            ]
        
        
        if juridico == True:
            print("indique los datos del  contacto de alguien")
            j=[
            input("nombre y apellido: "),
            input("correo electronico: "),
            input("Numero de telefono: "),
            ]
            data.append(j)
        lista_clientes.append(data)
        
        
        
    def modificar_cliente(lista_clientes:list): #modifica los datos de los clientes
        while True:
            while True:
                Response=input("""
                            El cliente a modificar esta registrado con su CI o su RIF?
                            1. Cedula
                            2. RIF
                            --->: """)
                try: 
                    int(Response)  
                    break
                except Exception:
                    print("entrada invalida")
            
            if Response=="1":
                juridico=False
                sample="la cedula"
                break
            elif Response=="2":
                juridico==True
                sample="el RIF"
                break
            else: print("Entrada Invalida")
        while True:
            id=input(f"""Ingrese {sample} del cliente a modificar
                     sin puntos, letras o guiones""")
            try: 
                    id=int(id)  
                    break
            except Exception:
                print("Formato inválido")
        
        for person in lista_clientes:
            if person[1]=="V-"+id or "J"+id:
                result=person
        try:
            while True:
                if juridico==True:
                    sub_index=int(input(f""" 
                                    que desea modificar?
                                
                                1 -> nombre                         {result[0]}
                                2 -> cedula                         {result[1]}
                                3 -> email                          {result[2]}
                                4 -> direccion                      {result[3]}
                                5 -> telefono                       {result[4]}
                                6 -> datos de contacto              {result[5]}
                                
                                0--> salir
                                --->: """))
                
                elif juridico==False:
                   sub_index=int(input(f""" 
                                    que desea modificar?
                                
                                1 -> nombre                         {result[0]}
                                2 -> cedula                         {result[1]}
                                3 -> email                          {result[2]}
                                4 -> direccion                      {result[3]}
                                5 -> telefono                       {result[4]}
                                
                                0--> salir
                                --->: """))
                if sub_index==1:
                    result[0]=input("ingrese el nuevo nombre: ")
                    
                elif sub_index==2:
                    if juridico==True:
                        while True:
                            a=input("ingrese el nuevo RIF: ")
                            try:
                                a=int(a)
                                break
                            except Exception:
                                print(" ingrese solo números ")
                            
                        result[1]="j"+ a
                        
                    elif juridico==False:
                        while True:
                            b=input("ingrese la nueva cedula: ")
                            try:
                                b=int(b)
                                break
                            except Exception:
                                print(" ingrese solo números ")
                        result[1]="V-"+ b
                        
                elif  sub_index==3:
                    result[2]=input("ingrese el nuevo email: ")
                
                elif sub_index==4:
                    result[3]=input("ingrese la nueva direccion: ")
                    
                elif sub_index==5:
                    result[4]=input("ingrese el nuevo numero de telefono")
                
                elif sub_index==6 and juridico==True:                    
                    result[5]=[
                    input("ingrese el nuevo nombre de la persona de contacto"),
                    input("ingrese el nuevo numero de telefono de contacto"),
                    input("ingrese el nuevo correo de contacto")
                    ]
                    
                elif sub_index==6 and juridico==False:
                    print("entrada invalida")
                elif sub_index==0:
                    break
                
                else: print("entrada invalida")
        except Exception:
                print("entrada invalida")
    
    def remove_client(lista_clientes:list): #elimina un cliente de la lista mediante su ID

        while True:
            respoponse=input("""
                            el cliente esta registrado con su RIF o Cedula?
                            1. RIF
                            2. Cedula
                            
                            ------>: """)
            try: 
                respoponse=int(respoponse)  
                break
            except Exception:
                print("entrada invalida")
            
        verdugo=input("ingrese las cifras de la cédula o el RIF a eliminar (por ejemplo; 11222333 ): ")
        confirmador=0
        
        if respoponse==1:
            for i in lista_clientes:
                if verdugo in i[1]:
                    confirmador+=1
                    print(f"se ha eliminado el cliente con la cedula {i[0]}")
                    lista_clientes.pop(i)
                    
        elif respoponse==2:
            for i in lista_clientes:
                if verdugo in i[1]:
                    confirmador+=1
                    print(f"se ha eliminado el cliente {i[0]} con la cedula {i[1]} ")
                    lista_clientes.remove(i)
                    
        if confirmador==0:
            print("no se encontró el cliente")
            
    def buscar_cliente_cedula(lista_clientes:list):
        while True:
            respoponse=input(""" Ingrese la cedula a buscar:
                                                      
                            ------>: """)
            try: 
                int(respoponse)  
                break
            except Exception:
                print("entrada invalida")
        confirmador=0
        for i in lista_clientes:
            if respoponse in i[1] and i[5]==False:
                print(f"""
                      ---------------------------
                      nombre:           {i[0]}
                      RIF:              {i[1]}
                      email:            {i[2]}
                      direccion:        {i[3]}
                      telefono:         {i[4]}""")
                confirmador+=1
                
        if confirmador==0:
            print(" ")
            print("no se encontraron coincidencias")


    def buscar_cliente_rif(lista_clientes:list):
        while True:
            respoponse=input(""" Ingrese el RIF a buscar:
                                                      
                            ------>: """)
            try: 
                int(respoponse)  
                break
            except Exception:
                print("entrada invalida")
        confirmador=0
            
        for i in lista_clientes:
            if respoponse in i[1] and i[5]==True:
                print("resultados:  ")
                print(f"""
                      ---------------------------------
                      nombre:           {i[0]}
                      RIF:              {i[1]}
                      email:            {i[2]}
                      direccion:        {i[3]}
                      telefono:         {i[4]}
                            contactos
                            nombre:          {i[6][0]}   
                            email:           {i[6][1]}   
                            telefono:        {i[6][2]}   
                      """)
                confirmador+=1
                
        if confirmador==0:
            print(" ")
            print("no se encontraron coincidencias")
                
    def buscar_cliente_email(lista_clientes:list):
        respoponse=input(""" Ingrese el email a buscar:
                                                      
                            ------>: """)
        confirmador=0
        for i in lista_clientes:
            if i[5]==False and respoponse in i[2]:
                print(f"""
                    ----------------------------
                    nombre:           {i[0]}
                    RIF:              {i[1]}
                    email:            {i[2]}
                    direccion:        {i[3]}
                    telefono:         {i[4]}""")
                confirmador+=1
            
            elif i[5]==True and respoponse in i[2]:
                print("resultados:  ")
                print(f"""
                    ---------------------------------
                    nombre:           {i[0]}
                    RIF:              {i[1]}
                    email:            {i[2]}
                    direccion:        {i[3]}
                    telefono:         {i[4]}
                            contactos
                            nombre:          {i[6][0]}   
                            email:           {i[6][1]}   
                            telefono:        {i[6][2]}   
                    """)
                confirmador+=1

        if  confirmador==0:
            print(" ")
            print("no se encontraron coincidencias")