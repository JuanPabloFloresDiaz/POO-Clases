# Validaciones.py
### Clase Validaciones que contiene métodos estáticos para validar diferentes tipos de datos
class Validaciones:
    # Método para validar la longitud de una cadena
    @staticmethod
    def validate_length(input_str, min_length=None, max_length=None):
        """Valida la longitud de una cadena"""
        if min_length is not None and len(input_str) < min_length:
            return False
        if max_length is not None and len(input_str) > max_length:
            return False
        return True
    # Método para validar un rango numérico
    @staticmethod
    def validate_range(value, min_value=None, max_value=None):
        """Valida que un valor numérico esté dentro de un rango"""
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True
    # Métodos para validar diferentes tipos de datos
    ### Método para validar un número entero
    @staticmethod
    def validate_integer(input_str):
        """Valida que la entrada sea un número entero válido"""
        return input_str.lstrip('-').isdigit()
    ### Método para validar un número decimal
    @staticmethod
    def validate_double(input_str):
        """Valida que la entrada sea un número decimal válido"""
        try:
            float(input_str)
            return True
        except ValueError:
            return False
    ### Método para obtener mensajes de error específicos
    @staticmethod
    def get_validation_message(validation_type, **kwargs):
        """Retorna mensajes de error específicos para cada tipo de validación"""
        messages = {
            'length': f"El texto debe tener entre {kwargs.get('min_length', 'N/A')} y {kwargs.get('max_length', 'N/A')} caracteres.",
            'range': f"El valor debe estar entre {kwargs.get('min_value', 'N/A')} y {kwargs.get('max_value', 'N/A')}.",
            'integer': "Eso no es un número entero válido. Intenta de nuevo.",
            'double': "Eso no es un número decimal válido. Intenta de nuevo.",
            'empty': "El campo no puede estar vacío."
        }
        return messages.get(validation_type, "Entrada inválida. Intenta de nuevo.")