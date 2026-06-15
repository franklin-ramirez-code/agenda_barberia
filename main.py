from validaciones import pedir_texto, limpiar_pantalla
from archivo import cargar_citas, guardar_cita
from citas import (
    agregar_cita,
    mostrar_citas,
    pedir_barberos,
    pedir_dia,
    filtrar_citas_barbero,
    filtrar_citas_dia,
    buscar_cita_exacta,
    buscar_citas_cliente,
    cancelar_cita,
    marcar_atendida,
    mostrar_citas_pendientes,
    BARBEROS,
    DIAS
)


OPCIONES_VALIDAS = ('1', '2', '3' , '4', '5', '6', '7', '8', '9')

def mostrar_menu():
    print('===== GESTION DE BARBERIA =====')
    print()
    print('1. Registrar cita')
    print('2. Mostrar todas las citas')
    print('3. Buscar cita por cliente')
    print('4. Filtrar citas por barbero')
    print('5. Filtrar citas por dia')
    print('6. Cancelar cita')
    print('7. Marcar cita como atendida')
    print('8. Mostrar citas pendientes')
    print('9. Salir')
    print()
    

def main() -> None:
    citas = cargar_citas()
    
    while True:
        mostrar_menu()
        opcion = pedir_texto('Seleccione: ')
        
        if opcion not in OPCIONES_VALIDAS:
            print('ERROR: Opcion no valida')
            continue
        
        if opcion == '1':
            limpiar_pantalla()
            cambio = agregar_cita(citas)
            if cambio:
                guardar_cita(citas)

        elif opcion == '2':
            limpiar_pantalla()
            mostrar_citas(citas)

        elif opcion == '3':
            limpiar_pantalla()
            cliente = pedir_texto('Cliente: ')
            resultado = buscar_citas_cliente(citas, cliente)
            mostrar_citas(resultado)

        elif opcion == '4':
            limpiar_pantalla()
            barbero = pedir_texto('Barbero: ')
            
            if barbero not in BARBEROS:
                print('ERROR: Este barbero no existe')
            else:
                resultado = filtrar_citas_barbero(citas, barbero)
                mostrar_citas(resultado)

        elif opcion == '5':
            limpiar_pantalla()
            dia = pedir_texto('Dia: ')
            if dia not in DIAS:
                print('Este dia no es valido')
            else:
                resultado = filtrar_citas_dia(citas, dia)
                mostrar_citas(resultado)

        elif opcion == '6':
            limpiar_pantalla()
            cambio = cancelar_cita(citas)
            if cambio:
                guardar_cita(citas)

        elif opcion == '7':
            limpiar_pantalla()
            cambio = marcar_atendida(citas)
            if cambio:
                guardar_cita(citas)

        elif opcion == '8':
            limpiar_pantalla()
            mostrar_citas_pendientes(citas)

        elif opcion == '9':
            guardar_cita(citas)
            print('Saliendo...')
            break



main()
