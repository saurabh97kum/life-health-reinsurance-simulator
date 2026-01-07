import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_loss_distribution(losses, title="Loss Distribution"):
    """Plot histogram with KDE using Streamlit"""
    st.subheader(title)
    fig, ax = plt.subplots()
    sns.histplot(losses, bins=30, kde=True, ax=ax)
    ax.set_xlabel("Loss Amount")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
