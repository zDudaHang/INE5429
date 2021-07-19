import time
from util import find_number_of_bits
from lcg import LCG
from bbs import BBS

solicited_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

seed =  int(time.time())

lcg = LCG(seed=seed)

# Como o SO pode escalonar os processos, 
# eh importante considerar mais de um numero gerado para encontrar um valor mais proximo da realidade
quantity_of_numbers = 100

with open("./generate_random.txt", "w") as writer:
    writer.write("===== LCG =====\n")
    for numBits in solicited_bits:
        # Colocando o valor do parametro m
        lcg.__m__(numBits)

        avg_time = 0.0

        writer.write(f"Começando a gerar números de {numBits} bits\n")
        for _ in range(quantity_of_numbers):

            start = time.time()

            value = lcg.next()

            final = time.time()

            # Pega a quantidade de bits que a saida gerou
            bits = find_number_of_bits(value)

            # Verifica se a quantidade de bits foi realmente atendida
            assert(numBits == bits)

            time_to_generate = final - start

            avg_time += (time_to_generate / quantity_of_numbers)

            writer.write(f"bits = {bits} => {time_to_generate} segundos\n")
        writer.write(f"O tempo médio para gerar um número com {numBits} bits foi {avg_time} segundos\n")

    bbs = BBS(seed=seed)

    writer.write("===== BBS =====\n")
    for numBits in solicited_bits:

        avg_time = 0.0

        writer.write(f"Começando a gerar números de {numBits} bits\n")
        for _ in range(quantity_of_numbers):

            start = time.time()

            value = bbs.generate(num_bits=numBits)

            final = time.time()

            # Pega a quantidade de bits que a saida gerou
            bits = find_number_of_bits(value)

            # Verifica se a quantidade de bits foi realmente atendida
            assert(numBits == bits)

            time_to_generate = final - start

            avg_time += (time_to_generate / quantity_of_numbers)

            writer.write(f"bits = {bits} => {time_to_generate} segundos\n")
        writer.write(f"O tempo médio para gerar um número com {numBits} bits foi {avg_time} segundos\n")
