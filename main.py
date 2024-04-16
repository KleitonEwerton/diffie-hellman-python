# Escolha de p deve ser um primo (caso não dará erro) https://www.wolframalpha.com/input?i=primitiveroot+23
p = 23


import random

class DiffieHellman:
    def __init__(self, p, g):
        self.p = p
        self.g = g

    # Gera a chave privada
    def generate_private_key(self):
        return random.randint(1, self.p - 1)  # private key should be in [2, p-2]

    # Calcula a chave pública
    def calculate_public_key(self, private_key):
        return pow(self.g, private_key, self.p)

    # Calcula o segredo compartilhado
    def calculate_shared_secret(self, other_public_key, own_private_key):
        return pow(other_public_key, own_private_key, self.p)

# Algoritmo de Euclides para encontrar o MDC
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Verifica se g é um gerador primitivo de p
def is_primitive_root(g, p):
    if gcd(g, p) != 1:
        return False
    powers = set()
    for i in range(1, p):
        powers.add(pow(g, i, p))
    return len(powers) == p - 1

# Encontra um gerador primitivo de p
def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

def main():
    
    # Encontrando um gerador primitivo para p verifique aqui: https://www.wolframalpha.com/input?i=primitiveroot+23
    g = find_primitive_root(p)

    # Criando duas instâncias do DiffieHellman para cada participante
    alice = DiffieHellman(p, g)
    bob = DiffieHellman(p, g)

    # Gerando chaves privadas para Alice e Bob
    a_private = alice.generate_private_key()
    b_private = bob.generate_private_key()

    # Calculando as chaves públicas de Alice e Bob
    a_public = alice.calculate_public_key(a_private)
    b_public = bob.calculate_public_key(b_private)

    # Troca de chaves públicas
    shared_secret_a = alice.calculate_shared_secret(b_public, a_private)
    shared_secret_b = bob.calculate_shared_secret(a_public, b_private)

    # Verificando se os segredos compartilhados são iguais (que devem ser)
    assert shared_secret_a == shared_secret_b

    print("p:", p)
    print("g:", g)
    print("Chave privada de Alice (a):", a_private)
    print("Chave privada de Bob (b):", b_private)
    print("Chave pública de Alice (A):", a_public)
    print("Chave pública de Bob (B):", b_public)
    print("Segredo compartilhado a:", shared_secret_a)
    print("Segredo compartilhado b:", shared_secret_a)
    print("S:", shared_secret_a)


if __name__ == "__main__":
    main()
