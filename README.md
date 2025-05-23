This repo includes a Python REPL application that calculates call and put options for given input values using the Black-Scholes Model

# Black-Scholes (or Black-Scholes-Merton) Model
It is a differential equation developed in 1973 used to calculate the theoretical value of European-style options contracts.

It posits that instruments will have a lognormal distribution of prices (asset prices can't be negative) following a random walk with constant drift and volatility.

**Assumptions**
- No dividends are paid out during option lifetime
- Markets are random
- No transaction costs to buy the option
- Risk-free rate and volatility of the underlying asset are constant
- Returns of the underlying asset are normally distributed
- The option is European and can only be exercised at expiration

**Black-Scholes Model Formula**

<img width="428" alt="image" src="https://github.com/user-attachments/assets/48d1cb3b-b6b6-435b-bf2f-f20fe41f1271" />

C	=	call option price
N	=	CDF of the normal distribution
S_t	=	spot price of an asset
K	=	strike price
r	=	risk-free interest rate
t	=	time to maturity
\sigma	=	volatility of the asset
