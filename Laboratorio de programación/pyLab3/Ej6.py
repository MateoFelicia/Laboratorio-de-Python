#6. map() con lambda

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))

print(cuadrados) #[1, 4, 16, 49]