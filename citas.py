# IMPORTAR LAS FUNCIONES DE OTRO MODULO
from validaciones import pedir_texto

# DECLARAR LAS CONSTANES A NIVEL GLOBAL
SERVICIOS = ('corte','barba', 'tinte', 'cejas', 'manicure')
BARBEROS = (('carlos', 'andrea', 'miguel'))
DIAS = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

# GENERAR ID PARA CADA CLIENTE
def generar_id(citas) -> int:
    if not citas:
        return 1
    
    mayor_id = 0
    for cita in citas:
        if cita['id'] > mayor_id:
            mayor_id = cita['id']
    return mayor_id + 1

# SERVICIOS DISPONIBLES: El usuario ingresa un servicio valido y lo devuelve
def pedir_servicio() -> str:
    print('--- SERVICIOS DISPONIBLES ---')
    print(', '.join(SERVICIOS))
    print()
    while True:
        servicio = pedir_texto('Servicio: ')
        if servicio in SERVICIOS:
            return servicio
        print('ERROR: Ingrese un servicio disponible')
        print()

# BARBEROS DISPONIBLES: Pide el barbero y lo devuelve si es valido
def pedir_barberos() -> str:
    print('--- BARBEROS DISPONIBLES ---')
    print(', '.join(BARBEROS))
    while True:
        barbero = pedir_texto('Barbero: ')
        if barbero in BARBEROS:
            return barbero
        print('ERROR: Ingrese un barbero disponible')

# PEDIR DIA DE LA SEMANA
def pedir_dia() -> str:
    while True:
        dia = pedir_texto('Dia: ')
        if dia in DIAS:
            return dia
        print('ERROR: Intente nuevamente')

# HORARIO OCUPADO: Devuelve un bool basicamente para responder si/no -> si = True, no = False
# Se usan bool en este caso para validar algo
def horario_ocupado(citas: list, servicio: str, barbero: str, dia: str) -> bool: 
    for cita in citas:
        if cita['barbero'] == barbero and cita['servicio'] == servicio and cita['dia'] == dia:
            if cita['estado'] == 'pendiente':
                return True
    return False

# AGREGAR CITAS NUEVAS: Primero se pide la entrada de texto y luego se guarda en el JSON usando los datos ingresados
def agregar_cita(citas: list) -> None: # None porque no retorna nada, solamente guarda e imprime
    cliente = pedir_texto('Cliente: ')
    telefono = pedir_texto('Telefono: ')
    servicio = pedir_servicio()
    barbero = pedir_barberos()
    dia = pedir_dia()
    hora = pedir_texto('Hora (HH:MM): ')
    
    if horario_ocupado(citas, barbero, dia, hora):
        print('ERROR: Ya hay una cita con este barbero el mismo dia y hora')
        return False
    
    # Se crea el diccionario usando los campos de entrada del usuario
    nueva_cita = {
        'id': generar_id(citas),
        'cliente': cliente,
        'telefono': telefono,
        'servicio': servicio,
        'barbero': barbero,
        'dia': dia,
        'hora': hora,
        'estado': 'pendiente'
    }
    
    # Se a;aden los campos al JSON
    citas.append(nueva_cita)
    print('CITA AGREGADA EXITOSAMENTE')
    return True

# MOSTRAR LAS CITAS EXISTENTES
def mostrar_citas(citas) -> None:
    if not citas:
        print('NO HAY CITAS AGENDADAS TODAVIA')
        return
    
    print(f'--- CITAS AGENDADAS: {len(citas)} ---')
    for cita in citas:
        print(f'ID: {cita['id']}')
        print(f'Cliente: {cita['cliente']}')
        print(f'Telefono: {cita['telefono']}')
        print(f'Servicio: {cita['servicio']}')
        print(f'Barbero: {cita['barbero']}')
        print(f'Dia: {cita['dia']}')
        print(f'Hora: {cita['hora']}')
        print(f'Estado: {cita['estado']}')
        print('-' * 30)

# BUSCAR TODAS LAS CITAS QUE TENGA UN CLIENTE
def buscar_citas_cliente(citas: list, cliente) -> list:
    encontradas = []
    for cita in citas:
        if cita['cliente'] == cliente:
            encontradas.append(cita)
    return encontradas

# MOSTRAR SOLAMENTE LAS CITAS DEL BARBERO SELECCIONADO
def filtrar_citas_barbero(citas: list, barbero: str) -> list:
    encontradas = []
    
    for cita in citas:
        if cita['barbero'] == barbero:
            encontradas.append(cita)
    return encontradas

# MOSTRAR SOLAMENTE LAS CITAS DE ESE DIA
def filtrar_citas_dia(citas: list, dia: str) -> list: 
    encontradas = []
    
    for cita in citas:
        if cita['dia'] == dia:
            encontradas.append(cita)

# DEVUELVE UNA SI LA ENCUENTRA, NONE SI NO
def buscar_cita_exacta(citas, cliente, dia, hora) -> dict | None:
    
    for cita in citas:
        if cita['cliente'] == cliente and cita['dia'] == dia and cita['hora'] == hora:
            return cita
    return None

# MARCAR COMO CANCELADA UNA CITA
def cancelar_cita(citas: list, cliente, dia, hora) -> bool:
    cliente = pedir_texto('Cliente: ')
    dia = pedir_dia()
    hora = pedir_texto('Hora: ')
    
    cita = buscar_cita_exacta(cita, cliente, dia, hora)
    
    if cita is None:
        print('ERROR: No existe registro del cliente solicitado')
        return False
    
    if cita['estado'] == 'cancelada':
        print('Esta cita ya esta cancelada')
        return False
    
    if cita['estado'] == 'atendida':
        print('ERROR: No puede marcar como cancelada una cita atendida')
        return False
    
    cita['estado'] = 'cancelada'
    print('CITA CANCELADA EXITOSAMENTE')
    return True

# MARCAR COMO ATENDIDA UNA CITA
def marcar_atendida(citas: list) -> bool:
    cliente = pedir_texto('Cliente: ')
    dia = pedir_dia()
    hora = pedir_texto('Hora: ')
    
    cita = buscar_cita_exacta(citas, cliente, dia, hora)
    
    if cita is None:
        print('ERROR: No existe cita con esas credenciales')
        return False
    
    if cita['estado'] == 'atendida':
        print('ERROR: Esta cita ya se encuentra atendida')
    
    if cita['estado'] == 'cancelada':
        print('ERROR: No puede marcar como atendida una cita cancelada')
        return False
    
    cita['estado'] = 'atendida'
    print('CITA ATENDIDA EXITOSAMENTE')
    return True

# MOSTRAR TODAS LAS CITAS PENDIENTES
def mostrar_citas_pendientes(citas: list) -> None:
    pendientes = []
    
    for cita in citas:
        if cita['estado'] == 'pendiente':
            pendientes.append(cita)
    
    if not pendientes:
        print('No hay citas pendientes')
        return
    
    mostrar_citas(pendientes)