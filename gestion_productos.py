

class productos:
  def __init__(self,name,description,price,category,inventory,compatible_vehicles,):
    self.name=name
    self.description=description
    self.price=price
    self.category=category
    self.inventory=inventory
    self.compatible_vehicles=compatible_vehicles


#agregado
  def agregar(inventario:list, tamaño_del_inventario:int):#funciona, bonito output, aprueba de errores
    try: a=float(input("precio del objeto: "))

    except Exception:
      a=50.0
      print(f"""entrada invalida, se seleccionó automaticamente que tiene un precio de 50.0
              para modificar esto debe modificar el objeto con el ID Nº{tamaño_del_inventario+1}""")
      
    try: b=int(input("objetos disponibles a la venta: "))
    except Exception:
      b=50.0
      print(f"""entrada invalida, se seleccionó automaticamente que tiene una desponibilidad de 100 unidades
              para modificar esto debe modificar el objeto con el ID Nº{tamaño_del_inventario+1}""")
      
    nuevo_objeto: list=[
    tamaño_del_inventario+1,
    input("nombre del objeto: "),
    input("descripcion del objeto :"),
    a,    
    input("categoria del objeto: "),
    b,
    []
          ]
    respuesta=input("""
                    desea especificar los vehiculos compatibles con el objeto?
                    de no especificar se considerara comparible con todo tipo de vehiculo
                    "si" o "no": """)
    if respuesta=="no":
      nuevo_objeto[6]="todos"
      inventario.append(nuevo_objeto)
      
      
    elif respuesta=="si":
      try:
        cantidad=int(input("cuantos vehiculos desea añadir?: "))
        n=0
        while n<cantidad:
          nuevo_objeto[6].append(input(f"especifique el vehiculo compatible Nº{n+1}: "))
          n+=1
        inventario.append(nuevo_objeto)
        
          
      except Exception:
        print(f"""entrada invalida, se seleccionó automaticamente que es compatible con todos los vehiculos
              para modificar esto debe modificar el objeto con el ID Nº{tamaño_del_inventario+1}""")
        nuevo_objeto[6]="todos"
        inventario.append(nuevo_objeto)
        
        
    else: 
      print(f"""entrada invalida, se seleccionó automaticamente que es compatible con todos los vehiculos
              para modificar esto debe modificar el objeto con el ID Nº{tamaño_del_inventario+1}""")
      nuevo_objeto[6]="todos"
      inventario.append(nuevo_objeto)

    
  #agregado
  def busqueda_category(inventario: list):# funciona, enbellecer output, aprueba de errores
    results=[]
    category=input("ingrese una categoria a buscar: ")
    for i in inventario:
      if category in i[4]:
        results.append(i)
        
    if len(results)>0:
      print("los objetos que satisfacen la busqueda son:")
      for i in results:
        print(f"""
              ID:                        {i[0]}
              Nombre:                    {i[1]}
              Descripción:               {i[2]}
              Precio:                    {i[3]}
              Category:                  {i[4]}
              Inventario:                {i[5]}
              Vehiculos compatibles:     {i[6]}
              """)
        
    else: print("no se encontró ninguna coincidencia")
    
  #agregado 
  def busqueda_price(inventario: list):# funciona, enbellecer output, aprueba de errores
    results=[]
    filtro=[float(input("ingrese un precio minimo de busqueda: ")),float(input("ingrese un precio maximo de busqueda: "))]
    for i in filtro:
      if i<0:
        i*=-1
    filtro.sort()
    precio_min=filtro[0]
    precio_max=filtro[1]
    
    for i in inventario:
      if i[3]>=precio_min and i[3]<=precio_max:
        results.append(i)
        
        
    if len(results)>0:
      print("los objetos que satisfacen el rango de precio:")
      for i in results:
        print(f"""
              ID:                        {i[0]}
              Nombre:                    {i[1]}
              Descripción:               {i[2]}
              Precio:                    {i[3]}
              Category:                  {i[4]}
              Inventario:                {i[5]}
              Vehiculos compatibles:     {i[6]}
              """)
        
    else: print("no se encontró ninguna coincidencia")
  
  #agregado
  def busqueda_inventory(inventario: list):# busqueda por disponibilidad minima de un objeto--->objetos con un invenatrio mayor o igual al input
    results=[]
    try:
      cantidad=int(input("ingrese una cantidad de inventario minima: "))
      if cantidad < 0:
        cantidad*=-1
      for i in inventario:
        if i[5]>=cantidad:
          results.append(i)
          
      if len(results)>0:
        print(f"los objetos que tienen una disponibilidad de {cantidad} o mayor son: ")
        for i in results:
          print(f"""
              ID:                        {i[0]}
              Nombre:                    {i[1]}
              Descripción:               {i[2]}
              Precio:                    {i[3]}
              Category:                  {i[4]}
              Inventario:                {i[5]}
              Vehiculos compatibles:     {i[6]}
              """)
      else: print("no se encontró ninguna coincidencia")    
    
    except Exception:
      print("ingrese solo números porfavor")
        
  #agregado
  def busqueda_nombre(inventario: list): #busqueda por simulitud-->todos los objetos que contengan el input dentro del nombre
    results=[]
    nombre=input("ingrese una palabra o silaba para buscar similares: ")
    for i in inventario:
      if nombre in i[1]:
        results.append(i)
      
    if len(results)>0:
      print("los objetos que se llaman asi son: ")
      for i in results:
        print(f"""
              ID:                        {i[0]}
              Nombre:                    {i[1]}
              Descripción:               {i[2]}
              Precio:                    {i[3]}
              Category:                  {i[4]}
              Inventario:                {i[5]}
              Vehiculos compatibles:     {i[6]}
              """)
      
    else: print("no se encontró ninguna coincidencia")
    
 #agregado
  def modificar_datos(inventario: list):    #pregunta que objeto modificar, selecciona un atributo a modificar, sustituye el objeto original por el modificado
    try:
      busqueda_indx =int(input("ingrese el ID sel objeto a modificar: "))        
      try:
        while True:
          result=None
          
          for i in inventario:
            if i[0]==busqueda_indx:
              result=i
          
          if result==None:
            raise
            
          sub_index=int(input(f""" 
                            que desea modificar?
                        
                        1 -> nombre                         {result[1]}
                        2 -> descripcion                    {result[2]}
                        3 -> precio                         {result[3]}
                        4 -> categoria                      {result[4]}
                        5 -> disponibilidad de inventario   {result[5]}
                        6 -> vehiculos compatibles          {result[6]}
                        
                        7--> salir
                        --->: """))
          
          if sub_index==1:
            result[1]=input("ingrese los nuevos datos: ")
            
            
          elif sub_index==2:
            result[2]=input("ingrese los nuevos datos: ")
            
            
          elif sub_index==3:
            try:
              result[3]=float(input("ingrese los nuevos datos: ")) 
            except Exception: print("dato inválido")
            
          elif sub_index==4:
            result[4]=input("ingrese los nuevos datos: ")
            
            
          elif sub_index==5:
            result[5]=int(input("ingrese los nuevos datos: "))
            
            
          elif sub_index==6:
            result[6]=input("ingrese los nuevos datos: ")
            
          elif sub_index==7:
            break
                
          elif sub_index>7:
            print("ingrese solo numeros del 1 al 6")
            return
            
      except Exception:
        print("ID no encontrada")
        return
      
    except Exception:
      print("ID invalida")
      
      
 #agregado
  def eliminar_objeto(inventario:list):
    while True:
      verdugo=input("Ingrese el ID del objeto que desee eliminar: ")
      try: 
        verdugo=int(verdugo)
        break
      except Exception:
        print("entrada invalida")
    for i in inventario:
      if i[0]==verdugo:
        print(f"se ha eliminado el objeto con ID {inventario[i]}")
        inventario.pop(i)
    