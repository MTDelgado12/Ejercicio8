'''Diseño de un sistema de gestión de proyectos:
Crear un sistema de gestión de proyectos que permita crear proyectos, asignar tareas a los miembros del equipo, 
realizar seguimiento del progreso y generar informes. Utiliza clases como "Proyecto", "Tarea" y 
"Equipo" para modelar el sistema y utiliza métodos para gestionar las operaciones.
'''
'''class Controlador:
    def __init__(self):
        self.Interfaz()
    
    def Interfaz(self):
        print("Este es el sistema de gestion de proyectos:")'''

class Equipo:
    nomequipo=0
    team=[]
    rol=[]
    def __init__(self,Miembosequipo,Nombequipo):
        self.Miembrosequipo=Miembosequipo
        self.Nombequipo=Nombequipo
        self.integrantes()
        self.AsignacionRol()
        self.MiembrosEquipo()

    def integrantes(self):
        Equipo.nomequipo=self.Nombequipo=input("Ingrese el nombre del equipo: ")
        self.numequipo=int(input("Ingrese el numero total de integrantes: "))
        for i in range (self.numequipo):
            Equipo.team.append(input(f"Ingrese el nombre del integrante {i+1} del equipo: "))
        print("------------------------------------------------")

    def AsignacionRol(self):
        for i in range (len(Equipo.team)):
            Equipo.rol.append(input(f"Ingrese el rol de {Equipo.team[i]}: "))
        print("------------------------------------------------")

    def MiembrosEquipo(self):
        print(f"El Equipo {self.Nombequipo} cuenta con {self.numequipo} miembros, sus integrantes son: ")
        for i in range (len(Equipo.team)):
            print(f"{i+1} - {Equipo.team[i]} - {Equipo.rol[i]}")
        print("------------------------------------------------")

class Proyecto(Equipo):
    tareas=[]
    def __init__(self,Nombreproy,Fechaasignadaproy,Fechamaxproy,tipoproy):
        self.Nombreproy=Nombreproy
        self.Fechaasignadaproy=Fechaasignadaproy
        self.Fechamaxproy=Fechamaxproy
        self.tipoproy=tipoproy
        self.crearproyecto()
        self.AsignarTarea()

    def crearproyecto(self):
        self.Nombreproy=input("Ingrese el nombre del proyecto: ")
        self.Fechaasignadaproy=int(input("Ingrese la fecha en la que se asigno el proyecto: "))        
        self.Fechamaxproy=int(input("Ingrese la fecha maxima para la entrega del proyecto: "))
        if self.Fechamaxproy-self.Fechaasignadaproy >= 20:
            self.tipoproy="Plazo largo"
        elif 10 <= self.Fechamaxproy-self.Fechaasignadaproy < 20:
            self.tipoproy="Plazo medio"
        elif 0 < self.Fechamaxproy-self.Fechaasignadaproy < 10:
            self.tipoproy="Plazo corto"
        print("------------------------------------------------")

    def AsignarTarea(self):
        self.numtareas=int(input(f"Ingrese el total de tareas del proyecto {self.Nombreproy}: "))
        for i in range (self.numtareas):
            Proyecto.tareas.append(input(f"Ingrese la tarea {i+1}: "))
        print("------------------------------------------------")

    def GenerarInforme(self):
        print(f"Proyecto: {self.Nombreproy} \n\
Tipo: {self.tipoproy} \n\
Equipo encargado: {Equipo.nomequipo} \n\
Tareas: {self.numtareas}")
        for i in range (self.numtareas):
            print(f"{i+1} = {Tarea.tsignadas[i]}")
    
class Tarea:
    tsignadas=[]
    def __init__(self):
        self.MostrarTareas()
        self.AsignarTarea()

    def MostrarTareas(self):
        print("Tareas: ")
        for i in range (len(Proyecto.tareas)):
            print(f"{i+1} - {Proyecto.tareas[i]}")
        print("------------------------------------------------")

    def AsignarTarea(self):
        for i in range (len(Proyecto.tareas)):
            print(f"{i+1} - {Proyecto.tareas[i]} se le asignara a: ")
            Tarea.tsignadas.append(input())

Team=Equipo(None,None)
proyecto=Proyecto(None,None,None,None)
tareas=Tarea()
proyecto.GenerarInforme()