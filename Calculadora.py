# Datos del paciente
nombre = input("Nombre Paciente: ")
paterno = input("Apellido Paterno: ")
materno = input("Apellido Materno: ")

# Validar que los campos de texto
if nombre == "" or paterno == "" or materno == "":
    print("Asegúrate de no dejar campos en blancos.")
else:
    # Datos numericos, validar inserte solo valores númericos
    edad = int(input("Edad: "))
    peso = float(input("Peso(KG): "))
    estatura = float(input("Estatura(Metro): "))
        
    # Validar que la edad, el peso y la estatura sean cifras válidas
    if edad <= 0 or peso <= 0 or estatura <= 0:
        print("Validar incluir solo valores númericos")
    else:
        # Calcular el IMCf
        imc = peso / (estatura ** 2)
        # Visualizar resultado IMC
        print(f"Índice de Masa Corporal (IMC): {imc:.2f}")



