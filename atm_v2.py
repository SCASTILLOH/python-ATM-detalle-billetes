
class Cajero:
    def __init__(self):
        self.saldo_cajero = 0
        self.billete20 = 99
        self.billete10 = 0
        
        self.billetes_stock = {'billete20': 0, 'billete10':0}

        self.billetes_valor = {'billete20': 20000,
                               'billete10': 10000}

    def carga_billetes(self, billete20=0, billete10=0):

        print('========CARGA DE BILLETES==========')
        print(f'Saldo inicial cajero = {self.saldo_cajero}')
        self.billetes_stock['billete20'] += billete20
        self.billetes_stock['billete10'] += billete10
        self.saldo_cajero += (billete20 * self.billetes_valor['billete20']) + (billete10 * self.billetes_valor['billete10'])

        print('Se carga billete20 = {} >= ${}'.format(billete20, billete20 * self.billetes_valor['billete20']))
        print('Se carga billete10 = {} >= ${}'.format(billete10, billete10 * self.billetes_valor['billete10']))
        print(f'Nuevo saldo del cajero: {self.saldo_cajero}')
        print('===================================')

    def saldo(self):
        print('========SALDO CAJERO==========')
        print(f'Saldo cajero: {self.saldo_cajero}')
        print('Q Billete20 =>: {} - $ {}'.format(self.billetes_stock['billete20'], self.billetes_stock['billete20'] * self.billetes_valor['billete20']))
        print('Q Billete10 =>: {} - $ {}'.format(self.billetes_stock['billete10'], self.billetes_stock['billete10'] * self.billetes_valor['billete10']))
        print('==============================')


    def giro(self, monto_solicitado):
        #monto_solicitado = int(input(f'Monto: '))

        transaccion = []

        if monto_solicitado % 10000 > 0:
            print('Solo contamos con billetes de 20 y 10. Cambia tu monto solicitado.')
        else:
            if self.saldo_cajero >= monto_solicitado:
                print()
                print('========GIRO==========')
                print(f'Monto solicitado: ${monto_solicitado:_}')
                print('******INFO INICIAL DE CAJERO***')
                print(f'Saldo cajero: {self.saldo_cajero:_}')
                for billete, stock in self.billetes_stock.items():
                    print('Q {} =>: {} - $ {:_}'.format(billete, stock, stock*self.billetes_valor[billete]))
                
                for billete, stock in self.billetes_stock.items():
                    d = {billete: {'utilizado': 0, 'monto_girado': 0}}
                    while self.billetes_stock[billete] > 0 and int(monto_solicitado / self.billetes_valor[billete]) >= 1:
                        d[billete]['utilizado'] += 1
                        monto_solicitado -= self.billetes_valor[billete]
                        self.billetes_stock[billete] -= 1
                        d[billete]['monto_girado'] += self.billetes_valor[billete]
                        
                    transaccion.append(d)
                
                total_girado = 0
                
                print('**RESUMEN GIRO**')
                for item in transaccion:
                    for k, v in item.items():
                        print('Q {} utilizados => {} = $ {:_}'.format(k, v['utilizado'], v['utilizado'] * self.billetes_valor[k]))
                        total_girado += v['utilizado'] * self.billetes_valor[k]
                print(f'Total girado => ${total_girado:_}')
                
                self.saldo_cajero -= total_girado
                
                
                print('**SALDO EN CAJERO**')
                print(f'Saldo cajero => ${self.saldo_cajero}')
                print('Q Billete20 =>: {} - $ {}'.format(self.billetes_stock['billete20'], self.billetes_stock['billete20'] * self.billetes_valor['billete20']))
                print('Q Billete10 =>: {} - $ {}'.format(self.billetes_stock['billete10'], self.billetes_stock['billete10'] * self.billetes_valor['billete10']))
           
            else:
                print('Saldo insuficiente para giros.')


cajero2 = Cajero()
cajero2.carga_billetes(billete20=4, billete10=100)
print()
# cajero2.carga_billetes(billete20=100, billete10=500)
cajero2.giro(1000000)


                
                