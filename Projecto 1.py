import random
from timeit import repeat
import numpy

lista = list([random.randint(0, 1000001) for iter in range(100)])
array_numpy = numpy.random.randint(0,1000001,(100))

def search_in(search,collection):
    if search in collection:
        print(f'Encontrou {search} na coleção')
    else:
        print(f'Não encontrou {search} na coleção')

def search_pes(search, collection):
    for inteiro in collection:
        if inteiro==search :
            print(f'Encontrou {search} na coleção')
        break

        print(f'Não encontrou {search} na coleção')

def search_bin(key, array):
    length = len(array)
    left = 0
    right = length - 1

    while(left <= right):
        middle = int((left + right)/2)
        if array[middle] == key:
            print(f'Encontrou {key} na coleção')
            break
        if key < array[middle]:
            right = middle - 1
        if key > array[middle]:
            left = middle + 1
    else:
        print(f'Não encontrou {key} na coleção')

non_max_value = max(lista) + 1

print('Tempos lista, valor não presente:')
duration_search_in = min(repeat(lambda: search_in(non_max_value,lista), number=1, repeat=35))
duration_search_pes = min(repeat(lambda: search_pes(non_max_value,lista), number=1, repeat=35))
duration_search_bin = min(repeat(lambda: search_bin(non_max_value,lista), number=1, repeat=35))
print(f'Duração search_in: {duration_search_in}')
print(f'Duração search_pes: {duration_search_pes}')
print(f'Duração search_bin: {duration_search_bin}')

non_max_value = max(array_numpy) + 1

print('Tempos array, valor não presente:')
duration_search_in = min(repeat(lambda: search_in(non_max_value,array_numpy), number=1, repeat=35))
duration_search_pes = min(repeat(lambda: search_pes(non_max_value,array_numpy), number=1, repeat=35))
duration_search_bin = min(repeat(lambda: search_bin(non_max_value,array_numpy), number=1, repeat=35))
print(f'Duração search_in: {duration_search_in}')
print(f'Duração search_pes: {duration_search_pes}')
print(f'Duração search_bin: {duration_search_bin}')

random_value = random.choice(lista)

print('Tempos lista, valor presente:')
duration_search_in = min(repeat(lambda: search_in(random_value,lista), number=1, repeat=35))
duration_search_pes = min(repeat(lambda: search_pes(random_value,lista), number=1, repeat=35))
duration_search_bin = min(repeat(lambda: search_bin(random_value,lista), number=1, repeat=35))
print(f'Duração search_in: {duration_search_in}')
print(f'Duração search_pes: {duration_search_pes}')
print(f'Duração search_bin: {duration_search_bin}')

random_value = random.choice(array_numpy)

print('Tempos lista, valor presente:')
duration_search_in = min(repeat(lambda: search_in(random_value,array_numpy), number=1, repeat=35))
duration_search_pes = min(repeat(lambda: search_pes(random_value,array_numpy), number=1, repeat=35))
duration_search_bin = min(repeat(lambda: search_bin(random_value,array_numpy), number=1, repeat=35))
print(f'Duração search_in: {duration_search_in}')
print(f'Duração search_pes: {duration_search_pes}')
print(f'Duração search_bin: {duration_search_bin}')

