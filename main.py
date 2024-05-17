from clases.clasePaciente import Paciente
from clases.claseMedico import Medico
from clases.claseCitas import Cita
from clases.sistemaCitas import SistemaCitas, Paciente, Medico

paciente1 = Paciente('Juan', 'Perez', 'DNI', '12345678', '1990-01-01')
paciente2 = Paciente('Maria', 'Gomez', 'DNI', '87654321', '1985-05-15')
medico1 = Medico('Ana', 'Garcia', 'RM123')

sistema = SistemaCitas()
sistema.agregar_paciente(paciente1)
sistema.agregar_paciente(paciente2)
sistema.agregar_medico(medico1)

sistema.programar_cita('2024-05-01', '2024-05-20', '10:00', 'Consultorio 1', medico1, paciente1)
sistema.programar_cita('2024-05-02', '2024-05-20', '11:00', 'Consultorio 1', medico1, paciente2)

# Cancelar una cita
cita_a_cancelar = sistema.citas[0]  # Asumimos que es la primera cita programada
sistema.cancelar_cita(cita_a_cancelar)

# Buscar citas disponibles
citas_disponibles = sistema.buscar_citas_disponibles('2024-05-20')
for cita in citas_disponibles:
    print(cita)

print("hola mundo")
    