import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chiller Health Dashboard", layout="wide")

st.title("🌬️ Gordon–Ng Chiller Monitoring Dashboard")
st.markdown("Track model coefficients and diagnose faults using real-time data.")

# 📥 Simulated chiller data
data = {
    'Q_ev': [520, 530, 540, 550, 560, 570, 580, 590],
    'T_ev_in': [12.0, 11.8, 11.5, 11.2, 11.0, 10.8, 10.5, 10.3],
    'T_con_out': [34.5, 34.8, 35.0, 35.2, 35.5, 35.8, 36.0, 36.2],
    'P_comp': [130, 128, 126, 124, 122, 120, 118, 117]
}
df = pd.DataFrame(data)
df['COP'] = df['Q_ev'] / df['P_comp']

# Fit Gordon–Ng regression
X = df[['Q_ev', 'T_ev_in', 'T_con_out']]
y = df['COP']
model = LinearRegression()
model.fit(X, y)

# Extract coefficients
b0 = model.intercept_
b1, b2, b3 = model.coef_
df['COP_pred'] = model.predict(X)

# 🔍 Display coefficients
st.subheader("🔧 Gordon–Ng Model Coefficients")
st.write(f"**b₀ (Intercept):** {b0:.4f}")
st.write(f"**b₁ (Cooling Load - Q_ev):** {b1:.4f}")
st.write(f"**b₂ (Evaporator Temp - T_ev_in):** {b2:.4f}")
st.write(f"**b₃ (Condenser Temp - T_con_out):** {b3:.4f}")

# 🚨 Fault Detection
st.subheader("🚨 Chiller Health Alerts")
alerts = []
if b1 < 0.01:
    alerts.append("⚠️ Low responsiveness to load changes — check refrigerant or water flow.")
if b2 > 0:
    alerts.append("⚠️ Efficiency improving with higher evaporator inlet temp — unexpected.")
if b3 > 0.02:
    alerts.append("⚠️ Possible condenser fouling or cooling tower inefficiency.")

if alerts:
    for alert in alerts:
        st.warning(alert)
else:
    st.success("✅ Chiller performance looks stable and efficient!")

# 📊 Plot COP comparison
st.subheader("📈 COP: Actual vs Predicted")
fig, ax = plt.subplots()
ax.plot(df['COP'], label='Actual COP', marker='o')
ax.plot(df['COP_pred'], label='Predicted COP', linestyle='--', marker='x')
ax.set_xlabel("Sample Index")
ax.set_ylabel("COP")
ax.set_title("COP Prediction Accuracy")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# 💾 Optional CSV Export
st.download_button(
    label="📥 Download Model Results (CSV)",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="chiller_model_results.csv",
    mime="text/csv"
)
