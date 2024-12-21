# Prueba Técnica para Programador Junior - Python

**Duración total**: 30 minutos

**Objetivo**: Evaluar conocimientos básicos de programación orientada a objetos, lógica de programación y uso de estructuras de datos en Python.

## Estructura de Archivos

```plaintext
.
├── parte1
│   ├── producto.py         # Código de la Parte 1
│   └── test_producto.py    # Pruebas unitarias para la Parte 1
├── parte2
│   ├── logica.py           # Código de la Parte 2
│   └── test_logica.py      # Pruebas unitarias para la Parte 2
├── README.md               # Documentación de la prueba técnica
└── runner.py               # Script para ejecutar las pruebas
```

## Instrucciones

### Parte 1: Programación Orientada a Objetos

- **Archivo**: `parte1/producto.py`
- **Pruebas**: `parte1/test_producto.py`

Implementa la clase `Producto` con los atributos y métodos descritos en las instrucciones de la prueba.

Ejecuta las pruebas para verificar la implementación:
```bash
python3 -m unittest discover -s parte1 -p "test_*.py"
```

### Parte 2: Lógica de Programación y Estructuras de Datos

- **Archivo**: `parte2/logica.py`
- **Pruebas**: `parte2/test_logica.py`

Implementa las funciones `fibonacci` y `analizar_texto`.

Ejecuta las pruebas para verificar la implementación:
```bash
python3 -m unittest discover -s parte2 -p "test_*.py"
```

### Ejecución General de Pruebas

Usa el archivo `runner.py` para ejecutar todas las pruebas de ambas partes:
```bash
python3 runner.py
```

---

## Parte 1: Programación Orientada a Objetos (15 puntos)

### Clase Producto (15 puntos)

- **Atributos**:
  - `nombre` (str)
  - `precio` (float)
  - `cantidad` (int)

- **Métodos**:
  - `__init__`: Inicializa los atributos.
  - `calcular_total`: Devuelve el precio total del producto (precio × cantidad).
  - `__str__`: Devuelve la representación en formato:
    ```python
    Producto(nombre=Nombre, precio=Precio, cantidad=Cantidad)
    ```

#### Ejemplo de uso:
```python
p1 = Producto("Laptop", 1500.0, 2)
print(p1.calcular_total())  # 3000.0
print(p1)  # Producto(nombre=Laptop, precio=1500.0, cantidad=2)
```

---

## Parte 2: Lógica de Programación y Estructuras de Datos (15 puntos)

### Fibonacci Recursivo (10 puntos)

Escribe una función `fibonacci(n)` que calcule el n-ésimo número de la secuencia de Fibonacci de forma recursiva.

#### Ejemplo de uso:
```python
print(fibonacci(6))  # 8
```

### Análisis de Texto (5 puntos)

Crea una función `analizar_texto(texto)` que reciba un texto como cadena y devuelva un diccionario con:
- Número de palabras.
- Número de letras (excluyendo espacios).

#### Ejemplo de uso:
```python
texto = "Hola mundo"
print(analizar_texto(texto))
# {'palabras': 2, 'letras': 9}
```

---

## Criterios de Evaluación

- **Puntaje total**: 30 puntos.
- **Aprobación mínima**: 20 puntos.

### Parte 1: Programación Orientada a Objetos (15 puntos)

1. **Definición de clase y atributos (3 puntos):**
   - La clase `Producto` está correctamente definida con los atributos `nombre`, `precio`, y `cantidad`.

2. **Método `__init__` (3 puntos):**
   - El constructor inicializa correctamente los atributos.

3. **Método `calcular_total` (4 puntos):**
   - Calcula correctamente el precio total (`precio × cantidad`).

4. **Método `__str__` (5 puntos):**
   - Devuelve una representación clara y en el formato especificado.

### Parte 2: Lógica de Programación y Estructuras de Datos (15 puntos)

1. **Fibonacci Recursivo (10 puntos):**
   - Lógica correcta (6 puntos).
   - Eficiencia básica (2 puntos).
   - Resultados esperados (2 puntos).

2. **Análisis de Texto (5 puntos):**
   - Cálculo del número de palabras (2 puntos).
   - Cálculo del número de letras (2 puntos).
   - Formato del diccionario (1 punto).

---

## Notas de Evaluación

- **Errores menores:** Resta hasta 1 punto por detalles menores (nombres incorrectos de variables, errores de formato).
- **Errores críticos:** Fallos que generan excepciones o resultados incorrectos restan la totalidad de los puntos asignados al criterio correspondiente.

