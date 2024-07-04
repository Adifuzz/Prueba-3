import os 
import random 
os.system ("clear") 

def validar_nif(nif): 
    if len(nif) != 12: 
     return False 
    if nif[-4] != "-":  
        return False 
    numeros = "123456789" 
    for digito in nif[:7] :
        if digito not in numeros: 
            return False 
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    #for a in nif[:-3].upper(): 
     #   if a not in letras: 
      #      return False 
    return True
    
def validar_nombre(nombre): 
    if len(nombre) < 8 or nombre == "" or nombre == " ": 
        return False 
    return True 

def validar_edad(edad): 
    if edad <= 15: 
        return False 
    return True
    

identificacion = []
def grabar(): 
    nif = input("ingrese NIF\n") 
    while not validar_nif(nif): 
        nif = input("NIF incorrecto, vuelva a intentarlo: ")
    nombre = input("ingrese nombre y apellido: ") 
    while not validar_nombre(nombre): 
        nombre = input("nombre no valido, vuelva a intentarlo: ") 
    edad = int(input("ingrese edad: "))
    while not validar_edad(edad): 
        edad = int(input("edad no valida, vuelva a intentarlo"))  
    #while loop == True:
    op_ec = (input(""" 
         Ingrese opcion de estado conyugal 
         1. Soltero/a 
         2. Casado/a 
         3. Separado/a 
         4. Viudo/a 
         \n"""))    
    if op_ec == "1" : 
            ec = "soltero/a"  

    elif op_ec == "2": 
            ec = "Casado/a" 
    elif op_ec == "3": 
            ec = "Separado/a"  
    elif op_ec == "4": 
            ec = "Viudo/a"  
    else: 
            print("opcion no valida")  
    for letra in nif:   
        if (nif[:-2]) == "sp" or nif[:-2] == "SP": 
            nacionalidad = "España" 
        else: 
            nacionalidad = "Union Europea" 

    registro = { 
     "NIF": nif, 
     "Nombre": nombre, 
      "Edad": edad, 
     "Estado conyugal": ec, 
     "Nacionalidad": nacionalidad  
    }  

    identificacion.append(registro)  
    print ("registro completo")  

def buscar(): 
    nif_buscar = input("ingrese NIF a buscar") 
    encontrado = False  
    for registro in identificacion: 
         if registro["NIF"]== nif_buscar: 
              print("Registro: ") 
              print(f"NIF: {registro["NIF"]}")
              print(f"Nombre: {registro["Nombre"]}") 
              print(f"Edad: {registro["Edad"]}") 
              print(f"Estado Conyugal {registro["Estado conyugal"]}")
              print(f"Nacionalidad {registro["Nacionalidad"]}") 
              encontrado = True 
              break 
    if not encontrado: 
         print("NIF no encontrado") 
def valor(valor_certificado): 
     total_certificado += valor_certificado 

     

def imprimir_certificados():  
    val_valor() 
    print(""" 
           Imprimir :
           1. certificado de nacimiento 
           2. estado conyugal 
           3. pertenencia Union Europea 
           """) 
    op_imprimir = input("Que indica la opcion: ") 
    if op_imprimir == "1": 
     for registro in identificacion:
        print("certificado de nacimiento") 
        print(f"NIF: {registro["NIF"]}")
        print(f"Nombre: {registro["Nombre"]}") 
        print(f"Edad: {registro["Edad"]}") 
        print("certificado impreso")
    elif op_imprimir == "2": 
         for registro in identificacion: 
               print("estado conyugal") 
               print(f"NIF: {registro["NIF"]}")
               print(f"Nombre: {registro["Nombre"]}") 
               print(f"Edad: {registro["Edad"]}")  
               print(f"Estado Conyugal {registro["Estado conyugal"]}") 
               print("certificado impreso")
    elif op_imprimir == "3": 
         for registro in identificacion: 
              print("Pertenecia a union europea") 
              print(f"NIF: {registro["NIF"]}")
              print(f"Nombre: {registro["Nombre"]}") 
              print(f"Edad: {registro["Edad"]}") 
              print(f"Nacionalidad {registro["Nacionalidad"]}")  
              print("certificado impreso")
    else: 
         print("opcion no valida")          



def salir(): 
    print("Hasta luego") 
    print("""power by adolfo
          Ver.2873648237y4""")
    exit() 

def val_valor(): 
     certif_lista =[]
     certif_lista.append((random.randint(1500,5000))) 
     


def menu (): 
    while True: 
        print("""          ********Menu******** 
              1.grabar datos 
              2.Buscar Dtos  
              3.Imprimir cerificados 
              4. Salir  
              """) 
        op = input("ingrese opcion\n") 
        if op == "1": 
            grabar() 
        elif op == "2": 
            buscar() 
        elif op == "3": 
            imprimir_certificados() 
        elif op == "4": 
            salir() 
        else: 
            print("opcion no valida")  


menu()