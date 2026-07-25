# Predição de Receita de Vendas

> 🇺🇸 Prefer reading in English? Click here: [README.md](README.md)

## Sobre o projeto

Este projeto foi desenvolvido como parte de um desafio de Machine Learning da Rocketseat.

O objetivo é prever a receita gerada por vendedores utilizando técnicas de Regressão com base nas seguintes variáveis:

- Tempo de experiência
- Número de vendas
- Fator sazonal

O projeto contempla todo o fluxo de desenvolvimento de um modelo de Machine Learning, incluindo:

- Carregamento dos dados
- Análise Exploratória de Dados (EDA)
- Pré-processamento
- Treinamento de um modelo de Regressão Polinomial
- Avaliação utilizando K-Fold Cross Validation
- Disponibilização do modelo com FastAPI
- Interface desenvolvida com Streamlit

---

## Dataset

O conjunto de dados possui **100 registros** e não contém valores nulos.

| Variável | Descrição |
|----------|-----------|
| experience_time | Tempo (em meses) que o vendedor trabalha na empresa. |
| sales_count | Número de vendas realizadas pelo vendedor. |
| seasonal_factor | Fator sazonal variando entre 1 e 10. |
| revenue_brl | Receita total gerada pelo vendedor (variável alvo). |

---

## Análise Exploratória

Durante a EDA foram realizadas análises como:

- Inspeção dos dados
- Verificação de valores nulos
- Estatísticas descritivas
- Histogramas
- Gráficos de dispersão
- Pairplot
- Matriz de correlação

A análise mostrou que as variáveis independentes apresentam uma correlação linear muito fraca com a variável alvo (`revenue_brl`), o que impactou diretamente o desempenho do modelo.

---

## Modelo

Neste projeto foi utilizada diretamente uma **Regressão Polinomial**, sem a criação prévia de um modelo de Regressão Linear como baseline.

O pipeline é composto por:

- StandardScaler
- PolynomialFeatures
- LinearRegression

A avaliação foi realizada utilizando **Validação Cruzada K-Fold (5 folds)**.

Métricas avaliadas:

- RMSE
- R² Score
- Análise dos resíduos
- Teste de normalidade dos resíduos (QQ Plot)

---

## Disponibilização do Modelo

Após o treinamento, o modelo foi disponibilizado utilizando:

- FastAPI
- Streamlit

O Streamlit envia as informações do usuário para a API, que realiza a predição utilizando o modelo treinado e retorna o resultado em tempo real.

---

## Tecnologias

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Pingouin
- Matplotlib
- Seaborn

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/HannahGrecco/sales-revenue-prediction.git
```

### 2. Instale as dependências

Utilizando Pipenv:

```bash
pipenv install
```

### 3. Ative o ambiente virtual

```bash
pipenv shell
```

### 4. Execute a API

```bash
uvicorn api_sales_model:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```

### 5. Execute o Streamlit

```bash
streamlit run app_streamlit_sales.py
```

A aplicação abrirá em:

```
http://localhost:8501
```

## Observações

Embora o desafio sugerisse iniciar pela Regressão Linear e, posteriormente, comparar seu desempenho com a Regressão Polinomial, neste projeto foi implementada diretamente a Regressão Polinomial. Para avaliar o impacto do grau do polinômio, foram realizados testes alterando manualmente o parâmetro `degree` e comparando as métricas obtidas para cada configuração.

O projeto foi desenvolvido como parte do desafio de Machine Learning da Rocketseat.
