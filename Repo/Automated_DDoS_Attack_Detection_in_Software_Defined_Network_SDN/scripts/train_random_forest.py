import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# Cargar dataset
df = pd.read_csv("/home/jeison/Escritorio/Banco_de_datos/datasets/dataset_sdn_Automated_DDoS.csv")

print("Columnas originales:")
print(df.columns)

# Eliminar columnas no útiles para ML
columnas_eliminar = ["dt", "src", "dst", "switch", "Pairflow"]
df = df.drop(columns=columnas_eliminar)

print("\nColumnas después de limpieza:")
print(df.columns)
S
# Convertir columna Protocol a numérico
df["Protocol"] = df["Protocol"].astype('category').cat.codes


# Separar variables
X = df.drop("label", axis=1)
y = df["label"]

# Convertir label si es texto
if y.dtype == 'object':
    y = y.astype('category').cat.codes

# Dividir
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluación
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte:")
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(model, "modelo_random_forest.pkl")
print("\nModelo guardado correctamente.")
