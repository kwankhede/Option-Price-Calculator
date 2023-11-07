import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import norm
from datetime import datetime, timedelta

N = norm.cdf


def BS_CALL(S, K, T, r, sigma, dividend_yield):
    d1 = (np.log(S / K) + (r - dividend_yield + sigma**2 / 2) * T) / (
        sigma * np.sqrt(T)
    )
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-dividend_yield * T) * N(d1) - K * np.exp(-r * T) * N(d2)


def BS_PUT(S, K, T, r, sigma, dividend_yield):
    d1 = (np.log(S / K) + (r - dividend_yield + sigma**2 / 2) * T) / (
        sigma * np.sqrt(T)
    )
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * N(-d2) - S * np.exp(-dividend_yield * T) * N(-d1)


# Calculate Greeks
def calculate_greeks(S, K, T, r, sigma, dividend_yield, option_type):
    d1 = (np.log(S / K) + (r - dividend_yield + sigma**2 / 2) * T) / (
        sigma * np.sqrt(T)
    )
    d2 = d1 - sigma * np.sqrt(T)

    option_type = option_type.lower()  # Convert option type to lowercase

    if option_type == "call":
        delta = np.exp(-dividend_yield * T) * N(d1)
        gamma = (np.exp(-dividend_yield * T) * N(d1)) / (S * sigma * np.sqrt(T))
        vega = S * np.exp(-dividend_yield * T) * N(d1) * np.sqrt(T) / 100
        theta = (
            -S * sigma * np.exp(-dividend_yield * T) * N(d1) / (2 * np.sqrt(T))
            - r * K * np.exp(-r * T) * N(d2)
        ) / 365
        rho = K * T * np.exp(-r * T) * N(d2) / 100
    elif option_type == "put":
        delta = -np.exp(-dividend_yield * T) * N(-d1)
        gamma = (np.exp(-dividend_yield * T) * N(d1)) / (S * sigma * np.sqrt(T))
        vega = S * np.exp(-dividend_yield * T) * N(d1) * np.sqrt(T) / 100
        theta = (
            -S * sigma * np.exp(-dividend_yield * T) * N(d1) / (2 * np.sqrt(T))
            - r * K * np.exp(-r * T) * N(-d2)
        ) / 365
        rho = -K * T * np.exp(-r * T) * N(-d2) / 100
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    return delta, gamma, vega, theta, rho


# Calculate intrinsic value
def calculate_intrinsic_value(S, K, option_type):
    if option_type == "call":
        intrinsic_value = S - K
    elif option_type == "put":
        intrinsic_value = K - S
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    return intrinsic_value


# Classify option
def classify_option(intrinsic_value):
    if intrinsic_value > 0:
        return "In the Money (ITM)"
    elif intrinsic_value < 0:
        return "Out of the Money (OTM)"
    else:
        return "At the Money (ATM)"


# Streamlit UI
st.title("Europian Option Price Calculator")

# Initialize session state
if "on_first_streamlit_run" not in st.session_state:
    st.session_state.on_first_streamlit_run = True

# Create a sidebar for input parameters
st.sidebar.title("Input Parameters")

S = st.sidebar.slider(
    "Current Stock Price (S)", min_value=0.01, max_value=1000.0, value=100.0, step=0.01
)
K = st.sidebar.slider(
    "Strike Price (K)", min_value=0.01, max_value=1000.0, value=100.0, step=0.01
)
start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 11, 7).date())
expire_date = st.sidebar.date_input(
    "Expire Date", value=(datetime(2023, 11, 27)).date()
)
T = ((expire_date - start_date).days) / 365.0
r = st.sidebar.slider(
    "Risk-Free Interest Rate (%)", min_value=0.01, max_value=100.0, value=5.0, step=0.01
)  # Input as a percentage
sigma = st.sidebar.slider(
    "Volatility (%)", min_value=0.01, max_value=100.0, value=25.0, step=0.01
)  # Input as a percentage
dividend_yield = st.sidebar.slider(
    "Dividend Yield (%)", min_value=0.01, max_value=100.0, value=1.0, step=0.01
)  # Input as a percentage
option_type = st.sidebar.selectbox(
    "Option Type",
    ["Call", "Put"],
    index=0,
    format_func=lambda x: "Call" if x == "Call" else "Put",
).lower()

# Define a default button
calculate_button = st.sidebar.button("Calculate", key="calculate_button")

# Automatically trigger calculation when the app loads
if st.session_state.on_first_streamlit_run:
    st.session_state.on_first_streamlit_run = False
    calculate_button = True

if calculate_button:
    if option_type == "call":
        option_price = BS_CALL(
            S, K, T, r / 100.0, sigma / 100.0, dividend_yield / 100.0
        )
    elif option_type == "put":
        option_price = BS_PUT(S, K, T, r / 100.0, sigma / 100.0, dividend_yield / 100.0)
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    delta, gamma, vega, theta, rho = calculate_greeks(
        S, K, T, r / 100.0, sigma / 100.0, dividend_yield / 100.0, option_type
    )
    intrinsic_value = calculate_intrinsic_value(S, K, option_type)
    option_classification = classify_option(intrinsic_value)

    st.markdown("### Details")

    # Create a table to display the option details
    option_details = {
        "Theoretical Price": f"₹{option_price:.4f}",
        "Intrinsic Value": f"{intrinsic_value:.4f}",
        "Option Classification": option_classification,
    }
    st.table(option_details)

    st.markdown("### Greeks")

    # Create a table to display the Greeks
    greeks = {
        "Delta": f"{delta:.4f}",
        "Gamma": f"{gamma:.4f}",
        "Vega": f"{vega:.4f}",
        "Theta": f"{theta:.4f}",
        "Rho": f"{rho:.4f}",
    }
    st.table(greeks)

    # Create the "Option Price vs. Underlying Price" interactive graph using Plotly
    underlying_prices = np.linspace(0.8 * S, 1.2 * S, 100)
    option_prices = (
        [
            BS_CALL(S, K, T, r / 100.0, sigma / 100.0, dividend_yield / 100.0)
            for S in underlying_prices
        ]
        if option_type == "call"
        else [
            BS_PUT(S, K, T, r / 100.0, sigma / 100.0, dividend_yield / 100.0)
            for S in underlying_prices
        ]
    )

    fig = px.line(
        x=underlying_prices,
        y=option_prices,
        labels={"x": "Underlying Stock Price (S)", "y": "Option Price"},
        title="Option Price vs. Underlying Price",
    )
    st.plotly_chart(fig)
