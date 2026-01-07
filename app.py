# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Life & Health Reinsurance Simulator", layout="wide")

st.title("Life & Health Reinsurance Simulator")

# ---------------------------
# Sidebar: Simulation Inputs
# ---------------------------
st.sidebar.header("Simulation Parameters")

portfolio_type = st.sidebar.selectbox(
    "Select portfolio",
    ["Life", "Health", "Combined"]
)

num_policies = st.sidebar.slider("Number of policies", 100, 10000, 1000, step=100)
mean_loss = st.sidebar.slider("Mean loss per policy ($)", 1000, 20000, 5000, step=500)
std_dev = st.sidebar.slider("Std deviation of loss ($)", 500, 10000, 2000, step=100)

num_simulations = st.sidebar.slider("Number of years to simulate", 1, 50, 1)

# ---------------------------
# Helper function: simulate losses
# ---------------------------
def simulate_losses(n_policies, mean, std, n_years=1):
    """Simulate annual losses for a portfolio."""
    losses = np.random.normal(mean, std, size=(n_years, n_policies))
    total_losses_per_year = losses.sum(axis=1)
    return total_losses_per_year

# ---------------------------
# Simulate based on portfolio
# ---------------------------
if portfolio_type == "Life":
    losses = simulate_losses(num_policies, mean_loss, std_dev, num_simulations)
elif portfolio_type == "Health":
    # Example: Health portfolio might have higher mean & lower std
    health_mean = mean_loss * 1.2
    health_std = std_dev * 0.8
    losses = simulate_losses(num_policies, health_mean, health_std, num_simulations)
else:  # Combined portfolio
    # Simple combo of Life + Health
    life_losses = simulate_losses(num_policies, mean_loss, std_dev, num_simulations)
    health_losses = simulate_losses(num_policies, mean_loss*1.2, std_dev*0.8, num_simulations)
    losses = life_losses + health_losses

# Convert to DataFrame
df_losses = pd.DataFrame({"Annual Loss": losses})

# ---------------------------
# Display Summary Metrics
# ---------------------------
st.subheader("Summary Statistics")

mean_val = df_losses["Annual Loss"].mean()
max_val = df_losses["Annual Loss"].max()
std_val = df_losses["Annual Loss"].std()
median_val = df_losses["Annual Loss"].median()
var_995 = np.percentile(df_losses["Annual Loss"], 99.5)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Mean annual loss", f"${mean_val:,.0f}")
col2.metric("Max annual loss", f"${max_val:,.0f}")
col3.metric("Median annual loss", f"${median_val:,.0f}")
col4.metric("99.5% VaR", f"${var_995:,.0f}")

# ---------------------------
# Loss Distribution Plot
# ---------------------------
st.subheader(f"{portfolio_type} Loss Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df_losses["Annual Loss"], bins=30, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Annual Loss ($)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# ---------------------------
# Optional: Download results
# ---------------------------
csv = df_losses.to_csv(index=False)
st.download_button("Download Simulation Results as CSV", csv, "simulation_results.csv")
