import subprocess
subprocess.run('clear', shell=True)

# LIMPIA LA PANTALLA
def limpiar_pantalla():
    import subprocess
    subprocess.run('clear', shell=True)

# VALIDACION DE ENTRADA DE TEXTO
def pedir_texto(msg: str) -> str:
    while True:
        try:
            texto = input(msg).lower().strip()
        
            if texto == '':
                print('ERROR: No puede quedar vacio')
            else:
                return texto
        except ValueError:
            print('ERROR: Caracter no valido')

# VALIDACION DE ENTRADA NUMERICA
def pedir_numero(msg: str) -> int:
    while True:
        try:
            numero = int(input(msg))
            
            if numero < 0:
                print('ERROR: No puede ser negativo')
            else: 
                return numero
        except ValueError:
            print('ERROR: Caracter no valido')

#VALIDACION DEL HORARIO DE ATENCION
def hora_en_horario_atencion(hora: str) -> bool:
    partes = hora.split(':') # separa en dos partes y la division entre ambas son los dos puntos
    
    if len(partes) != 2: # si las partes son distintas de dos
        return False
    
    horas = partes[0] # toma el primer elemento de la variable partes
    minutos = partes[1] # toma el segundo elemento
    
    if not horas.isdigit() or not minutos.isdigit(): # esto sirve para validar si son numeros, tipo 'si horas no es un numero, return False'
        return False
    
    if len(horas) != 2 or len(minutos) != 2: # obliga a escribir dos caracteres en las horas y minutos -> 08:00, 06:35
        return False
    
    # Convertir a enteros 
    horas = int(horas)
    minutos = int(minutos)
    
    if horas < 0 or horas > 23: # evita introducir horas que nada que ver -> 25:00
        return False
    if minutos < 0 or minutos > 59: # al igual que la hora, evita que ponga cosas raras en los minutos -> 10:85
        return False
    
    hora_en_minutos = horas * 60 + minutos # se convierte todo en un solo numero, ayuda a que la vomparacion de horas sea mas facil
    
    # declarar las variables que van a reprresentar los valores de apertura y cierre
    apertura = 8 * 60
    cierre = 21 * 60
    
    return apertura <= hora_en_minutos <= cierre
    
    
    
    