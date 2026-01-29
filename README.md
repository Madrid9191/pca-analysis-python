# 📊 Análisis de Componentes Principales (PCA) en Python

Implementación completa, manual y educativa del **Análisis de Componentes Principales (Principal Component Analysis, PCA)** usando Python.

Este proyecto permite:

✔ Preprocesamiento automático de datos  
✔ Codificación de variables categóricas  
✔ Estandarización  
✔ Cálculo manual de autovalores y autovectores  
✔ Visualización avanzada  
✔ Exportación de resultados  

Especialmente útil para **agricultura, ecología, biotecnología y análisis experimental**.

---

# 🧠 ¿Qué es el PCA?

El **Análisis de Componentes Principales (PCA)** es una técnica estadística de **reducción de dimensionalidad** que transforma un conjunto de variables correlacionadas en un nuevo conjunto de variables no correlacionadas llamadas:

### 👉 Componentes principales (PCs)

Cada componente:

- es combinación lineal de las variables originales
- explica la máxima varianza posible
- es ortogonal a los demás

---

# 🎯 Objetivos del PCA

- Reducir número de variables
- Detectar patrones
- Eliminar colinealidad
- Visualizar datos multivariados
- Identificar variables más influyentes

---

# 📐 Fundamento matemático

Sea una matriz de datos estandarizados:

\[
X_{n \times p}
\]

## 1️⃣ Matriz de correlación/covarianza
\[
R = \frac{1}{n-1} X^T X
\]

## 2️⃣ Descomposición espectral
\[
R v = \lambda v
\]

donde:

- \( \lambda \) = autovalores (varianza explicada)
- \( v \) = autovectores (direcciones principales)

## 3️⃣ Componentes principales
\[
Z = X V
\]

---

# ⚠️ Supuestos y consideraciones

Para aplicar PCA correctamente:

✅ Variables numéricas o codificadas  
✅ Relaciones lineales  
✅ Escalas comparables (estandarizar)  
✅ Tamaño de muestra suficiente  
✅ Correlación entre variables  

### Recomendaciones
- usar matriz de correlación si escalas distintas
- revisar outliers
- interpretar solo componentes con varianza relevante

---

# 📊 ¿Cómo interpretar los resultados?

## Scree Plot
- muestra varianza por componente
- buscar “codo”
- regla de Kaiser: autovalor > 1

## Varianza acumulada
- elegir número de PCs para explicar 80–90%

## Biplot
- puntos = observaciones
- flechas = variables
- ángulo pequeño → alta correlación
- direcciones opuestas → correlación negativa

## Cargas factoriales (loadings)
- |valor| alto → mayor contribución
- indica qué variables forman cada componente

## Scatter PC1 vs PC2
- agrupa muestras similares
- detecta clusters o outliers

---

# 🧰 Librerías utilizadas

| Librería | Uso |
|---------|------|
| pandas | manejo de datos |
| numpy | álgebra lineal |
| matplotlib | gráficos |
| seaborn | heatmaps |
| scikit-learn | estandarización y codificación |
| openpyxl | exportar Excel |

---

# Instrucciones 
 
## Asegúrese de tener Python 3.8 o superior instalado.

Puede verificarlo ejecutando en la terminal o consola:
python --version
python3 --version

## Descargar el repositorio

Desde GitHub:

git clone https://github.com/Madrid9191/pca-analysis-tool.git
cd pca-analysis-tool


O descargue el repositorio como archivo .zip y descomprímalo.

## Instalar dependencias

Instalar dependencias

pip install -r requirements.txt

Esto instalará automáticamente todas las librerías necesarias.

## Preparar los datos

El archivo de datos debe cumplir las siguientes condiciones:

Formato CSV (.csv) o Excel (.xlsx / .xls)

## Ejecutar el programa

Desde la carpeta raíz del proyecto, ejecute:

python src/PCA.py

Se iniciará un menú interactivo en la consola.

## Paso 1 — Cargar archivo

Ingrese:

datos.xlsx

## Paso 2 — Variables ordinales (opcional)

Ejemplo:

Calidad, Nivel


Si no hay → presione Enter.

## Paso 3 — Variables nominales (opcional)

Ejemplo:

Tratamiento, Region


Se aplica automáticamente One-Hot Encoding.

## Paso 4 — Estandarización

El programa transforma automáticamente:

media = 0

desviación estándar = 1

## Paso 5 — Cálculo del PCA

Se obtienen:

Componentes principales

Autovalores

Varianza explicada

Cargas factoriales

Datos transformados

## Paso 6 — Gráficos generados

Incluye:

📊 Scree Plot

📈 Varianza acumulada

🔵 Scatter PC1 vs PC2

🧭 Biplot

🔥 Heatmap de cargas

📌 Contribución de variables

## Cerrar el programa

El análisis finaliza automáticamente al terminar el flujo.

Para interrumpir el proceso en cualquier momento:

Ctrl + C
