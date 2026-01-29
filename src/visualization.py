import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from .config import *

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


def plot_time_series(data, title, ylabel, save_path=None):
    """Plota série temporal."""
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Data")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(FIGURES_DIR / save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_volatility_comparison(pre_data, post_data, break_date, title):
    """Compara volatilidade antes e depois de quebra estrutural."""
    fig, ax = plt.subplots()
    ax.plot(pre_data.index, pre_data, label="Pre-Break", alpha=0.7)
    ax.plot(post_data.index, post_data, label="Post-Break", alpha=0.7)
    ax.axvline(break_date, color="red", linestyle="--", label="Structural Break")
    ax.set_title(title)
    ax.set_ylabel("Volatilidade")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(corr_matrix, title, save_path=None):
    """Plota heatmap de correlação."""
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", 
                center=0, ax=ax, cbar_kws={"label": "Correlação"})
    ax.set_title(title)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(FIGURES_DIR / save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_comparative_evolution(data_dict, title, ylabel, save_path=None):
    """Plota evolução comparativa de múltiplas séries."""
    fig = go.Figure()
    
    for name, data in data_dict.items():
        fig.add_trace(go.Scatter(
            x=data.index, 
            y=data.values,
            name=name,
            mode="lines"
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Data",
        yaxis_title=ylabel,
        hovermode="x unified"
    )
    
    if save_path:
        fig.write_html(FIGURES_DIR / save_path)
    
    return fig
