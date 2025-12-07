# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not require class or instance access."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: uses cls to access class attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
