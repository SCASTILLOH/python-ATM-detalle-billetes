class Cajero:
    def __init__(self, saldo_cajero=0, billete20=0, billete10=0):
        self.saldo_cajero = saldo_cajero
        self.billete20 = billete20
        self.billete10 = billete10
    
    def carga_billetes(self, billete20=0, billete10=0):
        self.billete20 += billete20
        self.billete10 += billete10
        self.saldo_cajero += ( billete20 * 20000) + (billete10 * 10000)
        print(f'Se carga billete20 = {billete20}')
        print(f'Se carga billete10 = {billete10}')
        print(f'Nuevo saldo del cajero: {self.saldo_cajero}')
         
    def saldo(self):
        print(f'Saldo cajero: {self.saldo_cajero}')
        print(f'Q Billete20 =>: {self.billete20} - $ {self.billete20 * 20000}')   
        print(f'Q Billete10 =>: {self.billete10} - $ {self.billete10 * 10000}')
    
    def giro(self, monto_solicitado):
        #monto_solicitado = int(input(f'Monto: '))
        
        billete20_utilizado = 0
        billete10_utilizado = 0
        monto_girado = 0        
        
        if monto_solicitado % 10000 > 0:
            print('Solo contamos con billetes de 20 y 10. Cambia tu monto solicitado.')
        else:
            if self.saldo_cajero >= monto_solicitado:

                print('***INFO INICIAL DE CAJERO***')
                print(f'Saldo cajero: {self.saldo_cajero}')
                print(f'Q Billete20 =>: {self.billete20} - $ {self.billete20 * 20000}')   
                print(f'Q Billete10 =>: {self.billete10} - $ {self.billete10 * 10000}')
     
                '''
                miestra haya billete20 y el monto sea divisible en 20000 
                => 20000 / 20000 == 1 => True
                => 15000 / 20000 == 0,75 => False
                '''
                while self.billete20 > 0 and int(monto_solicitado / 20000) >= 1: 
                    billete20_utilizado += 1
                    monto_solicitado -= 20000
                    self.billete20 -= 1
                    monto_girado += 20000
                print('****')
                
                '''
                miestra haya billete10 y el monto sea divisible en 10000 
                => 10000 / 10000 == 1 => True
                => 5000 / 10000 == 0,5 => False
                '''
                while self.billete10 > 0 and int(monto_solicitado / 10000) >= 1: 
                    billete10_utilizado += 1
                    monto_solicitado -= 10000
                    self.billete10 -= 1
                    monto_girado += 10000
                
                self.saldo_cajero -= monto_girado
                print('**RESUMEN GIRO**')
                print(f'Q billete20 utilizados => {billete20_utilizado} = $ {billete20_utilizado * 20000}')
                print(f'Q billete10 utilizados => {billete10_utilizado} = $ {billete10_utilizado * 10000}')
                print(f'Total girado => ${monto_girado}')
                print('**SALDO EN CAJERO**')
                print(f'Saldo cajero => ${self.saldo_cajero}')
                print(f'Q Billete20 =>: {self.billete20} - $ {self.billete20 * 20000}')   
                print(f'Q Billete10 =>: {self.billete10} - $ {self.billete10 * 10000}')
                
            else:
                print('Saldo insuficiente para giros.')

cajero = Cajero()
cajero.carga_billetes(billete20=50, billete10=20)
cajero.giro(200000)
cajero.giro(810000)