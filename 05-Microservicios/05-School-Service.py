"""
Contruye un objeto que permita insertar, actulizar, eliminar y consultar los datos de un Alumno.
    Consultar mediante GET -> api/people/<id> por ejemplo api/people/5 -> Retorna 200 OK
    Consultar listado  GET -> api/people/ -> Retorna 200 OK
    
    --Insertar mediante POST -> api/people + datos en JSON en el Body -> Retorna 201 Created + Id del nuevo alumno
    
    --Actualizar mediante PUT -> api/people/<id> por ejemplo api/people/5 + datos en JSON en el Body -> Retorna 204 NoContent
    
    --Eliminar mediante DELETE -> api/people/<id> por ejemplo api/people/5 -> Retorna 204 NoContent
    ATENCIÓN, eliminar solo los alumnos creados por vosotros


    {'personID': 5, 'lastName': 'Harui', 'firstName': 'Roger', 'hireDate': '1998-07-01T00:00:00', 'enrollmentDate': None, 'officeAssignment': None, 'studentGrades': [], 'courses': []}

"""
import requests
import json


class People:
    # Defino variables de clase People
    PersonID = None
    LastName = None
    FirstName = None
    HireDate = None
    EnrollmentDate = None

# Defino constuctor de Clase
    def __init__(self, PersonID, LastName, FirstName, HireDate, EnrollmentDate) -> None:
        self.PersonID = PersonID
        self.LastName = LastName
        self.FirstName = FirstName
        self.HireDate = HireDate
        self.EnrollmentDate = EnrollmentDate
# Insertar persona , Hay q validar q dicha persona ya exista

    def insert_people(self):
        mydata = {'personID': 40, 'lastName': 'RC', 'firstName': 'AA', 'hireDate': None,
                  'enrollmentDate': '2023-04-06T00:00:00', 'officeAssignment': None, 'studentGrades': [], 'courses': []}
        url = "http://eoi-api.eastus.cloudapp.azure.com/api/people"
        myheaders = {'Content-Type': 'application/json'}
        response = requests.post(url, data=mydata, headers=myheaders)
        # response = requests.request("POST", url,headers=myheaders, data=mydata)
        print(response.status_code, response.reason, sep="-")
        print(response.text)


# Actualizar persona, Preguntar que datos modificar


    def update_people(self):
        id = (input("Indique el Id de la persona: "))
        my_url = f"http://eoi-api.eastus.cloudapp.azure.com/api/people/{id}"
        mydata = {'personID': 40, 'lastName': 'RC', 'firstName': 'AAnew', 'hireDate': None,
                  'enrollmentDate': '2023-04-06T00:00:00', 'officeAssignment': None, 'studentGrades': [], 'courses': []}
        myheaders = {'Content-Type': 'application/json'}
        response = requests.put(url=my_url, json=mydata, headers=myheaders)
        print(response.status_code, response.reason, sep="-")
        print(response.text)


# Eliminar persona, solo eliminar personas cuyo id sea mayor que 34

    def delete_people(self):
        id = (input("Indique el Id de la persona: "))
        my_url = f"http://eoi-api.eastus.cloudapp.azure.com/api/people/{id}"
        myheaders = {'Content-Type': 'application/json'}
        response = requests.delete(url=my_url, headers=myheaders)
        print(response.status_code, response.reason, sep="-")
        print(response.text)

# Consultar datos de una persona
    def consult_people(self):
        try:
            id = (input("Indique el Id de la persona: "))
            my_url = f"http://eoi-api.eastus.cloudapp.azure.com/api/people/{id}"
            response = requests.get(my_url)
            if (response.status_code == 200):
                data = response.json()
                print(f"Id: {data['personID']}")
                print(f"Apellido: {data['lastName']}")
                print(f"Nombre: {data['firstName']}")
                print(f"Fecha de contratación: {data['hireDate']}")
                print(f"Fecha de inscripción: {data['enrollmentDate']}")
                print(f"Notas de Estudiante: {data['studentGrades']}")
                print(f"Cursos: {data['courses']}")
            else:
                print(f"Error:", response.reason)
        except KeyError:
            print("Clave no encontrada")

# Consultar Lista de nombres
    def consult_list(self):
        url = f"http://eoi-api.eastus.cloudapp.azure.com/api/people"
        response = requests.get(url)
        if (response.status_code == 200):
            data = list(response.json())
            print("Lista de Nombres:")
            for i in data:
                print(i['firstName'])
        else:
            print(f"Error:", response.reason)

        print("")


