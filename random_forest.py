# -*- coding: utf-8 -*-
"""Random_forest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BCWT10uni3rj0Pz0YamlArEB4jyAbfPm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

dataset= pd.read_csv('/content/drive/MyDrive/dataset/dataset_A_Z_alfabeto.csv').astype('float32')
dataset.rename(columns={'0':'label'}, inplace=True)

X = dataset.drop('label',axis = 1)
y = dataset['label']

alfabeto_data = np.reshape(X.values, (X.shape[0], 28, 28))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# Achatamento dos dados (se for necessário)
data = alfabeto_data.reshape((alfabeto_data.shape[0], -1))

# Dividir os dados: 80% treino e 20% para teste + validação
X_train, X_resto, y_train, y_resto = train_test_split(data, y, test_size=0.2, random_state=42)

# Dividir o restante em 50% para validação e 50% para teste (10% cada do total original)
X_validacao, X_test, y_validacao, y_test = train_test_split(X_resto, y_resto, test_size=0.25, random_state=42)

# Criar o classificador RandomForest
RFC = RandomForestClassifier(n_estimators=150, random_state=42)

# Treinar o classificador no conjunto de treino
RFC.fit(X_train, y_train)

# Fazer predições no conjunto de teste
predicted_test = RFC.predict(X_test)

# Fazer predições no conjunto de validação
predicted_validacao = RFC.predict(X_validacao)

# Avaliação conjunta dos conjuntos de teste e validação

# Concatenar os dados para avaliação conjunta
y_combined = np.concatenate([y_test, y_validacao])
predicted_combined = np.concatenate([predicted_test, predicted_validacao])

# Exibir algumas predições para conferir
print("Primeiras predições combinadas (teste + validação):", predicted_combined[:10])

# Calcular a acurácia combinada
accuracy_combined = metrics.accuracy_score(y_combined, predicted_combined)
print("Acurácia combinada (teste e validação):", accuracy_combined)

# Calcular a matriz de confusão combinada
confusion_matrix_combined = metrics.confusion_matrix(y_combined, predicted_combined)
print("Matriz de Confusão combinada:")
print(confusion_matrix_combined)

# Calcular as métricas de classificação combinadas
classification_report_combined = metrics.classification_report(y_combined, predicted_combined, zero_division=0)
print("Relatório de Classificação combinado (teste e validação):")
print(classification_report_combined)

# Avaliar separadamente os scores de teste e validação
score_test = RFC.score(X_test, y_test)
print("Score no conjunto de teste:", score_test)

score_validacao = RFC.score(X_validacao, y_validacao)
print("Score no conjunto de validação:", score_validacao)

import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, RFC.predict(X_test))

# Cria um DataFrame para a matriz de confusão
df_cm = pd.DataFrame(cm, range(26), range(26))

# Plot da matriz de confusão usando seaborn
plt.figure(figsize=(20, 15))
sns.set(font_scale=1.4)  # Para o tamanho da fonte dos rótulos
sns.heatmap(df_cm, annot=True, annot_kws={"size": 16})  # Tamanho da fonte dos números na matriz
plt.show()