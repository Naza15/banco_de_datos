# 📊 Plan de Trabajo:
## Banco de Datos SYN Flood + IA para Detectar Ataques

---

## 🎯 OBJETIVO FINAL

**Semana 12:** Sistema funcionando que:
- ✅ Entiende cómo se genera un ataque SYN flood
- ✅ Tiene dataset validado de SYN flood (10k-50k filas)
- ✅ Modelo ML entrenado con accuracy ≥ 90%
- ✅ Código reproducible y documentado

---

## 🔧 STACK A USAR (Proyectos GitHub)

| Proyecto | Función | Por qué |
|----------|---------|--------|
| **chiragbiradar** | Dataset base + features | 2.6M filas listas, 22 features estándar |
| **hackinsdn/secflood** | Entender generación SYN | Script puro, paramétrico, simple |
| **DipankarSaha94** | Entrenar 5 algoritmos ML | 7 algoritmos, código ready-to-use |
| **martimy/sdn_lab** | Infraestructura (opcional) | Si generas datos propios |

---

## 📅 TIMELINE DETALLADO

### SEMANA 1 SETUP & APRENDIZAJE
**Objetivo 1:** Entender el flujo completo (datos → features → ML)

#### Semana 1: Setup Técnico + Proyecto chiragbiradar

**Tareas:**
1. **Clonar y explorar proyectos** (4 horas)
   ```bash
   git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation
   git clone https://github.com/DipankarSaha94/Automated_DDoS_Attack_Detection_in_SDN
   git clone https://github.com/hackinsdn/secflood
   ```

2. **Instalar dependencias Python** (2 horas)
   ```bash
   pip3 install pandas numpy scikit-learn matplotlib jupyter scapy
   ```

3. **Descargar dataset chiragbiradar** (2-4 horas depende conexión)
   - Dataset: 2.6M filas, ~500MB
   - Guardar en: `data/raw/chiragbiradar_dataset.csv`

4. **Leer documentación chiragbiradar** (3 horas)
   - README.md completo
   - Feature specification (22 features explicadas)
   - Ataques definidos (SYN, UDP, ICMP)

**Deliverable:** Proyecto clonado, dataset descargado, entendimiento básico ✅

#############################################################################################################################3

**Objetivo 2:** Análisis Exploratorio del Dataset
1. **Crear Jupyter notebook: `01_exploratory_analysis.ipynb`** (6 horas)
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Cargar dataset
   df = pd.read_csv('data/raw/chiragbiradar_dataset.csv')
   
   # Exploración básica
   print(df.shape)  # (2,600,000, 22)
   print(df.columns)  # 22 features
   print(df['Label'].value_counts())  # Benign vs Attack
   
   # Visualizaciones
   df['Label'].value_counts().plot(kind='bar')
   plt.title('Distribución Benign vs Attack')
   
   # Estadísticas por tipo de ataque
   print(df.groupby('Label').describe())
   ```

2. **Filtrar solo SYN flood** (3 horas)
   ```python
   # De chiragbiradar, extraer solo datos SYN
   # (Revisar cómo está etiquetado en dataset)
   syn_data = df[df['Attack_Type'] == 'SYN']  # o similar
   print(f"SYN flood rows: {len(syn_data)}")  # ~500k-1M rows
   
   # Guardar
   syn_data.to_csv('data/processed/syn_flood_only.csv', index=False)
   ```

3. **Analizar distribución de features** (3 horas)
   ```python
   # Heatmap de correlación
   import seaborn as sns
   sns.heatmap(syn_data.corr(), annot=False)
   
   # Distribuciones por feature
   for col in syn_data.columns[:5]:
       syn_data[col].hist()
       plt.title(f'{col} distribution')
   ```

**Deliverable:** Notebook completo con análisis + datos SYN filtrados ✅

##############################################################################################################

## 📋 CHECKLIST A PARA LA REUNION

### OBJETIVO 1
- [ ] Proyectos clonados
- [ ] Dataset descargado (500MB)
- [ ] Dependencias Python instaladas
- [ ] README chiragbiradar leído

### OBJETIVO 2
- [ ] Exploratory analysis notebook completo
- [ ] Dataset entendido (shape, features, labels)
- [ ] SYN flood filtrado y guardado

########################################################################################################################

## 📚 REPOSITORIOS CLAVE

| Proyecto | URL | Uso |
|----------|-----|-----|
| chiragbiradar | github.com/chiragbiradar/DDoS-Attack-Detection | Dataset base |
| DipankarSaha94 | github.com/DipankarSaha94/Automated_DDoS | ML framework |
| hackinsdn/secflood | github.com/hackinsdn/secflood | Entender SYN flood |

---

## 💡 NOTAS IMPORTANTES

1. **Dataset:** No generas datos, usas chiragbiradar (mucho más rápido para 3 meses)
2. **Focus:** Solo SYN flood (no UDP/ICMP) por simplicidad
3. **ML:** 5 algoritmos simples, sin Deep Learning
4. **Reproducibilidad:** Todo versionado en Git desde semana 1

