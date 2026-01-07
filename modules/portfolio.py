import numpy as np
import pandas as pd

# Portfolio design
def create_life_portfolio(n_policies=1000, mean_loss=5000, std_loss=2000, seed=42):
    """Simulate life portfolio losses"""
    np.random.seed(seed)
    losses = np.random.normal(mean_loss, std_loss, n_policies)
    return pd.Series(losses)

def create_health_portfolio(n_policies=1000, mean_loss=4000, std_loss=1500, seed=42):
    """Simulate health portfolio losses"""
    np.random.seed(seed)
    losses = np.random.normal(mean_loss, std_loss, n_policies)
    return pd.Series(losses)

# Generic function to simulate portfolio
def simulate_portfolio(portfolio_type="Life", n_policies=1000, mean_loss=5000, std_loss=2000):
    if portfolio_type == "Life":
        return create_life_portfolio(n_policies, mean_loss, std_loss)
    elif portfolio_type == "Health":
        return create_health_portfolio(n_policies, mean_loss, std_loss)
    else:
        raise ValueError("Unknown portfolio type")
