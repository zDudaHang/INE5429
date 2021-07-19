
from random import randint


def fermat_test(n: int, k: int = 100) -> bool:
    # Nenhum numero menor que 2 eh primo
    if n < 2:
        return False

    # Casos base
    if n in [2,3]:
        return True
    
    # Numeros pares nao sao primos
    if n % 2 == 0:
        return False
    
    for _ in range(k):
        # Pegue um valor entre [2,...,n-2]
        a = randint(2, n - 2)

        # a^(n-1) % n != 1 => Eh composto
        if pow(a, n - 1, n) != 1:
            return False
    
    # Provavelmente eh um primo
    return True