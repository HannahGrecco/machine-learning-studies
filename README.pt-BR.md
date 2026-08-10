# Classificação de Diabetes com Gaussian Naive Bayes

🇺🇸 Read in English: [README.md](README.md)

## Visão Geral

Este projeto aplica um classificador **Gaussian Naive Bayes (GaussianNB)** para prever diabetes usando duas variáveis numéricas:

- `glucose_level`
- `blood_pressure`

O dataset foi dividido em conjuntos de treino e teste usando **train_test_split** do scikit-learn.

## Análise Exploratória de Dados (EDA)

- A variável alvo (`diabetes`) está **bem balanceada**, verificado com `value_counts()` visualizado em Plotly (`px.bar`).
- O **nível de glicose** apresenta uma distribuição aproximadamente **normal**.
- A **pressão arterial** não segue uma distribuição normal e apresenta **duas regiões principais de concentração (comportamento bimodal)**.

## Modelo

- **Algoritmo:** Gaussian Naive Bayes (`GaussianNB`)
- **Divisão Treino/Teste:** `train_test_split`
- **Métrica de Avaliação:** **Recall**
- **Avaliação Adicional:** **Matriz de Confusão**

O Recall foi escolhido porque, em um problema de classificação médica, identificar corretamente os casos positivos de diabetes é mais importante do que maximizar a acurácia geral.

## Resultados

O modelo obteve um desempenho sólido:

- **Verdadeiros Negativos:** 86
- **Falsos Positivos:** 7
- **Falsos Negativos:** 7
- **Verdadeiros Positivos:** 99

Esses resultados indicam que o modelo foi eficaz em identificar pacientes diabéticos, mantendo um bom equilíbrio entre previsões positivas e negativas.

## Tecnologias

- Python
- Pandas
- Plotly
- Scikit-learn
- Matplotlib