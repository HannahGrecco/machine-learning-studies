# Irrigation Linear Regression Analysis

🌐 [Leia em Português](README.pt.md)

A linear regression project to model the relationship between irrigation hours and irrigated area per angle, using a synthetic irrigation dataset.

## Objective

Predict `irrigated_area_per_angle` based on `irrigation_hours` using a simple linear regression model.

## Steps

1. Load the irrigation data from a CSV file
2. Visualize the data to understand the structure and available variables
3. Calculate descriptive statistics of the variables
4. Create scatter plots to visualize the relationship between irrigation hours and irrigated area per angle
5. Analyze the correlation between the variables
6. Split the data into training and test sets
7. Train a linear regression model using irrigation hours as the independent variable (X) and irrigated area per angle as the dependent variable (Y)
8. Print the equation of the line obtained by the model
9. Use performance metrics (MSE, MAE) to evaluate the model's accuracy
10. Visualize the actual vs predicted results in a chart
11. Calculate and analyze the model's residuals
12. Check the normality of the residuals using statistical tests and plots
13. Use the model to make predictions (example: predict irrigated area per angle for 15 hours of irrigation)

## Dataset

The dataset contains three columns: `irrigation_hours`, `irrigated_area`, and `irrigated_area_per_angle`. During exploratory data analysis, `irrigation_hours` and `irrigated_area` were found to be highly correlated with `irrigated_area_per_angle` (correlation ≈ 1.0). To avoid multicollinearity and stay aligned with the challenge's scope, only `irrigation_hours` was used as the model's feature; `irrigated_area` was excluded from the model and used only for exploratory analysis.

## Exploratory Analysis

- The scatter plot between `irrigation_hours` and `irrigated_area_per_angle` showed a near-perfect linear relationship, with no visible outliers.
- The correlation heatmap (Pearson) showed correlation values close to 1.0 across all variables, confirming the linear and proportional nature of the data.
- Descriptive statistics (`describe()`) showed a consistent proportional growth: each additional irrigation hour corresponded to a fixed increase in irrigated area.

## Model Results

| Metric | Value |
|---|---|
| Coefficient (`coef_`) | ≈ 66.666 |
| MAE | 0.00 |
| MSE | 0.00 |
| R² | 1.00 |

The model achieved a perfect fit, confirming the near-deterministic relationship already observed during exploratory analysis: each additional irrigation hour increases the irrigated area per angle by approximately 66.666 units.

## Residual Analysis

Residuals were on the order of 1e-12, which in practice means they are zero. These near-zero values are attributable to floating-point precision limitations rather than actual model error.

The normality tests (Q-Q plot and Shapiro-Wilk) were not fully conclusive in this case, as residuals lack real variability — the Shapiro-Wilk test returned a p-value far below 0.05, but this reflects the floating-point "banding" pattern rather than a true deviation from normality. This is expected behavior given the deterministic nature of the dataset.

## Prediction Example

For 15 hours of irrigation, the model predicted an irrigated area per angle of 1000.00.

## Conclusion

The dataset used in this project is synthetic and follows an exact linear formula, which explains the perfect model performance (R² = 1.00, zero error). In real-world scenarios, such perfect metrics would typically raise concerns about overfitting or data leakage. Here, however, this outcome is consistent with the data's deterministic generation process, not with a flaw in the modeling approach. The project correctly applied the full machine learning pipeline (EDA, train/test split, training, evaluation, and residual analysis), and demonstrated awareness of when "perfect" results should be interpreted critically rather than taken at face value.

## Tech Stack

- Python
- pandas
- seaborn / matplotlib
- scikit-learn
- scipy
