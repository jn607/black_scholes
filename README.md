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

<img width="440" alt="image" src="https://github.com/user-attachments/assets/70b6bf71-d951-45b7-89da-463ab4f11ea5" />
