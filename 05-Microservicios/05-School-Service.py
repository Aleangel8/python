"""
Contruye un objeto que permita insertar, actulizar, eliminar y consultar los datos de un Alumno.
    Consultar mediante GET -> api/people/<id> por ejemplo api/people/5 -> Retorna 200 OK
    Consultar listado  GET -> api/people/ -> Retorna 200 OK
    
    Insertar mediante POST -> api/people + datos en JSON en el Body -> Retorna 201 Created + Id del nuevo alumno
    
    Actualizar mediante PUT -> api/people/<id> por ejemplo api/people/5 + datos en JSON en el Body -> Retorna 204 NoContent
    
    Eliminar mediante DELETE -> api/people/<id> por ejemplo api/people/5 -> Retorna 204 NoContent
    ATENCIÓN, eliminar solo los alumnos creados por vosotros


    {'personID': 5, 'lastName': 'Harui', 'firstName': 'Roger', 'hireDate': '1998-07-01T00:00:00', 'enrollmentDate': None, 'officeAssignment': None, 'studentGrades': [], 'courses': []}

"""
import requests

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
    def insert_people():
          pass
# Actualizar persona, Preguntar que datos modificar
    def update_people():
          pass
# Eliminar persona, solo eliminar personas cuyo id sea mayor que 34
    def delete_people():
          pass
# Consultar datos de una persona 
    def consult_people():
          pass


url= "http://eoi-api.eastus.cloudapp.azure.com/api/people/34"


p1 = People("6481638","Ruiz","Angel Alejandro","05/04/2023","05/04/2024")
print(p1.PersonID)
print(p1.LastName)
print(p1.FirstName)
print(p1.HireDate)
print(p1.EnrollmentDate)


# myheaders={"to": "USD","from": "EUR", "amount":num, "apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}
#   response = requests.get(url, headers=myheaders)

response = requests.get(url)

if (response.status_code == 200):
        data = response.json()
        print(data)

else:
        print(f"Error: ", response.reason)


