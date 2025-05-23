from black_scholes.model import black_scholes

def main():
   print("Black-Scholes REPL. Press Ctrl+C to exit.") 
   while True:
        try:
            S     = float(input("Enter spot price (S): "))
            K     = float(input("Enter strike price (K): "))
            T     = float(input("Enter time to expiration (years): "))
            r     = float(input("Enter risk-free rate (e.g. 0.05): "))
            sigma = float(input("Enter volatility (e.g. 0.2): "))

            call_price, put_price = black_scholes(S, K, T, r, sigma)
            print(f"\nCall Price: {call_price:.4f}")
            print(f"Put  Price: {put_price:.4f}\n")

        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
if __name__ == "__main__":
    main()