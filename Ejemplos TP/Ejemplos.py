class CuentaBancaria:
   __saldo = 0
   def __init__ (self,saldo):
       self.__saldo = saldo
   def getSaldo(self):
       return self.__saldo
   def copy(self):
       otraCuenta = CuentaBancaria(self.__saldo)
       return otraCuenta
       

if __name__ == '__main__':
      Cuenta1 = CuentaBancaria(100)
      Cuenta2 = Cuenta1.copy()
      print(Cuenta2.getSaldo())