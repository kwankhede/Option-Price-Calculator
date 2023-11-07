

# European Option Price Calculator

## Introduction

The European Option Price Calculator is a tool for calculating the prices of European call and put options using the Black-Scholes-Merton (BSM) model. It also calculates the Greeks (delta, gamma, vega, theta, and rho) for the specified option.

## Usage

To use the calculator, simply enter the following parameters:

- **Underlying stock price (S):** The current price of the underlying stock.
- **Strike price (K):** The price at which the option can be exercised.
- **Time to maturity (T):** The time remaining until the option expires, expressed in years.
- **Risk-free interest rate (r):** The annualized risk-free interest rate.
- **Volatility (sigma):** The annualized volatility of the underlying stock.
- **Option type:** The type of option ('call' or 'put').

Once you have entered the parameters, click the "Calculate" button. The calculator will then display the option price and Greeks.

## Option Pricing Formulas

### Black-Scholes Formula for Call Option

The Black-Scholes formula for calculating the theoretical price of a European call option is as follows:


C = S * e^(-qT) * N(d1) - K * e^(-rT) * N(d2)
=

- \(C\) is the call option price.
- \(S\) is the current stock price.
- \(K\) is the strike price.
- \(T\) is the time to expiration in years.
- \(r\) is the risk-free interest rate.
- \(q\) is the dividend yield.
- \(N\) is the cumulative distribution function.
- \(d1\) and \(d2\) are calculated as follows:


d1 = (ln(S/K) + (r - q + (sigma^2)/2) * T) / (sigma * sqrt(T))
d2 = d1 - sigma * sqrt(T)


### Black-Scholes Formula for Put Option

The Black-Scholes formula for calculating the theoretical price of a European put option is as follows:


P = K * e^(-rT) * N(-d2) - S * e^(-qT) * N(-d1)


- \(P\) is the put option price.
- Other variables are the same as in the call option formula.

## References

- Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. The Journal of Political Economy, 81(3), 637-659.
- Merton, R. C. (1973). Theory of rational option pricing. The Bell Journal of Economics and Management Science, 4(1), 141-183.

## License

This code is licensed under the MIT License. Please see the LICENSE file for more information.
```
