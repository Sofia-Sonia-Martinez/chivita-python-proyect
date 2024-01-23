def generar_secuencia(n):
    secuencia = [4]
    for i in range(2, n+1):
        siguiente_termino = secuencia[-1] + 4 + i - 2
        secuencia.append(siguiente_termino)
    return secuencia

# Generar los primeros 200 términos de la secuencia
n_terminos = 200
secuencia_200 = generar_secuencia(n_terminos)

# Imprimir la secuencia
print(secuencia_200)

