"""1) Hacer un programa que gestione datos para una escuela. El programa tiene que ser capaz
de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido,
fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de
faltas, cantidad de amonestaciones recibidas.)
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos
f) Dar Persistencia a los Datos del programa mediante la implementación Archivos
El trabajo practico se deberá subir a un repositorio de GitHub Publico, y se entregara
únicamente la dirección del repositorio (No de la pagina)."""

#hay que dividir en tareas
#ya tengo mi base de datos, vamos a ver como agregar, sacar (""""fácil""""") y después modificar (difícil)
#Primero vamos a agregar 
# Como organizo mis datos? 
# (DNI, Nombre, Apellido,
# fecha de nacimiento, Nombre de Tutor, 
# registro de todas las notas, cantidad de
# faltas, cantidad de amonestaciones recibidas.)

# a) Llevar un registro de todos los datos de alumnos de la escuela (DNI, Nombre, Apellido,
# fecha de nacimiento, Nombre de Tutor, registro de todas las notas, cantidad de
# faltas, cantidad de amonestaciones recibidas.)

import datetime


def ordenar(alumnos,apellidos):
    apellidos.sort()
    alumnos_ordenados = []
    ya_en_lista = []
    for i in range(len(apellidos)):
        for j in range(len(alumnos)):
            if alumnos[j][2]==apellidos[i] and (alumnos[j][0] not in ya_en_lista):
                alumnos_ordenados.append(alumnos[j])
                ya_en_lista.append(alumnos[j][0])
                break
        
    return alumnos_ordenados,apellidos
            
def actualizar(alumnos):
    base_de_datos = open(r"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","w")
    apellidos = []
    for alumno in alumnos:
        for dato in alumno:
            base_de_datos.write(f"{dato};")
        base_de_datos.write("\n")
        apellidos.append(alumno[2])
    
    base_de_datos.close()
    return apellidos,alumnos

#b) Mostrar los datos de cada alumno
def listado_alumnos(alumnos):
    for alumno in alumnos:
        fecha = datetime.datetime.strptime(alumno[3],"%Y-%m-%d %H:%S:%f")
        print (f"--{alumno[2]}, {alumno[1]} DNI:{alumno[0]} Nacimiento:{fecha.day}/{fecha.month}/{fecha.year}")
        print (f"   Tutor: {alumno[4]} Notas:{alumno[5]}")
        print (f"   Faltas: {alumno[6]} Amonestaciones: {alumno[7]}")
    return

#c) Modificar los datos de los alumnos
def modificar(alumnos,apellidos):
    print("Qué alumno desea modificar?")
    listado_alumnos(alumnos)
    a_modificar = input("DNI: ")
    alumnos,apellidos = expulsar(alumnos,apellidos,a_modificar,True)
    agregar()
    return



# d) Agregar alumnos
def agregar():
     # Agregar alumnos a mi base de datos
    DNI = input("Ingrese el DNI del alumno:\n")
    Apellido = input("Ingrese apellido del alumno:\n")
    Nombre = input("Ingrese el nombre del alumno: (incluyendo segundo nombre si corresponde)\n")
    print("Ingrese fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))
    fecha_de_nacimiento = datetime.datetime(anio,mes,dia)
    nombre_tutor = input("Tutor Asignado:")
    notas = []
    cant_notas = input("Cuántas notas tiene el alumno?\n")
    for i in range(int(cant_notas)):
        nota = int(input(f"Ingrese nota {i+1}: "))
        notas.append(nota)
    faltas = int(input("Cuántas faltas tiene el alumno?\n"))
    amonestaciones = int(input("Cuántas amonestaciones tiene?\n"))
    Alumno = [DNI,Nombre,Apellido,fecha_de_nacimiento,nombre_tutor,notas,faltas,amonestaciones]
    with open(r"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","a") as base_de_datos:
        for dato in Alumno:
            base_de_datos.write(f"{dato};")
        base_de_datos.write("\n")
    Alumno[3] = str(Alumno[3])
    global alumnos,apellidos
    alumnos.append(Alumno)
    apellidos.append(Alumno[2])
    return 


#e) Expulsar alumnos
def expulsar(alumnos,apellidos,expulsado=0,falsa_expulsion=False):
    aux = len(alumnos)
    if not falsa_expulsion:
        print("Qué alumno desea expulsar?")
        listado_alumnos(alumnos)
        expulsado = input("Ingrese DNI:\n")
    for alumno in alumnos:
        if alumno[0] == expulsado and not falsa_expulsion:
            print(f"{alumno[1]} {alumno[2]} fue expulsado de la institución.")
            alumnos.remove(alumno)
            apellidos.remove(alumno[2])
            apellidos = actualizar(alumnos)
        elif alumno[0] == expulsado and falsa_expulsion:
            alumnos.remove(alumno)
            print("Ingrese los datos modificados del alumno")
            apellidos.remove(alumno[2])
            apellidos = actualizar(alumnos)
    if aux == len(alumnos):
        print("No se encontró al alumno")
    return alumnos,apellidos

    




#                               Ejecución
ahora = datetime.datetime.now()
backup = open(fr"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\backups\{datetime.datetime.date(ahora)}-{ahora.hour}:{ahora.minute}","w")
with open(rf"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","r") as base_de_datos:
    alumnos = base_de_datos.readlines()
    apellidos = []
    for i in range (len(alumnos)):
        backup.write(alumnos[i])
        alumnos[i] = alumnos[i].split(";")
        alumnos[i].pop()
        apellidos.append(alumnos[i][2])
    alumnos,apellidos = ordenar(alumnos,apellidos)
    
backup.close()



while True:
    print("                         Seleccione una opción:")
    print("     1) Listado de Alumnos")
    print("     2) Agregar Alumno")
    print("     3) Expulsar Alumno")
    print("     4) Modificar Alumno")
    print("Ingrese ''*'' para salir")
    opcion = input()
    if opcion=="*":
        break
    elif opcion=="1":
        listado_alumnos(alumnos)
    elif opcion=="2":
        agregar()
        alumnos,apellidos = ordenar(alumnos,apellidos)
    elif opcion=="3":
        alumnos,apellidos = expulsar(alumnos,apellidos)
        actualizar(alumnos)
    elif opcion=="4":
        modificar(alumnos,apellidos)
    elif 1<int(opcion) or int(opcion)>4:
        print("Elija una opción válida")
    

ahora = datetime.datetime.now()
with open(fr"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\backups\{datetime.datetime.date(ahora)}-{ahora.hour}:{ahora.minute}","w") as backup:
    for alumno in alumnos:
        for dato in alumno:
            backup.write(f"{dato};")
        backup.write("\n")
