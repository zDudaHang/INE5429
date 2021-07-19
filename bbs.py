from math import gcd

class BBS:
    def __init__(self, seed: int = 1, p: int = 3141592653589771, q: int = 2718281828459051) -> None:
        if p == q:
            raise ValueError("Os valores de p e q não podem ser iguais")
        if p % 4 != 3 or q % 4 != 3:
            raise ValueError("Os valores de p e q devem ser congruentes a 3 (mod 4)")
        if gcd(p,q) != 1:
            raise ValueError("Os valores p e q devem ser relativamente primos, ou seja, gcd(p,q) = 1")
        self.m = p * q
        self.state = seed
    
    def next(self):
        # X_n+1 = ( X_n ^ 2 ) mod m
        self.state = pow(self.state, 2, self.m)
        
        # B_n = X_n mod 2
        return self.state % 2
    
    def generate(self, num_bits: int, prime: bool = False) -> int:
        number = 0
        for _ in range(num_bits):
            number = (number << 1) | self.next()
        
        # Se o valor nao atender ao numero de bits, coloque o valor 1 no MSB
        # if number < (2**(num_bits - 1)):
        #     number = 1 << num_bits - 1 | number

        if number < (2**(num_bits - 1)):
            return self.generate(num_bits, prime)
        
        # Nao retornar numeros pares caso estejam pedindo um primo, eh perda de tempo
        if prime:
            return number | 1
        
        return number