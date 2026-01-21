### ===== EJERCICIOS BÁSICOS DE OPERACIONES BANCARIAS (CON INPUT) =====

# ============================================
# EJERCICIO 1 - SUPER BÁSICO
# ============================================
# Calcula el interés simple que genera una cuenta de ahorros.
# Formula: interes = capital * tasa * tiempo
# Donde:
# - capital: es el dinero inicial en la cuenta
# - tasa: es la tasa de interés anual (ejemplo: 0.05 para 5%)
# - tiempo: es el tiempo en años
# Imprime el capital inicial, el interés ganado y el total final.

capital = 10000.0
tasa = 0.05
tiempo = 2

## Resolución aquí ##
# Formula interes = capital * tasa * tiempo
interes = capital * tasa * tiempo
total_final = capital + interes

# AHORA ANTES DE NADA SE REALIZARA EL MISMO EJEMPLO PERO CON INPUTS
def validate_float_value(prop):
    while True:
        try:
            value = float(input("Ingrese el valor de su " + prop + ":"))
            return value
        except ValueError:
            print("Valor invaido. Intente nuevamente.")
            

input_capital = validate_float_value("capital")
input_tasa = validate_float_value("tasa de interes")
input_tiempo = validate_float_value("tiempo")
    
print("Iniciado calculo de interes simple con los valores asignados:")
interes_input = input_capital * input_tasa * input_tiempo
total_final_input = input_capital + interes_input
    
print("El valor final del capital contando el interes es de: " + str(total_final_input))


# ============================================
# EJERCICIO 2 - SUPER BÁSICO
# ============================================
# Un cliente quiere hacer un depósito a su cuenta bancaria.
# Solicita al usuario el monto del depósito y suma ese valor
# al saldo actual de la cuenta. Imprime el saldo anterior,
# el monto depositado y el nuevo saldo.

saldo_actual = 5000.0

## Resolución aquí ##
monto = 1500.0
nuevo_saldo = saldo_actual + monto

# Aquí se imprimria con print("El saldo anterior es: ", saldo_actual)
# Aquí se imprimria con print("El monto depositado es: ", monto)
# Aquí se imprimria con print("El nuevo saldo es: ", nuevo_saldo)

# AHORA ANTES DE NADA SE REALIZARA EL MISMO EJEMPLO PERO CON INPUTS y con una nueva función no se debe usar la de arriba.
def validate_double_value(mensaje):
    while True:
        try:
            value = float(input(mensaje))
            return value
        except ValueError:
            print("Valor invaido. Intente nuevamente.")

input_saldo_actual = validate_double_value("Ingrese el saldo actual de su cuenta:")
input_monto = validate_double_value("Ingrese el monto a depositar:")
nuevo_saldo_input = input_saldo_actual + input_monto

print("El saldo anterior es: " + str(input_saldo_actual))
print("El monto depositado es: " + str(input_monto))
print("El nuevo saldo es: " + str(nuevo_saldo_input))

# ============================================
# EJERCICIO 3 - SUPER BÁSICO
# ============================================
# Verifica si un cliente puede realizar un retiro de su cuenta.
# Solicita al usuario el monto que desea retirar.
# Si tiene suficiente saldo, realiza el retiro y muestra el nuevo saldo.
# Si no tiene suficiente, muestra un mensaje de saldo insuficiente.

saldo_cuenta = 3000.0

## Resolución aquí ##

monto_retiro = 3500.0
if monto_retiro <= saldo_cuenta:
    nuevo_saldo_cuenta = saldo_cuenta - monto_retiro
    # Aquí se imprimiria con print("Retiro exitoso. Nuevo saldo: ", nuevo_saldo_cuenta)
else:
    # Aquí se imprimiria con print("Saldo insuficiente para realizar el retiro.")
    pass
## Siempre se hace el ejercicio luego con inputs y sin reciclar funciones, porque se supone que es un nuevo ejercicio.

def validate_money_value(mensaje):
    while True:
        try:
            value = float(input(mensaje))
            return value
        except ValueError:
            print("Valor invaido. Intente nuevamente.")
            
input_saldo_cuenta = validate_money_value("Ingrese el saldo actual de su cuenta:")
input_monto_retiro = validate_money_value("Ingrese el monto a retirar:")

if input_monto_retiro <= input_saldo_cuenta:
    nuevo_saldo_cuenta = input_saldo_cuenta - input_monto_retiro
    print("Retiro exitoso. el nuevo saldo es: " + str(nuevo_saldo_cuenta))
else:
    print("Saldo insuficiente para realizar el retiro.")

# ============================================
# EJERCICIO 4 - SUPER BÁSICO
# ============================================
# Un cliente tiene una lista de movimientos (depósitos positivos y retiros negativos).
# Calcula el saldo final de la cuenta después de aplicar todos los movimientos.
# Imprime cada movimiento y el saldo final.

saldo_inicial = 1000.0
movimientos = [500, -200, 300, -150, 1000]

## Resolución aquí ##

## Siempre se hace el ejercicio luego con inputs y sin reciclar funciones, porque se supone que es un nuevo ejercicio.

movimientos_input = []

def validate_numeric_value(mensaje, type_cast):
    while True:
        if type_cast == 'int':
            try:
                value = int(input(mensaje))
                return value
            except ValueError:
                print("Valor invaido. Intente nuevamente.")
        while type_cast == 'float':
            try:
                value = float(input(mensaje))
                return value
            except ValueError:
                print("Valor invaido. Intente nuevamente.")
        else:
            print("Tipo de dato no soportado. Use 'int' o 'float'.")
            return None
            
input_movimientos_veces = validate_numeric_value("Ingrese la cantidad de movimientos a registrar:", 'int')
for i in range(input_movimientos_veces):
    movimiento = validate_numeric_value("Ingrese el valor del movimiento (positivo para depósito, negativo para retiro):", 'float')
    movimientos_input.append(movimiento)

input_saldo_inicial = validate_numeric_value("Ingrese el saldo inicial de su cuenta:", 'float')
saldo_final = input_saldo_inicial
for movimiento in movimientos_input:
    saldo_final += movimiento
    print("Movimiento: " + str(movimiento) + ", Saldo actual: " + str(saldo_final))

print("Saldo final de la cuenta: " + str(saldo_final))

# ============================================
# EJERCICIO 5 - NIVEL INTERMEDIO
# ============================================
# Sistema de transferencias bancarias entre cuentas.
# Solicita al usuario:
# 1. El nombre de la cuenta origen
# 2. El nombre de la cuenta destino
# 3. El monto a transferir
# 
# Verifica que:
# - La cuenta origen exista
# - La cuenta destino exista
# - La cuenta origen tenga saldo suficiente
# - El monto sea mayor a 0
# 
# Si todo es correcto, realiza la transferencia y muestra los nuevos saldos.
# Si hay algún error, muestra un mensaje apropiado.
# Además, agrega una comisión del 2% por transferencia que se descuenta de la cuenta origen.

cuentas = {
    "Juan": 5000.0,
    "Maria": 3000.0,
    "Pedro": 7500.0,
    "Ana": 2000.0
}
    
