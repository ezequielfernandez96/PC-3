class CuentaBancaria():
    def __init__(self,saldo_inicial,nombre,apellido,moneda="$"):
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda
        
    def depositar(self,monto):                                 #realiza un deposito en la cuenta
        self.movimientos.append("deposito:" + str(monto))      #agrega a la lista vacia "deposito: " + el monto
        self.saldo = self.saldo + monto                        # suma el saldo + el monto ingresado
        
    def extraer(self,monto):                                   #realiza una extracción en la cuenta
        if self.saldo - monto >= 0:                            #si el saldo - el monto es mayor o igual cero
            self.movimientos.append("extracción: " + str(monto))  #agrega a la lista vacia "extraccion:" + el monto ingresado
            self.saldo = self.saldo - monto                       #devuelve el saldo - el monto
        else:
            self.movimientos.append("saldo insuficiente: " + str(monto))  #si no se cumple que sea mayor o igual cero devuelve saldo insuficiente
            print("saldo insuficiente")
    
    def datos_titular(self):
        return self.apellido + "," + self.nombre + "con el saldo" + str(self.saldo) + "" + self.moneda
    
    def datos_saldo(self):
        return self.saldo
    
    def _reset_saldo(self):
        self.saldo = 0
        
    def datos_movimientos(self):
        return list(self.movimientos)