from random import randint

def miller_rabin_test(n: int, k: int = 100) -> bool:
    # Nenhum numero menor que 2 eh primo
    if n < 2:
        return False

    # Casos base
    if n in [2,3]:
        return True
    
    # Numeros pares nao sao primos
    if n % 2 == 0:
        return False
    
    # Eh necessario decompor o n como 2^r * d + 1, sendo d um numero impar
    r, d = decompose(n-1)

    for _ in range(k):
        # Pegue um valor aleatorio entre [2, n-2]
        a = randint(2, n - 2)

        # x = a^d mod n
        x = pow(a, d, n)

        if x in (1, n - 1):
            continue
        
        continue_loop = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                continue_loop = True
        
        if continue_loop: continue

        return False

    return True

def decompose(n: int):
    r = 0

    while n % 2 ==0:
        r += 1 
        n = n / 2
    
    return r, n

    