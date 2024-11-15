# -*- coding: utf-8 -*-
"""Tree_TCC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iIAa39nwzglQoYuwpEg0wIx0I4pKq9Gb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

dataset= pd.read_csv('/content/drive/MyDrive/dataset/dataset_A_Z_alfabeto.csv').astype('float32')
dataset.rename(columns={'0':'label'}, inplace=True)

X = dataset.drop('label',axis = 1)
y = dataset['label']

alfabeto_data = np.reshape(X.values, (X.shape[0], 28, 28))

# @title Texto de título padrão
from sklearn.model_selection import train_test_split
from sklearn import tree, metrics

# Achatamento de dados
data = alfabeto_data.reshape((alfabeto_data.shape[0], -1))

# Primeira divisão: 80% para treino, 20% restante
X_train, X_resto, y_train, y_resto = train_test_split(data, y, test_size=0.2, random_state=42)

# Segunda divisão: 50% do restante para validação e 50% para teste (25% para cada)
X_validacao, X_test, y_validacao, y_test = train_test_split(X_resto, y_resto, test_size=0.25, random_state=13)

# Criar um classificador Decision Tree
clf = tree.DecisionTreeClassifier(random_state=42)

# Treinar o classificador Decision Tree no conjunto de treino
clf.fit(X_train, y_train)

# Prever os valores no conjunto de teste
predicted = clf.predict(X_test)

# Exibir algumas predições para conferir
print(predicted[:10])

# Calcular a acurácia
accuracy = metrics.accuracy_score(y_test, predicted)
print("Acurácia:", accuracy)

# Calcular a matriz de confusão
confusion_matrix = metrics.confusion_matrix(y_test, predicted)
print("Matriz de Confusão:")
print(confusion_matrix)

# Calcular as métricas de classificação
classification_report = metrics.classification_report(y_test, predicted)
print("Relatório de Classificação:")
print(classification_report)

# Avaliar o modelo no conjunto de teste
clf_score = clf.score(X_test, y_test)
print("Score no conjunto de teste:", clf_score)

# Você também pode avaliar no conjunto de validação
validation_accuracy = clf.score(X_validacao, y_validacao)
print("Acurácia no conjunto de validação:", validation_accuracy)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()


import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, clf.predict(X_test))

# Cria um DataFrame para a matriz de confusão
df_cm = pd.DataFrame(cm, range(26), range(26))

# Plot da matriz de confusão usando seaborn
plt.figure(figsize=(20, 15))
sns.set(font_scale=1.4)  # Para o tamanho da fonte dos rótulos
sns.heatmap(df_cm, annot=True, annot_kws={"size": 16})  # Tamanho da fonte dos números na matriz
plt.show()