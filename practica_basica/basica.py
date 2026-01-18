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


# ============================================
# EJERCICIO 2 - SUPER BÁSICO
# ============================================
# Un cliente quiere hacer un depósito a su cuenta bancaria.
# Solicita al usuario el monto del depósito y suma ese valor
# al saldo actual de la cuenta. Imprime el saldo anterior,
# el monto depositado y el nuevo saldo.

saldo_actual = 5000.0


# ============================================
# EJERCICIO 3 - SUPER BÁSICO
# ============================================
# Verifica si un cliente puede realizar un retiro de su cuenta.
# Solicita al usuario el monto que desea retirar.
# Si tiene suficiente saldo, realiza el retiro y muestra el nuevo saldo.
# Si no tiene suficiente, muestra un mensaje de saldo insuficiente.

saldo_cuenta = 3000.0


# ============================================
# EJERCICIO 4 - SUPER BÁSICO
# ============================================
# Un cliente tiene una lista de movimientos (depósitos positivos y retiros negativos).
# Calcula el saldo final de la cuenta después de aplicar todos los movimientos.
# Imprime cada movimiento y el saldo final.

saldo_inicial = 1000.0
movimientos = [500, -200, 300, -150, 1000]


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
    
