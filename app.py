import streamlit as st
import numpy as np
from black_scholes.model import black_scholes

# Set page config
st.set_page_config(
    page_title="Black-Scholes Options Calculator",
    page_icon="📈",
    layout="wide"
)

# Title and description
st.title("📈 Black-Scholes Options Calculator")
st.markdown("""
This calculator uses the Black-Scholes model to price European-style options.
Enter the parameters below to calculate the theoretical option prices.
""")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Market Parameters")
    spot_price = st.number_input(
        "Spot Price (S)",
        min_value=0.0,
        value=100.0,
        step=1.0,
        help="Current price of the underlying asset"
    )
    strike_price = st.number_input(
        "Strike Price (K)",
        min_value=0.0,
        value=100.0,
        step=1.0,
        help="Price at which the option can be exercised"
    )
    time_to_expiry = st.number_input(
        "Time to Expiry (t) in years",
        min_value=0.0,
        value=1.0,
        step=0.1,
        help="Time until option expiration in years"
    )

with col2:
    st.subheader("Market Conditions")
    risk_free_rate = st.number_input(
        "Risk-Free Rate (r)",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
        step=0.01,
        format="%.2f",
        help="Annual risk-free interest rate (e.g., 0.05 for 5%)"
    )
    volatility = st.number_input(
        "Volatility (σ)",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.01,
        format="%.2f",
        help="Annual volatility of the underlying asset (e.g., 0.2 for 20%)"
    )

# Calculate button
if st.button("Calculate Option Prices", type="primary"):
    try:
        call_price, put_price = black_scholes(
            S=spot_price,
            K=strike_price,
            t=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )
        
        # Display results in a nice format
        st.success("Calculation Complete!")
        
        col3, col4 = st.columns(2)
        with col3:
            st.metric("Call Option Price", f"${call_price:.2f}")
        with col4:
            st.metric("Put Option Price", f"${put_price:.2f}")
            
        # Add some explanation
        st.info("""
        **Note:** These prices are theoretical values based on the Black-Scholes model assumptions:
        - No dividends
        - European-style options
        - Constant volatility
        - Risk-free rate is constant
        - No transaction costs
        """)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add footer with your name
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built by Joshua Nolan • Black-Scholes Model</p>
    <p style='font-size: 0.8em; color: #666;'>© 2025</p>
</div>
""", unsafe_allow_html=True) 