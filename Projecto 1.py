import random
from timeit import repeat
import matplotlib.pyplot as plt
import numpy

tamanho_maximo = 10000

lista_test = [random.randint(0, 1000000) for iter in range(100)]
array_numpy_test = numpy.random.randint(0, 1000000, 100)

def search_in(search, collection):
    if search in collection:
        print(f'Encontrou {search} na coleção')
    # else:
    # print(f'Não encontrou {search} na coleção')


def search_pes(search, collection):
    for inteiro in collection:
        if inteiro == search:
            print(f'Encontrou {search} na coleção')
            break

        # print(f'Não encontrou {search} na coleção')


def search_bin(key, array):
    length = len(array)
    left = 0
    right = length - 1

    while (left <= right):
        middle = int((left + right) / 2)
        if array[middle] == key:
            print(f'Encontrou {key} na coleção')
            break
        if key < array[middle]:
            right = middle - 1
        if key > array[middle]:
            left = middle + 1
    # else:
    # print(f'Não encontrou {key} na coleção')


def tempos(key,collection):
    duration_search_in = sum(repeat(lambda: search_in(key, collection), number=1, repeat=35)) / 35
    duration_search_pes = sum(repeat(lambda: search_pes(key, collection), number=1, repeat=35)) / 35
    duration_search_bin = sum(repeat(lambda: search_bin(key, collection), number=1, repeat=35)) / 35

    return [duration_search_in, duration_search_pes, duration_search_bin]

non_max_value = max(lista_test) + 1
tempos_lista_npresente = tempos(non_max_value, lista_test)

print(f'Duração search_in,search_pes e search_bin: {tempos_lista_npresente}')

random_value = random.choice(lista_test)
tempos_lista_presente = tempos(random_value, lista_test)

non_max_value = max(array_numpy_test) + 1
tempos_array_npresente = tempos(non_max_value, array_numpy_test)

random_value = random.choice(array_numpy_test)
tempos_array_presente = tempos(random_value, array_numpy_test)

#plot para lista, valores não presentes
x = [i for i in range(1000, tamanho_maximo, 1000)]
y1 = []
y2 = []
y3 = []

for i in range(1000, tamanho_maximo, 1000):
    lista = [random.randint(0, 1000000) for iter in range(i)]
    non_max_value = max(lista) + 1
    tempos_lista = tempos(non_max_value, lista)
    y1.append(tempos_lista[0])
    y2.append(tempos_lista[1])
    y3.append(tempos_lista[2])

fig, ax = plt.subplots()
ax.plot(x, y1, label="In")
ax.plot(x, y2, label="Sequencial")
ax.plot(x, y3, label="Binária")

ax.set_xlabel('Tamanho lista')
ax.set_ylabel('Tempos execução')
ax.set_title("Lista, valores não presentes")
ax.legend()

plt.show()

#plot para lista, valores presentes
y1 = []
y2 = []
y3 = []

for i in range(1000, tamanho_maximo, 1000):
    lista = [random.randint(0, 1000000) for iter in range(i)]
    random_value = random.choice(lista)
    tempos_lista = tempos(random_value, lista)
    y1.append(tempos_lista[0])
    y2.append(tempos_lista[1])
    y3.append(tempos_lista[2])

fig, ax = plt.subplots()
ax.plot(x, y1, label="In")
ax.plot(x, y2, label="Sequencial")
ax.plot(x, y3, label="Binária")

ax.set_xlabel('Tamanho lista')
ax.set_ylabel('Tempos execução')
ax.set_title("Lista, valores presentes")
ax.legend()

plt.show()

#plot para array, valores não presentes
y1 = []
y2 = []
y3 = []

for i in range(1000, tamanho_maximo, 1000):
    arrayzinho = numpy.random.randint(0, 1000000, i)
    non_max_value = max(arrayzinho) + 1
    tempos_lista = tempos(non_max_value, arrayzinho)
    y1.append(tempos_lista[0])
    y2.append(tempos_lista[1])
    y3.append(tempos_lista[2])

fig, ax = plt.subplots()
ax.plot(x, y1, label="In")
ax.plot(x, y2, label="Sequencial")
ax.plot(x, y3, label="Binária")

ax.set_xlabel('Tamanho array')
ax.set_ylabel('Tempos execução')
ax.set_title("Array, valores não presentes")
ax.legend()

plt.show()

#plot para array, valores presentes
y1 = []
y2 = []
y3 = []

for i in range(1000, tamanho_maximo, 1000):
    arrayzinho = numpy.random.randint(0, 1000000, i)
    random_value = random.choice(arrayzinho)
    tempos_lista = tempos(random_value, arrayzinho)
    y1.append(tempos_lista[0])
    y2.append(tempos_lista[1])
    y3.append(tempos_lista[2])

fig, ax = plt.subplots()
ax.plot(x, y1, label="In")
ax.plot(x, y2, label="Sequencial")
ax.plot(x, y3, label="Binária")

ax.set_xlabel('Tamanho Array')
ax.set_ylabel('Tempos execução')
ax.set_title("Array, valores presentes")
ax.legend()

plt.show()