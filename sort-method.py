numbers = [50, 7, 5, 3]
# print(numbers)
# new1 = [5, 3, 50, 7]
# new1 = [3, 5, 7, 50]
# el salto siempre tiene que ser el resultado de tamaño de la longitud entre 2
# el salto tambien podria se le podria llamar la razón
salto = len(numbers) // 2
# Hacemos una condicional donde el salto no puede ser 0, minimo tiene que ser 1
while salto > 0:
    # recordemos i comezará desde salto, es decir 2 en este caso
    # el ciclo for se repetira 2 veces en el primer while porque 4(tamaño) - 2(salto) = 2
    for i in range(salto, len(numbers)):
        # en un principio el valor de j será 0, despúes 1
        j = i - salto
        while j >= 0:
            # aquí es donde realmente damos el salto, k sera j + salto
            # k = j + salto
            if numbers[j] <= numbers[j + salto]:
                break
            # Caso contrario hacemos el intercambio de indices
            aux = numbers[j]
            numbers[j] = numbers[j + salto]
            numbers[j + salto] = aux
            j -= 1
            # print(numbers)
    # por cada iteracion dividimos salto entre 2, porque necesitamos parejas de dos
    salto //= 2

print(numbers)


# myJ = 2-2

# while myJ >= 0:
#     myJ -= 1


# for i in range(1, 4):
#     print(f'hello')
# print(myJ)
