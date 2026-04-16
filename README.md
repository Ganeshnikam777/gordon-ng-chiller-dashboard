# gordon-ng-chiller-dashboard
Streamlit dashboard for monitoring chiller health using Gordon–Ng model

## Overview

This dashboard uses the Gordon–Ng model to monitor chiller performance and diagnose faults using simulated real-time data.

## Features

- **Gordon–Ng Model Coefficients** – Displays regression coefficients fitted from chiller data
- **Chiller Health Alerts** – Flags potential faults (condenser fouling, refrigerant issues, etc.)
- **COP Prediction Chart** – Compares actual vs. predicted Coefficient of Performance (COP)
- **Input Data Table** – Shows raw input data alongside model results
- **CSV Export** – Download model results as a CSV file

## Setup

```bash
pip install -r requirements.txt
streamlit run gordon_ng_dashboard.py
```

## Requirements

See `requirements.txt` for dependencies.
