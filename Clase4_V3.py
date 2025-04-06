class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
    def __str__(self):
        return f"""
    -------------------------------------------------------------------------------------------------------
    Paciente: {self.__nombre}, Cedula: {self.__cedula}, Genero: {self.__genero}, Servicio: {self.__servicio} 
    -------------------------------------------------------------------------------------------------------"""
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
        # Lista de pacientes predeterminados (cada paciente es un diccionario)
        pacientes_iniciales = [
            {"nombre": "Ana Pérez", "cedula": 1001234567, "genero": "Femenino", "servicio": "Cardiología"},
            {"nombre": "Carlos Gómez", "cedula": 2002345678, "genero": "Masculino", "servicio": "Pediatría"},
            {"nombre": "María Rodríguez", "cedula": 3003456789, "genero": "Femenino", "servicio": "Oncología"}
        ]
        
        # Convertimos cada diccionario en un objeto Paciente
        for paciente_data in pacientes_iniciales:
            pac = Paciente()
            pac.asignarNombre(paciente_data["nombre"])
            pac.asignarCedula(paciente_data["cedula"])
            pac.asignarGenero(paciente_data["genero"])
            pac.asignarServicio(paciente_data["servicio"])
            self.__lista_pacientes.append(pac)
        
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        if self.verificarPaciente(c) == False:
            return None
        for p in self.__lista_pacientes:
            #retorne la cedula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p #si encuentro el paciente lo retorno
            
    def buscarPacientesPorNombre(self, nom_buscar):
        contador = 0
        for p in self.__lista_pacientes:
            if p.verNombre().lower().startswith(nom_buscar.lower()):
                contador += 1                
                print(p)        
        if contador == 0:
            print(f"No se encontró ningún paciente con el nombre *{nom_buscar}*")
    
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente \n3 Buscar paciente por nombre \n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
                
        elif opcion == 3:
            nom = input("Ingrese el nombre del paciente a buscar: \n>>>")
            sis.buscarPacientesPorNombre(nom)
        

        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
