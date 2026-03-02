# Teclado.py
# Importamos la clase Validaciones que contiene las funciones de validación
from Validaciones import Validaciones

# Creamos la clase Teclado que contendrá los métodos para leer diferentes tipos de datos
class Teclado:
    # Métodos estáticos para leer diferentes tipos de datos del teclado
    ### Método para leer un número entero con validaciones
    @staticmethod
    def read_integer(mensaje, min_digits=None, max_digits=None, min_value=None, max_value=None):
        """Lee un número entero del teclado con validaciones"""
        while True:
            entrada = input(f"{mensaje} ").strip()
            
            if not entrada:
                print(Validaciones.get_validation_message('empty'))
                continue
            
            if not Validaciones.validate_integer(entrada):
                print(Validaciones.get_validation_message('integer'))
                continue
            
            numero = int(entrada)
            num_str = str(abs(numero))
            
            if min_digits is not None or max_digits is not None:
                if not Validaciones.validate_length(num_str, min_digits, max_digits):
                    print(f"El número debe tener entre {min_digits or 'cualquier'} y {max_digits or 'cualquier'} dígitos.")
                    continue
            
            if min_value is not None or max_value is not None:
                if not Validaciones.validate_range(numero, min_value, max_value):
                    print(Validaciones.get_validation_message('range', min_value=min_value, max_value=max_value))
                    continue
            
            return numero

    ### Método para leer un número decimal con validaciones
    @staticmethod
    def read_double(mensaje, min_value=None, max_value=None):
        """Lee un número decimal del teclado con validaciones"""
        while True:
            entrada = input(f"{mensaje} ").strip()
            
            if not entrada:
                print(Validaciones.get_validation_message('empty'))
                continue
            
            if not Validaciones.validate_double(entrada):
                print(Validaciones.get_validation_message('double'))
                continue
            
            valor = float(entrada)
            
            if min_value is not None or max_value is not None:
                if not Validaciones.validate_range(valor, min_value, max_value):
                    print(Validaciones.get_validation_message('range', min_value=min_value, max_value=max_value))
                    continue
            
            return valor

    ### Método para leer texto con validaciones
    @staticmethod
    def read_text(mensaje, min_length=None, max_length=None):
        """Lee texto del teclado con validaciones de longitud"""
        while True:
            texto = input(f"{mensaje} ").strip()
            
            if not texto:
                print(Validaciones.get_validation_message('empty'))
                continue
            
            if not Validaciones.validate_length(texto, min_length, max_length):
                print(Validaciones.get_validation_message('length', min_length=min_length, max_length=max_length))
                continue
            
            return texto