# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

def calcular_area_base(raio):
    return math.pi * (raio ** 2)

def calcular_volume_cilindro(raio, altura):
    return calcular_area_base(raio) * altura
