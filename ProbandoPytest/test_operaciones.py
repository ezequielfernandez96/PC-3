import pytest
from operaciones import Operaciones
from funciones_extra import FuncionesExtra

def test_sumar():
    op = Operaciones()
    assert op.sumar(3, 2) == 5
    
def test_restar():
    op = Operaciones()
    assert op.restar(3, 2) == 1
    
def test_multiplicar():
    op = FuncionesExtra()  # Instanciar la clase correctamente
    assert op.multiplicar(3, 2) == 6
    
def test_dividir():
    op = FuncionesExtra()  # Instanciar la clase correctamente
    assert op.dividir(10, 0) == 0


