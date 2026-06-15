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
