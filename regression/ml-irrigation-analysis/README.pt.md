# Análise de Regressão Linear - Irrigação

🌐 [Read in English](README.md)

Projeto de regressão linear para modelar a relação entre horas de irrigação e área irrigada por ângulo, utilizando um dataset sintético de irrigação.

## Objetivo

Prever `irrigated_area_per_angle` (área irrigada por ângulo) com base em `irrigation_hours` (horas de irrigação) utilizando um modelo de regressão linear simples.

## Etapas

1. Carregar os dados de irrigação a partir de um arquivo CSV
2. Visualizar os dados para entender a estrutura e as variáveis disponíveis
3. Calcular as estatísticas descritivas das variáveis
4. Criar gráficos de dispersão para visualizar a relação entre horas de irrigação e área irrigada por ângulo
5. Analisar a correlação entre as variáveis
6. Dividir os dados em conjuntos de treino e teste
7. Treinar um modelo de regressão linear utilizando horas de irrigação como variável independente (X) e área irrigada por ângulo como variável dependente (Y)
8. Imprimir a equação da reta obtida pelo modelo
9. Utilizar as métricas de desempenho (MSE, MAE) para avaliar a precisão do modelo
10. Visualizar os resultados reais e preditos em um gráfico
11. Calcular e analisar os resíduos do modelo
12. Verificar a normalidade dos resíduos utilizando testes estatísticos e gráficos
13. Utilizar o modelo para fazer predições (exemplo: prever área irrigada por ângulo para 15 horas de irrigação)

## Dataset

O dataset contém três colunas: `irrigation_hours`, `irrigated_area` e `irrigated_area_per_angle`. Durante a análise exploratória, percebeu-se que `irrigation_hours` e `irrigated_area` apresentavam correlação muito alta com `irrigated_area_per_angle` (correlação ≈ 1.0). Para evitar multicolinearidade e manter o escopo proposto pelo desafio, apenas `irrigation_hours` foi utilizada como feature do modelo; `irrigated_area` foi excluída do modelo e usada apenas na análise exploratória.

## Análise Exploratória

- O gráfico de dispersão entre `irrigation_hours` e `irrigated_area_per_angle` mostrou uma relação linear quase perfeita, sem outliers visíveis.
- O heatmap de correlação (Pearson) mostrou valores próximos de 1.0 entre todas as variáveis, confirmando a natureza linear e proporcional dos dados.
- As estatísticas descritivas (`describe()`) mostraram um crescimento proporcional constante: cada hora adicional de irrigação correspondia a um aumento fixo na área irrigada.

## Resultados do Modelo

| Métrica | Valor |
|---|---|
| Coeficiente (`coef_`) | ≈ 66.666 |
| MAE | 0.00 |
| MSE | 0.00 |
| R² | 1.00 |

O modelo obteve um ajuste perfeito, confirmando a relação quase determinística já observada na análise exploratória: cada hora adicional de irrigação aumenta a área irrigada por ângulo em aproximadamente 66.666 unidades.

## Análise dos Resíduos

Os resíduos ficaram na ordem de 1e-12, o que na prática significa que são zero. Esses valores quase nulos são atribuíveis a limitações de precisão de ponto flutuante, e não a erro real do modelo.

Os testes de normalidade (Q-Q plot e Shapiro-Wilk) não foram totalmente conclusivos nesse caso, já que os resíduos não possuem variabilidade real — o teste de Shapiro-Wilk retornou um p-valor bem abaixo de 0.05, mas isso reflete o padrão de "degraus" causado pelo arredondamento de ponto flutuante, e não um real desvio de normalidade. Esse comportamento é esperado dado o caráter determinístico do dataset.

## Exemplo de Predição

Para 15 horas de irrigação, o modelo previu uma área irrigada por ângulo de 1000.00.

## Conclusão

O dataset utilizado neste projeto é sintético e segue uma fórmula linear exata, o que explica o desempenho perfeito do modelo (R² = 1.00, erro zero). Em cenários do mundo real, métricas tão perfeitas normalmente levantariam suspeita de overfitting ou data leakage. Aqui, porém, esse resultado é coerente com o processo determinístico de geração dos dados, e não com uma falha na modelagem. O projeto aplicou corretamente o pipeline completo de machine learning (EDA, split treino/teste, treinamento, avaliação e análise de resíduos), demonstrando consciência sobre quando resultados "perfeitos" devem ser interpretados com senso crítico, em vez de aceitos sem questionamento.

## Tecnologias

- Python
- pandas
- seaborn / matplotlib
- scikit-learn
- scipy
