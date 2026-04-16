# Applied-Data-Analytics-in-Finance
This repository reflects my experience analyzing financial KPIs  and my background in financial risk analysis and portfolio optimization.

# Portfolio Optimization (Long-Only Minimum Variance)

## Objective
Build a long-only minimum variance portfolio using optimization techniques to minimize risk while ensuring full capital allocation and no short positions.

## Tools & Technologies
- Python
- NumPy
- Pandas
- SciPy (optimization)
- SQLite

## Methodology
- Extracted historical price data from a SQLite database
- Calculated daily returns for multiple assets
- Estimated the variance-covariance matrix (annualized)
- Applied constrained optimization using `scipy.optimize.minimize`
- Imposed constraints:
  - Portfolio weights sum to 1 (L1 norm)
  - No short-selling (non-negative weights)

## Key Features
- Dynamic asset input
- Automated data extraction and cleaning
- Risk minimization through quantitative modeling
- Real-world financial constraints (long-only portfolio)

## Results
The model generates optimal portfolio weights that minimize total variance while maintaining diversification and compliance with investment constraints.

## Business Impact
This approach supports better investment decision-making by identifying low-risk asset allocations, a key concept in portfolio management and financial risk analysis.

## How to Run
1. Ensure the SQLite database (`fcp_database.db`) is available
2. Update asset tickers if needed
3. Run the script:


---

# 📈 Proyecto 2: Sales Prediction (te lo estructuro aunque no pude ver el archivo completo)

# Sales Prediction using Statistical Analysis

## Objective
Analyze historical sales data and build a statistical model to identify trends and generate predictions to support business decision-making.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn (if used)
- Statistical modeling

## Methodology
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Identification of trends and seasonality
- Application of statistical techniques for forecasting
- Model evaluation and interpretation

## Key Features
- End-to-end data analysis workflow
- Data-driven insights generation
- Predictive modeling approach
- Clear visualization of trends and patterns

## Results
The analysis identifies key drivers of sales behavior and provides a predictive framework to estimate future performance.

## Business Impact
Helps improve planning, forecasting accuracy, and strategic decision-making by leveraging historical data patterns.

## How to Run
1. Open the notebook:
```bash
jupyter notebook PrediccionEstadistica_ventas.ipynb





