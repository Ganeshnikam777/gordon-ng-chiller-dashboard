# gordon-ng-chiller-dashboard

Streamlit dashboard for monitoring chiller health using the Gordon–Ng model.

## Overview

This dashboard uses a linear regression model to analyze chiller performance data and diagnose potential faults. It displays Gordon–Ng model coefficients, health alerts, and a COP (Coefficient of Performance) comparison chart.

## Features

- **Model Coefficients**: Displays intercept and slope coefficients from the Gordon–Ng regression model
- **Fault Detection Alerts**: Warns about low load responsiveness, unexpected evaporator behavior, and condenser fouling
- **COP Chart**: Plots actual vs. predicted COP values
- **Data Export**: Download model results as a CSV file
- **Data Table**: View raw input data and computed COP values

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run gordon_ng_dashboard.py
```

## Requirements

See `requirements.txt` for dependencies.
