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


