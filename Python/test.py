from cuentaBancaria import CuentaBancaria

x = CuentaBancaria(10,"felipe","morales")

print(x.datos_titular())

x.depositar(1000000)
print(x.datos_saldo())

x.extraer(900000)
print(x.datos_saldo())

print(x.datos_movimientos())