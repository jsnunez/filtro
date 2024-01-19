import json
from os import system

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            print(enunciando,inferior,superior)
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def ad_gen():
        with open('generos.json') as file:
            data = json.load(file)


        print("1. crear Genero")
        print("2. listar genero")
        print("3. ir menu principal")
        a=validar_opcion("Opcion: ",1,3)
        if a==1:
            nombre= input("ingrese nombre del genero: ")
            n=str(len(data)+1)

            letra="G0"+n
            data[letra]={
             "id":letra ,
             "nombre":nombre

    }
        if a==2:
            n=int(len(data))
            for i in range (1,n+1):   
                print(data["G0"+str(i)])

        with open('generos.json', 'w') as file:
                json.dump(data, file)


def ad_Ac():       
    with open('actores.json') as file:
        data = json.load(file)     
    print("1. crear Actor")
    print("2. listar Actor")
    print("3. ir menu principal")
    a=validar_opcion("Opcion: ",1,3)
    if a==1:
            nombre= input("ingrese nombre del actor: ")
            n=str(len(data)+1)

            letra="A0"+n
            data[letra]={
             "id":letra ,
             "nombre":nombre

    }
    if a==2:
            n=int(len(data))
            for i in range (1,n+1):   
                print(data["A0"+str(i)])


    with open('actores.json', 'w') as file:
                json.dump(data, file)


def ad_form():
    with open('formatos.json') as file:
        data = json.load(file)  
    print("1. crear Formato")
    print("2. listar Formato")
    print("3. ir menu principal")
    a=validar_opcion("Opcion: ",1,3)
    if a==1:
            nombre= input("ingrese nombre del formato: ")
            n=str(len(data)+1)

            letra="F0"+n
            data[letra]={
             "id":letra ,
             "nombre":nombre
    }
    if a==2:
            n=int(len(data))
            for i in range (1,n+1):   
                print(data["F0"+str(i)])            

    with open('formatos.json', 'w') as file:
                json.dump(data, file)

def ges_pel():
    with open('data.json') as file:
        data = json.load(file)     
    print("1. agregar pelicula")
    print("2. editar pelicula")
    print("3. eliminar pelicula")
    print("4. eliminar actor")
    print("5. buscar pelicula")
    print("6. listar todas peliculas")   
    print("7. ir menu principal")
    a=validar_opcion("Opcion: ",1,7)
    if a==1: 
        n=str(len(data["blockbuster"]["peliculas"])+1)
        print(data)   
        nombre= input("ingrese nombre de la pelicula: ")
        duracion=input("ingrese duracion de la pelicula: ")
        sinopsis=input("ingrese sinopsis de la pelicula: ")
        with open('generos.json') as file:
            data1 = json.load(file)        
        print(data1)
        gensel=input("seleccione el genero con el id G")
        G={"G"+str(gensel):data1["G"+str(gensel)]}
        with open('actores.json') as file:
            data2 = json.load(file)  
        print(data2)
        actsel=input("seleccione el actor con el id A") 
        rol=input("seleccione el rol del actor")         
        A={"A"+str(actsel):data2["A"+str(actsel)],"rol":rol}
        
        with open('formatos.json') as file:
            data3 = json.load(file)  
        print(data3)
        formsel=input("seleccione el formato con el id F") 
        ncopy= input("numero de copias") 
        valor=input("valor prestamo")
        F={"F"+str(formsel):data3["F"+str(formsel)],"NroCopias":ncopy,"valorPrestamo":valor}
         

        data["blockbuster"]["peliculas"]["P0"+n]={
             "id":"P0"+n,
             "nombre":nombre  ,
             "duracion":duracion,
             "sinopsis":sinopsis,
             "genero":G,
             "actores":A,
             "formato":F,

             }  

    with open('data.json', 'w') as file:
                json.dump(data, file)

    if a==2: 
        selp=input("seleccionar id pelicula a mopdificar")
        print(data)   
        nombre= input("ingrese nombre de la pelicula: ")
        duracion=input("ingrese duracion de la pelicula: ")
        sinopsis=input("ingrese sinopsis de la pelicula: ")
        with open('generos.json') as file:
            data1 = json.load(file)        
        print(data1)
        gensel=input("seleccione el genero con el id G")
        G={"G"+str(gensel):data1["G"+str(gensel)]}
        with open('actores.json') as file:
            data2 = json.load(file)  
        print(data2)
        actsel=input("seleccione el actor con el id A") 
        rol=input("seleccione el rol del actor")         
        A={"A"+str(actsel):data2["A"+str(actsel)],"rol":rol}
        
        with open('formatos.json') as file:
            data3 = json.load(file)  
        print(data3)
        formsel=input("seleccione el formato con el id F") 
        ncopy= input("numero de copias") 
        valor=input("valor prestamo")
        F={"F"+str(formsel):data3["F"+str(formsel)],"NroCopias":ncopy,"valorPrestamo":valor}
        data["blockbuster"]["peliculas"]["P0"+selp]={
             "id":"P0"+selp,
             "nombre":nombre  ,
             "duracion":duracion,
             "sinopsis":sinopsis,
             "genero":G,
             "actores":A,
             "formato":F,

             }  

    with open('data.json', 'w') as file:
                json.dump(data, file)         

    if a==3: 
        selp=input("seleccionar id pelicula a eliminar")
        print(data)     
        data["blockbuster"]["peliculas"]["P0"+selp]={
             "id":"P0"+selp,
             "nombre":""  ,
             "duracion":0,
             "sinopsis":"",
             "genero":"",
             "actores":"",
             "formato":"",

             }  

    with open('data.json', 'w') as file:
                json.dump(data, file)   

    if a==5:   
        n=int(len(data["blockbuster"]["peliculas"]))
        for i in range (1,n) :
            if data["blockbuster"]["peliculas"]["P0"+str(i)]["nombre"] ==     "Ocho apellidos marroquís":
               print(data["blockbuster"]["peliculas"]["P0"+str(i)])

    if a==6:  
        n=int(len(data["blockbuster"]["peliculas"]))
        for i in range (1,n) :
          print(data["blockbuster"]["peliculas"]["P0"+str(i)]["nombre"])

def ges_info():
    with open('data.json') as file:
        data = json.load(file)  
    print("1. listar las pelicula de un genero especifico")
    print("2. listar las pelicula donde el protagonista sea silvester stallone")
    print("3. buscar pelicula y mostrar la sinopsis y los actores")
    print("4. ir menu principal")
    a=validar_opcion("Opcion: ",1,4)
    if a==1:
        with open('generos.json') as file:
            data1 = json.load(file)        
        print(data1)        
        n=int(len(data["blockbuster"]["peliculas"]))
        genero=input("ingrese id genero a ver G0")
        for i in range (1,n) :        
         if data["blockbuster"]["peliculas"]["P0"+str(i)]["generos"]["G0"+str(i)] ["id"]==  genero:
               print(data["blockbuster"]["peliculas"]["P0"+str(i)])
