from datetime import datetime

class Alumno:
    """Comentarios de uso de la clase"""
# Variables o propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento= None

# Funcion constructora que se ejecuta al crear (instanciar) el objeto
# self es una variabloe que representa al mismo objeto
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

# Otras funciones
    def getFullName(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def setFechaNacimiento(self, fecha) ->bool:
        try:
            if(len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            return True
        except:
            return False

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None):
            return -1
        else:
            return datetime.now().year-self.FechaNacimiento.year
        

class Estudiante(Alumno):
    Curso = None

    def __init__(self, nombre, apellido1, apellido2, curso) -> None:
        super().__init__(nombre, apellido1, apellido2)
        self.Curso = curso

# Crear un objeto (instanciamos un oobjeto) ejecuta la func constructora
alumno = Alumno("Angel", "Ruiz", "Centeno")
alumno2 = Alumno("Rosa", "Sanchez")

print(f"Me llamo : {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo : {alumno2.getFullName()}")

alumno.setFechaNacimiento("18-09-1993")
print(alumno.FechaNacimiento)
print(alumno.getEdad())   

print("")

estudiante1= Estudiante("Alex","Pereira", "Torres", "2doA")
estudiante1.setFechaNacimiento("12-02-2015")
print(f"<El estudiante se llama : {estudiante1.getFullName()}")
print(f"El primer apellido es: {estudiante1.Apellido1}")
print(estudiante1.FechaNacimiento)
print(estudiante1.getEdad())
print(estudiante1.Curso)
    
    