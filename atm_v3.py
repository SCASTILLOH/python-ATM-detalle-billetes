class Cajero:
    def __init__(self, saldo_cajero=0, billete_minimo=0):
        self.saldo_cajero = saldo_cajero
        self.billete_minimo = billete_minimo
        
        
        self.billetes = [
            {'type': 'billete20', 'quantity': 0, 'value_type': 20000, 'saldo': 0},
            {'type': 'billete10', 'quantity': 0, 'value_type': 10000, 'saldo': 0},
            {'type': 'billete5', 'quantity': 0, 'value_type': 5000, 'saldo': 0},
        ]
    
    def imprime_ticket_carga_billetes(self, **kwargs):
        for k, v in kwargs.items():
            tmp = [item for item in self.billetes if item['type'] == k][0]
            print('Se carga {} => Q={} => Total$ {}'.format(k, v, v * tmp['value_type']))
        print(f'Nuevo saldo del cajero: {self.saldo_cajero}')
    
    def carga_billetes(self, *args, **kwargs):
        print('========CARGA BILLETES==========')
        for k,v in kwargs.items():
            tmp = [item for item in self.billetes if item['type'] == k][0]
            tmp['quantity'] = v
            tmp['saldo'] = v * tmp['value_type']
            self.saldo_cajero += tmp['saldo']
        self.imprime_ticket_carga_billetes(**kwargs)
         
    def saldo(self):
        print(f'Saldo cajero: {self.saldo_cajero}')
    
    def giro(self, monto_solicitado=0):
        #monto_solicitado = int(input(f'Monto: '))
        self.monto_solicitado = monto_solicitado
        
        if monto_solicitado % self.billete_minimo > 0:
            print('Solo contamos con billetes de 20 y 10. Cambia tu monto solicitado.')
        else:
            if self.saldo_cajero >= monto_solicitado:

                print('========GIRO==========')
                print('***INFO INICIAL DE CAJERO***')
                self.saldo()
                print('**RESUMEN GIRO**')
                print(f'Monto de giro solicitado: {self.monto_solicitado}')
                
                transaccion = []
                def procesa_giro():
                    for item in self.billetes:
                        dt = {}
                        dt[item['type']] = {'utilizado': 0, 'monto_girado': 0}
                        while item['quantity'] > 0 and int(self.monto_solicitado / item['value_type']) >= 1: 
                            dt[item['type']]['utilizado'] += 1
                            self.monto_solicitado -= item['value_type']
                            item['quantity'] -= 1
                            dt[item['type']]['monto_girado'] += item['value_type']
                        self.saldo_cajero -= dt[item['type']]['monto_girado']  
                        transaccion.append(dt)
                              
                print('*Detalle: ')
                procesa_giro()
                
                for detalle in transaccion:
                    for k, v in detalle.items():
                        print('  {} utilizados {} = $ {:_}'.format(k, v['utilizado'], v['monto_girado']))
                
                self.saldo()
            else:
                print('Saldo insuficiente para giros.')

cajero = Cajero(billete_minimo=5000)
print()
cajero.carga_billetes(billete20=4, billete10=2, billete5=3)
print()
cajero.saldo()
print()
cajero.giro(50000)
print()
cajero.giro(65000)
print()


                
                