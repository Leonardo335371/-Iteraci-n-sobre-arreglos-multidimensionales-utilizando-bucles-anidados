# Definir las dimensiones de la matriz 3D: ciudades, días, semanas
ciudades = ["Salinas", "La Libertad", "Santa Elena"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3"]

# Creación de la matriz 3D con temperaturas de ejemplo (en °C)
# Dimensiones: 3 ciudades x 7 días x 3 semanas
temperaturas = [
    [  # Salinas
        [25, 26, 24, 23, 22, 21, 20],  # Semana 1
        [27, 28, 26, 25, 24, 23, 22],  # Semana 2
        [24, 25, 23, 22, 21, 20, 19],  # Semana 3
    ],
    [  # La Libertad
        [30, 31, 29, 28, 27, 26, 25],  # Semana 1
        [32, 33, 31, 30, 29, 28, 27],  # Semana 2
        [29, 30, 28, 27, 26, 25, 24],  # Semana 3
    ],
    [  # Santa Elena
        [20, 21, 19, 18, 17, 16, 15],  # Semana 1
        [22, 23, 21, 20, 19, 18, 17],  # Semana 2
        [19, 20, 18, 17, 16, 15, 14],  # Semana 3
    ]
]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i in range(len(ciudades)):
    print(f"\nPromedios de temperatura para {ciudades[i]}:")
    for j in range(len(semanas)):
        suma_temperaturas = 0
        for k in range(len(dias)):
            suma_temperaturas += temperaturas[i][j][k]
        promedio = suma_temperaturas / len(dias)
        print(f"{semanas[j]}: {promedio:.2f} °C")