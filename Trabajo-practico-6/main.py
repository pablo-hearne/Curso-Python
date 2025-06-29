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

import datetime
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido,
# fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de
# faltas, cantidad de amonestaciones recibidas.)

def listado_alumnos(alumnos):
    for alumno in alumnos:
        print (f"{alumno[2]}, {alumno[1]} DNI:{alumno[0]}")
    return

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
        
    return alumnos_ordenados
            
def actualizar(alumnos):
    base_de_datos = open(r"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","w")
    for alumno in alumnos:
        for dato in alumno:
            base_de_datos.write(f"{dato};")
        base_de_datos.write("\n")
    
    base_de_datos.close()
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
    with open(r"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","r") as base_de_datos:
        for dato in Alumno:
            base_de_datos.write(f"{dato};")
    return 


#e) Expulsar alumnos
def expulsar(alumnos):
    print("Qué alumno desea expulsar?")
    listado_alumnos(alumnos)
    aux = len(alumnos)
    expulsado = input("Ingrese DNI:\n")
    for alumno in alumnos:
        if alumno[0] == expulsado:
            print(f"{alumno[1]} {alumno[2]} fue expulsado de la institución.")
            alumnos.remove(alumno)
            actualizar(alumnos)
    if aux == len(alumno):
        print("No se encontró al alumno")
    return

    




#                               Ejecución

with open(r"D:\Cosas\Pablo\Curso Python\Trabajo-practico-6\base_de_datos.txt","r") as base_de_datos:
    alumnos = base_de_datos.readlines()
    apellidos = []
    for i in range (len(alumnos)):
        alumnos[i] = alumnos[i].split("\n")
        alumnos[i].pop()
        print(alumnos[i])
        apellidos.append(alumnos[i][2])
    alumnos = ordenar(alumnos,apellidos)
    




