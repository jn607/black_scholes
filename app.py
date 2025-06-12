import streamlit as st
from black_scholes.model import black_scholes
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Page config ---
st.set_page_config(
    page_title="Black-Scholes Options Calculator",
    page_icon=":chart_with_upwards_trend:",
    layout="centered"
)

# --- Custom CSS for modern, animated look ---
st.markdown("""
    <style>
    /* Remove Streamlit default padding and header */
    .block-container {
        padding-top: 1.5rem !important;
    }
    header {visibility: hidden;}
    /* Animated gradient background */
    body {
        background: linear-gradient(-45deg, #e0e7ef, #bbf7d0, #fecaca, #fca5a5, #bbf7d0);
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
        margin-top: 1.5rem;
        border: 1.5px solid rgba(255,255,255,0.25);
        transition: box-shadow 0.3s;
    }
    .main:hover {
        box-shadow: 0 12px 40px 0 rgba(31,38,135,0.22);
    }
    /* Animated green-red gradient title */
    .gradient-title {
        font-size: 2.7em;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #22c55e, #ef4444);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 4s linear infinite;
        letter-spacing: 0.03em;
        margin-bottom: 0.1em;
        margin-top: 0.2em;
    }
    @keyframes shine {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    /* Beveled, shiny, animated main button */
    .stButton>button {
        background: linear-gradient(90deg, #22c55e 0%, #ef4444 100%);
        color: white;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.1em;
        padding: 0.7em 2.5em;
        border: none;
        box-shadow: 0 2px 8px rgba(34,197,94,0.15);
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
        box-shadow: 0 6px 24px rgba(34,197,94,0.25);
        transform: translateY(-2px) scale(1.04);
        filter: brightness(1.08);
    }
    .stButton>button:hover:after {
        width: 120%;
    }
    /* Animated input fields */
    .stNumberInput>div>input {
        border-radius: 8px !important;
        border: 1.5px solid #bbf7d0 !important;
        transition: border 0.2s, box-shadow 0.2s;
    }
    .stNumberInput>div>input:focus {
        border: 1.5px solid #22c55e !important;
        box-shadow: 0 0 0 2px #22c55e;
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
            d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))
            d2 = d1 - sigma * math.sqrt(t)
            N_d1 = norm.cdf(d1)
            N_d2 = norm.cdf(d2)

            st.markdown("""
                <div class='result-card'>
                    <h3 style='text-align:center; color:#059669; margin-bottom:1em;'>Results</h3>
                    <div style='display:flex; justify-content:space-around;'>
                        <div>
                            <div style='color:#64748b; font-size:1.1em;'>Call Option Price</div>
                            <div style='font-size:2.1em; font-weight:700; color:#22c55e;'>${:.2f}</div>
                        </div>
                        <div>
                            <div style='color:#64748b; font-size:1.1em;'>Put Option Price</div>
                            <div style='font-size:2.1em; font-weight:700; color:#ef4444;'>${:.2f}</div>
                        </div>
                    </div>
                    <div style='margin-top:1em; text-align:center; color:#64748b; font-size:1em;'>
                        <em>These prices are theoretical values based on the Black-Scholes model assumptions.</em>
                    </div>
                </div>
            """.format(call, put), unsafe_allow_html=True)

            with st.expander("Show calculation steps and explanation"):
                st.markdown("#### Black-Scholes Formula")
                st.latex(r"""
                    \begin{align*}
                    d_1 &= \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)t}{\sigma\sqrt{t}} \\
                    d_2 &= d_1 - \sigma\sqrt{t} \\
                    C &= S N(d_1) - K e^{-rt} N(d_2) \\
                    P &= K e^{-rt} N(-d_2) - S N(-d_1)
                    \end{align*}
                """)
                st.markdown("#### Your Inputs")
                st.write(f"Spot Price (S): {S}")
                st.write(f"Strike Price (K): {K}")
                st.write(f"Time to Expiry (t): {t}")
                st.write(f"Risk-Free Rate (r): {r}")
                st.write(f"Volatility (σ): {sigma}")

                st.markdown("#### Step-by-Step Calculation")
                st.latex(fr"d_1 = \frac{{\ln({S}/{K}) + ({r} + 0.5 \times {sigma}^2) \times {t}}}{{{sigma} \times \sqrt{{{t}}}}} = {d1:.4f}")
                st.latex(fr"d_2 = {d1:.4f} - {sigma} \times \sqrt{{{t}}} = {d2:.4f}")
                st.latex(fr"C = {S} \times N({d1:.4f}) - {K} \times e^{{-{r} \times {t}}} \times N({d2:.4f}) = {call:.2f}")
                st.latex(fr"P = {K} \times e^{{-{r} \times {t}}} \times N(-{d2:.4f}) - {S} \times N(-{d1:.4f}) = {put:.2f}")

                st.info("N(x) is the cumulative distribution function (CDF) of the standard normal distribution.")

                # --- Graphical Explanation ---
                st.markdown("#### Visualizing d₁ and d₂ on the Standard Normal Distribution")
                x = np.linspace(-4, 4, 500)
                y = norm.pdf(x)
                fig, ax = plt.subplots(figsize=(7, 3.5))
                ax.plot(x, y, color="#6366f1", lw=2, label="Standard Normal PDF")
                ax.fill_between(x, 0, y, where=(x <= d1), color="#22c55e", alpha=0.3, label=f"Area ≤ d₁ ({d1:.2f})")
                ax.fill_between(x, 0, y, where=(x <= d2), color="#ef4444", alpha=0.3, label=f"Area ≤ d₂ ({d2:.2f})")
                ax.axvline(d1, color="#22c55e", linestyle="--", lw=2, label=f"d₁ = {d1:.2f}")
                ax.axvline(d2, color="#ef4444", linestyle="--", lw=2, label=f"d₂ = {d2:.2f}")
                ax.set_title("Standard Normal Distribution with d₁ and d₂")
                ax.set_xlabel("x")
                ax.set_ylabel("Probability Density")
                ax.legend(loc="upper left")
                st.pyplot(fig)

                st.markdown(f"""
                - The **green area** under the curve up to d₁ ({d1:.2f}) represents N(d₁) = {N_d1:.4f}
                - The **red area** under the curve up to d₂ ({d2:.2f}) represents N(d₂) = {N_d2:.4f}
                - These values are used in the Black-Scholes formula to calculate the option prices.
                """)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class='footer'>
        &copy; 2024 Joshua Nolan &mdash; Black-Scholes Model App<br>
        <span style='font-size:0.95em;'>Made with <span style='color:#ef4444;'>&#10084;&#65039;</span> and Streamlit</span>
    </div>
""", unsafe_allow_html=True) 