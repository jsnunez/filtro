import json
with open('generos.json') as file:
    data = json.load(file)
from commons.funciones import validar_opcion,ad_gen,ad_Ac,ad_form,ges_info,ges_pel
while True:  

    print("1. Administracdor de Genero")
    print("2. Administrador de Actores")
    print("3. Administrador de Formatos")
    print("4. gestor de informes")
    print("5. gestor de peliculas")
    print("6. salir")    
    x=validar_opcion("Opcion: ",1,6)
    while x==1:
            x=ad_gen()
    while x==2:
            x=ad_Ac()        
    while x==3:
            x=ad_form()
    while x==4:
            x=ges_info()
    while x==5:
            x=ges_pel()
    if x==6:
        print("saliendo")
        break   
           