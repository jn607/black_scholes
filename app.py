import streamlit as st
from black_scholes.model import black_scholes

# --- Page config ---
st.set_page_config(
    page_title="Black-Scholes Options Calculator",
    page_icon=":chart_with_upwards_trend:",
    layout="centered"
)

# --- Custom CSS for modern, animated look ---
st.markdown("""
    <style>
    /* Animated gradient background */
    body {
        background: linear-gradient(-45deg, #e0e7ef, #a5b4fc, #f0abfc, #fcd34d, #fca5a5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    /* Glassmorphic card */
    .main {
        background: rgba(255,255,255,0.75);
        border-radius: 24px;
        box-shadow: 0 8px 32px 0 rgba(31,38,135,0.18);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-top: 2.5rem;
        border: 1.5px solid rgba(255,255,255,0.25);
        transition: box-shadow 0.3s;
    }
    .main:hover {
        box-shadow: 0 12px 40px 0 rgba(31,38,135,0.22);
    }
    /* Animated gradient title */
    .gradient-title {
        font-size: 2.7em;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #6366f1, #f472b6, #fbbf24, #34d399);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 4s linear infinite;
        letter-spacing: 0.03em;
        margin-bottom: 0.1em;
    }
    @keyframes shine {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    /* Beveled, shiny, animated button */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #f472b6 100%);
        color: white;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.1em;
        padding: 0.7em 2.5em;
        border: none;
        box-shadow: 0 2px 8px rgba(99,102,241,0.15);
        transition: all 0.2s cubic-bezier(.4,0,.2,1);
        position: relative;
        overflow: hidden;
    }
    .stButton>button:after {
        content: "";
        position: absolute;
        left: 50%;
        top: 0;
        width: 0;
        height: 100%;
        background: rgba(255,255,255,0.25);
        transform: translateX(-50%);
        transition: width 0.3s;
        z-index: 1;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 24px rgba(99,102,241,0.25);
        transform: translateY(-2px) scale(1.04);
    }
    .stButton>button:hover:after {
        width: 120%;
    }
    /* Animated input fields */
    .stNumberInput>div>input {
        border-radius: 8px !important;
        border: 1.5px solid #c7d2fe !important;
        transition: border 0.2s, box-shadow 0.2s;
    }
    .stNumberInput>div>input:focus {
        border: 1.5px solid #6366f1 !important;
        box-shadow: 0 0 0 2px #6366f1;
    }
    /* Results animation */
    .result-card {
        background: rgba(236, 253, 245, 0.85);
        border-radius: 16px;
        padding: 1.2em 1em;
        margin-top: 1.5em;
        box-shadow: 0 2px 12px rgba(16,185,129,0.10);
        animation: fadeIn 1s;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    /* Footer */
    .footer {
        text-align:center;
        margin-top:2.5em;
        color:#64748b;
        font-size:1.05em;
        letter-spacing:0.01em;
        opacity:0.85;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Card ---
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-title'>Black-Scholes Options Calculator</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; margin-bottom:2em; font-size:1.15em;'>A creative, modern tool for pricing European options.<br>Built by <b>Joshua Nolan</b></p>", unsafe_allow_html=True)
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
        submitted = st.form_submit_button("✨ Calculate Option Prices")

    # --- Results ---
    if submitted:
        try:
            call, put = black_scholes(S, K, t, r, sigma)
            st.markdown("""
                <div class='result-card'>
                    <h3 style='text-align:center; color:#059669; margin-bottom:1em;'>Results</h3>
                    <div style='display:flex; justify-content:space-around;'>
                        <div>
                            <div style='color:#64748b; font-size:1.1em;'>Call Option Price</div>
                            <div style='font-size:2.1em; font-weight:700; color:#6366f1;'>${:.2f}</div>
                        </div>
                        <div>
                            <div style='color:#64748b; font-size:1.1em;'>Put Option Price</div>
                            <div style='font-size:2.1em; font-weight:700; color:#f472b6;'>${:.2f}</div>
                        </div>
                    </div>
                    <div style='margin-top:1em; text-align:center; color:#64748b; font-size:1em;'>
                        <em>These prices are theoretical values based on the Black-Scholes model assumptions.</em>
                    </div>
                </div>
            """.format(call, put), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class='footer'>
        &copy; 2024 Joshua Nolan &mdash; Black-Scholes Model App<br>
        <span style='font-size:0.95em;'>Made with <span style='color:#f472b6;'>&#10084;&#65039;</span> and Streamlit</span>
    </div>
""", unsafe_allow_html=True) 