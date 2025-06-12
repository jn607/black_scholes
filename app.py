import streamlit as st
from black_scholes.model import black_scholes

# --- Page config ---
st.set_page_config(
    page_title="Black-Scholes Options Calculator",
    page_icon=":chart_with_upwards_trend:",
    layout="centered"
)

# --- Custom CSS for modern look ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
    }
    .main {
        background-color: #fff;
        border-radius: 16px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.07);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-top: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5em 2em;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1e40af 0%, #2563eb 100%);
        color: #fff;
    }
    .metric-label {
        color: #64748b;
        font-size: 1.1em;
        margin-bottom: 0.2em;
    }
    .metric-value {
        font-size: 2.2em;
        font-weight: 700;
        color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Card ---
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; margin-bottom:0.2em;'>Black-Scholes Options Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; margin-bottom:2em;'>A modern tool for pricing European options.<br>Built by <b>Joshua Nolan</b></p>", unsafe_allow_html=True)
    st.divider()

    # --- Input Form ---
    with st.form("input_form"):
        col1, col2 = st.columns(2)
        with col1:
            S = st.number_input("Spot Price (S)", min_value=0.0, value=100.0, step=1.0)
            K = st.number_input("Strike Price (K)", min_value=0.0, value=100.0, step=1.0)
            t = st.number_input("Time to Expiry (years)", min_value=0.01, value=1.0, step=0.01)
        with col2:
            r = st.number_input("Risk-Free Rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01, format="%.2f")
            sigma = st.number_input("Volatility (σ)", min_value=0.0, max_value=1.0, value=0.2, step=0.01, format="%.2f")
        submitted = st.form_submit_button("Calculate Option Prices")

    # --- Results ---
    if submitted:
        try:
            call, put = black_scholes(S, K, t, r, sigma)
            st.divider()
            st.markdown("<h3 style='text-align:center; margin-bottom:1em;'>Results</h3>", unsafe_allow_html=True)
            col3, col4 = st.columns(2)
            with col3:
                st.markdown("<div class='metric-label'>Call Option Price</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='metric-value'>${call:.2f}</div>", unsafe_allow_html=True)
            with col4:
                st.markdown("<div class='metric-label'>Put Option Price</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='metric-value'>${put:.2f}</div>", unsafe_allow_html=True)
            st.info("These prices are theoretical values based on the Black-Scholes model assumptions.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div style='text-align:center; margin-top:2em; color:#94a3b8; font-size:0.95em;'>
        &copy; 2025 Joshua Nolan &mdash; Black-Scholes Model App
    </div>
""", unsafe_allow_html=True) 