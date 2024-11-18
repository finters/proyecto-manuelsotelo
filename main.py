from gestion_productos import productos 
from gest_cliente import client


import requests
import json



#DATOS DE LOS CLIENTES
clientes_list=[]
registro_venta=[]
#-------------------

#DATOS DEL INVENTARIO
cuenta_ID=0
inventario_total=[]
#-------------------

def empaquetador_inventario(data): #constructor de lista de diccionarios de los objetos
  pacage=[]
  for i in data:
    pacage.append({
    "id":i[0],
    "name":i[1],
    "description":i[2],
    "price":i[3],
    "category":i[4],
    "inventory":i[5],
    "compatible_vehicles":i[6]
    })
  return pacage

def empaquetador_clientes(data:list):  #constructor de lista de diccionarios de los clientes
  package=[]
  for i in data:
    if i[5]==True:
      package.append({
      "nombre":i[0],
      "ID":i[1],
      "Email":i[2],
      "direccion":i[3],
      "Telefono":i[4],
      "Juridico":i[5],
      "Contactos":i[6]
      })
     
    elif i[5]==False:
      package.append({
      "nombre":i[0],
      "ID":i[1],
      "Email":i[2],
      "direccion":i[3],
      "Telefono":i[4],
      "Juridico":i[5]
      })
  return package

def desconstructor_inventario(inventario): #prepara los datos en crudo de la lista del json de objetos para usarlos en el código
  data=[]
  for i in inventario:
    a:str=i.get("id")
    b:str=i.get("name")
    c:str=i.get("description")
    d:int=i.get("price")
    e:str=i.get("category")
    f:int=i.get("inventory")
    g:list=i.get("compatible_vehicles")
    data.append([a,b,c,d,e,f,g])
  return data

def descontructor_clientes(data:list):  #prepara los datos de la lista en crudo del json de los clientes para usarlos en el código
  package=[]
  for i in data:
    i:dict
    algo=i.get("Juridico")
    if algo==True:

        a:str=i.get("nombre")
        b:str=i.get("ID")
        c:str=i.get("Email")
        d:int=i.get("direccion")
        e:str=i.get("Telefono")
        f:int=i.get("Juridico")
        g:list=i.get("Contactos")
        package.append([a,b,c,d,e,f,g])
     
    elif algo==False:

        a:str=i.get("nombre")
        b:str=i.get("ID")
        c:str=i.get("Email")
        d:int=i.get("direccion")
        e:str=i.get("Telefono")
        f:int=i.get("Juridico")
        package.append([a,b,c,d,e,f])
  return package


#-----------------------------

########API#########################
def api_url():#baja la api
    api=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json")
    datos: list=api.json()
    return datos
#___________________________
def numero_id(inventario): #baja el contadpr de objetos creados
  try:
    with open('numero.txt', 'r', encoding='utf-8') as file:     
            numero=int(file.read().strip())
            return numero
  except Exception:
    with open('numero.txt', 'w', encoding='utf-8') as file:
      file.write(str(len(inventario)))
    return len(inventario)
########JSON##################
def extractor_client():
  try:
    with open('clientes.json',"r",encoding="utf-8") as file:
          datos = json.load(file)
    return datos
  except Exception:
    datos=[]
    with open('inventario.json',"w",encoding="utf-8") as file:
        json.dump(datos, file, ensure_ascii=False,indent=4)
    return datos    

def extractor_clientes():
  try:
    with open('ventas.json',"r",encoding="utf-8") as file:
          datos = json.load(file)
    return datos
  except Exception:
    datos=[]
    with open('ventas.json',"w",encoding="utf-8") as file:
        json.dump(datos, file, ensure_ascii=False,indent=4)
    return datos 

def datos_del_json():#intenta leer el json de los objetos, si falla baja la api y lee sus datos
    try:
        with open('inventario.json',"r",encoding="utf-8") as file:
            datos = json.load(file)
        
        return datos
    except Exception:
        datos=api_url()
        with open('inventario.json',"w",encoding="utf-8") as file:
            json.dump(datos, file, ensure_ascii=False,indent=4)
    return datos 