p1 = People("6481638", "Ruiz", "Angel Alejandro", "05/04/2023", "05/04/2024")
print(p1.PersonID)
print(p1.LastName)
print(p1.FirstName)
print(p1.HireDate)
print(p1.EnrollmentDate)

# Toma de datos
volver = 1
while (volver == 1):
    volver3 = 1
    while (volver3 == 1):
        try:
            # *******************************
            #            Menu
            # *******************************

            print("**********", "MENU", "**********", sep="\n")
            print("Option 1: Insertar Persona")
            print("Option 2: Modificar Persona")
            print("Option 3: Borrar Persona")
            print("Option 4: Consultar Persona")
            print("Option 5: Consultar Lista de Personas")
            print("Option 6: Salir")
            option = input("Que desea Hacer: ")
            match option:
                case "1": p1.insert_people()
                case "2": p1.update_people()
                case "3": p1.delete_people()
                case "4": p1.consult_people()
                case "5": p1.consult_list()
                case "6": volver3 = 0
                case _: print("Opcion no valida")
        except ValueError:
            print("Opcion no valida")
            volver3 = 1
        else:
            volver3 = 0

#   Check volver a intentar y validar entrada
    volver2 = 1
    while (volver2 == 1):
        try:
            volver = (
                input("Pulse 0 para Salir, Cualquier otro numero volver a intentar : "))
            if (int(volver) != 0):
                volver = 1
        except ValueError:
            print("No se introdujo un numero")
            volver2 = 1
        else:
            volver2 = 0

"""
Sugerencias

El código parece estar bien estructurado y organizado. Sin embargo, encontré algunas sugerencias que podrían mejorar la funcionalidad y legibilidad del código:

En el método insert_people(), estás definiendo un diccionario mydata con los datos de la persona a insertar. En lugar de definir un diccionario en el método, puedes hacer que los datos se pasen como parámetros al método para que sea más fácil de reutilizar y mantener.

En el método update_people(), estás definiendo un diccionario mydata con los datos de la persona a actualizar. De nuevo, sería mejor pasar los datos como parámetros para que el método sea más fácil de reutilizar y mantener.

En el método delete_people(), estás pidiendo al usuario que ingrese el ID de la persona a eliminar. Sin embargo, la condición para eliminar la persona es que su ID sea mayor que 34. Sería mejor establecer esta condición en el método delete_people() para evitar que el usuario intente eliminar personas con IDs inferiores a 35.

En el método consult_people(), estás utilizando un bloque try-except para manejar la excepción KeyError. En lugar de manejar la excepción, sería mejor verificar si la clave existe en el diccionario utilizando el método dict.get(), que devuelve None si la clave no existe.

Aquí te dejo una versión modificada del código con estas sugerencias implementadas:

"""


"""
import requests
import json


class People:
    # Defino variables de clase People
    PersonID = None
    LastName = None
    FirstName = None
    HireDate = None
    EnrollmentDate = None

    # Defino constuctor de Clase
    def __init__(self, PersonID, LastName, FirstName, HireDate, EnrollmentDate) -> None:
        self.PersonID = PersonID
        self.LastName = LastName
        self.FirstName = FirstName
        self.HireDate = HireDate
        self.EnrollmentDate = EnrollmentDate

    # Insertar persona, Hay que validar que dicha persona ya exista
    def insert_people(self, personID, lastName, firstName, hireDate, enrollmentDate):
        data = {
            'personID': personID,
            'lastName': lastName,
            'firstName': firstName,
            'hireDate': hireDate,
            'enrollmentDate': enrollmentDate,
            'officeAssignment': None,
            'studentGrades': [],
            'courses': []
        }
        url = "http://eoi-api.eastus.cloudapp.azure.com/api/people"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        print(response.status_code, response.reason, sep="-")
        print(response.text)

    # Actualizar persona, Preguntar que datos modificar
    def update_people(self, personID, lastName, firstName, hireDate, enrollmentDate):
        id = input("Indique el Id de la persona: ")
        url = f"http://eoi-api.eastus.cloudapp.azure.com/api/people/{id}"
        data = {
            'personID': personID,
            'lastName': lastName,
            'firstName': firstName,
            'hireDate': hireDate,
            'enrollmentDate': enrollmentDate,
            'officeAssignment': None,
            'studentGrades': [],
            'courses': []
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, json=data, headers=headers)
        print(response.status_code

"""
