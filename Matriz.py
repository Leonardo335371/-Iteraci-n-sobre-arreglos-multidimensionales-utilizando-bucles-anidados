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


        def calcular_promedio_temperaturas_ciudades(datos_temperaturas, nombres_ciudades):
            """
            Calcula la temperatura de cada ciudad durante un período de tiempo.

            Parámetros:
            datos_temperaturas (lista): Lista 3D donde cada elemento es [ciudad][semana][día]
            nombres_ciudades (lista): Lista de nombres de ciudades correspondientes a los índices de datos_temperaturas

            Retorna:
            dict: Diccionario con nombres de ciudades como claves y sus temperaturas como valores
            """
            promedios_ciudades = {}

            # Proceso sobre cada ciudad
            for idx_ciudad in range(len(datos_temperaturas)):
                temperaturas_ciudad = []
                # Proceso sobre cada semana de la ciudad actual
                for semana in datos_temperaturas[idx_ciudad]:
                    # Proceso sobre la temperatura de cada día en la semana
                    for temp in semana:
                        temperaturas_ciudad.append(temp)

                # Calcular la temperatura de la ciudad
                if temperaturas_ciudad:  # Evitar división
                    promedio_temp = sum(temperaturas_ciudad) / len(temperaturas_ciudad)
                    promedios_ciudades[nombres_ciudades[idx_ciudad]] = round(promedio_temp, 2)
                else:
                    promedios_ciudades[nombres_ciudades[idx_ciudad]] = 0.0

            return promedios_ciudades


        # Ejemplo
        if __name__ == "__main__":
            # Datos de ejemplo: [ciudad][semana][día]
            # Suponiendo 2 ciudades, 2 semanas, 7 días por semana
            datos_temperaturas = [
                [  # Salinas, Santa Elena, Ecuador
                    [25.5, 26.0, 24.8, 25.2, 26.5, 27.0, 25.8],  # Semana 1
                    [26.2, 25.9, 26.4, 25.7, 26.8, 27.2, 26.0]  # Semana 2
                ],
                [  # Otra ciudad (por ejemplo: Guayaquil)
                    [28.0, 28.5, 27.8, 29.0, 28.2, 28.7, 29.5],  # Semana 1
                    [27.5, 28.0, 28.3, 27.9, 28.6, 29.1, 28.4]  # Semana 2
                ]
            ]

            nombres_ciudades = ["Salinas", "Guayaquil"]

            # Calcular promedios
            promedios = calcular_promedio_temperaturas_ciudades(datos_temperaturas, nombres_ciudades)

            # Mostrar resultados
            for ciudad, promedio_temp in promedios.items():
                print(f"Temperatura promedio en {ciudad}: {promedio_temp}°C")