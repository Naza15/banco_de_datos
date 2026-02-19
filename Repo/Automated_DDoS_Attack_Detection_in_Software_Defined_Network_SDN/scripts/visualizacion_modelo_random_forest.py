import joblib
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import os

# Ruta del modelo
ruta_modelo = "/home/jeison/Escritorio/Banco_de_datos/Repo/Automated_DDoS_Attack_Detection_in_Software_Defined_Network_SDN/scripts/modelo_random_forest.pkl"

# Verificar que el archivo exista
if not os.path.exists(ruta_modelo):
    print("❌ No se encontró el modelo en la ruta especificada.")
    exit()

# Cargar el modelo
modelo = joblib.load(ruta_modelo)

print("✅ Modelo cargado correctamente")
print("Tipo de modelo:", type(modelo))
print("Número de árboles:", len(modelo.estimators_))

# ==============================
# 1️⃣ Mostrar importancia de características
# ==============================

if hasattr(modelo, "feature_importances_"):
    importancias = modelo.feature_importances_

    plt.figure()
    plt.bar(range(len(importancias)), importancias)
    plt.title("Importancia de las características")
    plt.xlabel("Índice de característica")
    plt.ylabel("Importancia")
    plt.show()

# ==============================
# 2️⃣ Visualizar un árbol del bosque
# ==============================

plt.figure(figsize=(12, 8))
plot_tree(modelo.estimators_[0], filled=True)
plt.title("Visualización de un árbol del Random Forest")
plt.show()
