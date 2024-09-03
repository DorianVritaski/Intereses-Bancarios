class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def actualizar_saldo(self):
        if self.saldo < 10000.00:
            self.saldo *= 1.03
        else:
            self.saldo *= 1.04

    def mostrar_saldo(self):
        print(f"Saldo final es {self.saldo:.2f}")

# Uso de la clase
def main():
    saldo_inicial = float(input("Dame el saldo actual: "))
    cuenta = CuentaBancaria(saldo_inicial)
    cuenta.actualizar_saldo()
    cuenta.mostrar_saldo()

if __name__ == "__main__":
    main()