#------------------------------
def guardado_de_datos(invetario:list,inventario_ID:list,clientes:list): #guarda los datos de los objetos y los clientes
  with open('inventario.json',"w",encoding="utf-8") as file:
    json.dump(invetario, file, ensure_ascii=False,indent=4)
    
  with open('numero.txt', 'w', encoding='utf-8') as file:
      file.write(str(inventario_ID))
      
  with open('clientes.json',"w",encoding="utf-8") as file:
    json.dump(clientes, file, ensure_ascii=False,indent=4)
 
  

##############-Iniciador-################
inventario_total=datos_del_json()
clientes_list=extractor_client()
cuenta_ID=numero_id(inventario_total)
inventario_total=desconstructor_inventario(inventario_total)
clientes_list=descontructor_clientes(clientes_list)
###############-Iniciador-################

#####--bucle_menu--####
while True:
  while True:
    a=input(""" que desea hacer?
          1. Gestionar Productos
          2. Gestionar Clientes
          3. Gestionar Ventas
          4. Gestionar Pagos
          5. Gestionar Envios
          6. Revisar Estadisticas generales
          
          0. Salir y gaurdar
          (ingrese solo UN número respectivo a una categoria por favor)
          ------>: """)
    try:
      a=int(a)
      if a < 7:
        break
      else: print("entrada inválida")
    except Exception: print("entrada inválida")
  
  if a ==1:  #gestion productos
    print(" ")
    while True:
      while True:
        b=input(""" que desea hacer?
            1. Agregar Productos
            2. Modificar datos de un producto
            3. Buscar por precio
            4. Buscar por nombre
            5. Buscar por categoria
            6. Buscar por cantidad Min. de inventario disponible
            7. Eliminar un objeto
            
            0. Atrás
            (ingrese solo UN número respectivo a una categoria por favor)
            ------>: """)
        try:
          b=int(b)
          if b < 8:
            break
          else: print("entrada inválida")
        except Exception: print("entrada inválida")
        
      if b==1:
        productos.agregar(inventario_total, cuenta_ID)
        cuenta_ID+=1

      elif b==2:
        productos.modificar_datos(inventario_total)
      
      elif  b==3:
        productos.busqueda_price(inventario_total)
        
      elif b==4:
        productos.busqueda_nombre(inventario_total)
        
      elif  b==5:
        productos.busqueda_category(inventario_total)
        
      elif b==6:
        productos.busqueda_inventory(inventario_total)
        
      elif b==7:
        productos.eliminar_objeto(inventario_total)
        
      elif b==8:
        break

  elif a==2: ### gestion de clientes
    while True:
      while True:
        b=input(""" 
                que desea hacer? 
            1. Agregar cliente
            2. Modificar datos de un cliente
            3. Buscar por cedula
            4. Buscar por rif
            5. Buscar por correo electronico
            6. Eliminar un cliente
            
            0. Atrás
            (ingrese solo UN número respectivo a una categoria por favor)
            ------>: """)
        try:
          b=int(b)
          if b < 7:
            break
          else: print("entrada inválida")
        except Exception: print("entrada inválida")
        
        
      if b==1:


        client.add_client(clientes_list)
        
      elif b==2:
        client.modificar_cliente(clientes_list)
        
      elif b==3:
        client.buscar_cliente_cedula(clientes_list)
        
      elif b==4:
        client.buscar_cliente_rif(clientes_list)
      
      elif b==5:
        client.buscar_cliente_email(clientes_list)
        
      elif b==6:
        client.remove_client(clientes_list)
        



      elif b==0:
        break







  elif a==0: ##salir del menu y proceder con el guardado y cerrado del programa
    break







###########-Finalizador-##################
print("Vuelva Pronto")
guardado_de_datos(empaquetador_inventario(inventario_total),cuenta_ID,empaquetador_clientes(clientes_list))


