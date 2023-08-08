class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.saude = 100  # Saúde inicial

    def fazer_som(self):
        pass

    def alimentar(self):
        self.saude += 10
        return f"{self.nome} foi alimentado(a) e sua saúde aumentou para {self.saude}%."

    def verificar_saude(self):
        return f"A saúde de {self.nome} está em {self.saude}%."

class Gado(Animal):
    def __init__(self, nome):
        super().__init__(nome, 'Gado')

    def fazer_som(self):
        return "Muuu!"

    def produzir_carne(self):
        return f"Carne de {self.nome}"

class Galinha(Animal):
    def __init__(self, nome):
        super().__init__(nome, 'Galinha')

    def fazer_som(self):
        return "Cóóó!"

    def produzir_ovos(self):
        return f"Ovos da {self.nome}"

# Simulação
gado1 = Gado("Boi Manso")
galinha1 = Galinha("Dona Galinha")

print(gado1.fazer_som())  # Saída: Muuu!
print(gado1.produzir_carne())  # Saída: Carne de Boi Manso

print(galinha1.fazer_som())  # Saída: Cóóó!
print(galinha1.produzir_ovos())  # Saída: Ovos da Dona Galinha

print(gado1.alimentar())  # Saída: Boi Manso foi alimentado(a) e sua saúde aumentou para 110%.
print(gado1.verificar_saude())  # Saída: A saúde de Boi Manso está em 110%.

print(galinha1.alimentar())  # Saída: Dona Galinha foi alimentado(a) e sua saúde aumentou para 110%.
print(galinha1.verificar_saude())  # Saída: A saúde de Dona Galinha está em 110%.
