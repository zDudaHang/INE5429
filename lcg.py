
class LCG:
    def __init__(self, seed: int = 1, num_bits: int = 32, a: int = 1664525, c : int = 1013904223) -> None:
        self.num_bits = num_bits
        self.m = 2 ** num_bits
        self.a = a
        self.c = c
        self.state = seed

    def __m__(self, num_bits: int):
        self.num_bits = num_bits
        self.m = 2 ** num_bits

    def next(self, prime: bool = False):
        # X_n+1 = (a * X_n - c) mod m
        self.state = (self.a * self.state + self.c) % self.m

        # Enquanto o número não tiver o bit mais significativo igual a 1, esse numero nao contem a quantidade de bits necessaria
        while self.state < (2**(self.num_bits - 1)):
            self.state = (self.a * self.state + self.c) % self.m
        
        # Nao retornar numeros pares caso estejam pedindo um primo, eh perda de tempo
        if prime:
            return self.state | 1
        
        return self.state