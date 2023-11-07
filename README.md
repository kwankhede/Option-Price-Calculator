European Option Price Calculator
Introduction
The European Option Price Calculator is a tool for calculating the prices of European call and put options using the Black-Scholes-Merton (BSM) model. It also calculates the Greeks (delta, gamma, vega, theta, and rho) for the specified option.

Usage
To use the calculator, simply enter the following parameters:

Underlying stock price (S): The current price of the underlying stock.
Strike price (K): The price at which the option can be exercised.
Time to maturity (T): The time remaining until the option expires, expressed in years.
Risk-free interest rate (r): The annualized risk-free interest rate.
Volatility (sigma): The annualized volatility of the underlying stock.
Option type The type of option ('call' or 'put').
Once you have entered the parameters, click the "Calculate" button. The calculator will then display the option price and Greeks.




1. **Black-Scholes Formula for Call Option:**

   The Black-Scholes formula for calculating the theoretical price of a European call option is as follows:

   \[
   C = S \cdot e^{-qT} \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
   \]

   - \(C\) is the call option price.
   - \(S\) is the current stock price.
   - \(K\) is the strike price.
   - \(T\) is the time to expiration in years.
   - \(r\) is the risk-free interest rate.
   - \(q\) is the dividend yield.
   - \(N\) is the cumulative distribution function.
   - \(d_1\) and \(d_2\) are calculated as follows:

   \[
   d_1 = \frac{{\ln\left(\frac{S}{K}\right) + \left(r - q + \frac{{\sigma^2}}{2}\right)T}}{{\sigma \sqrt{T}}}
   \]

   \[
   d_2 = d_1 - \sigma \sqrt{T}
   \]

2. **Black-Scholes Formula for Put Option:**

   The Black-Scholes formula for calculating the theoretical price of a European put option is as follows:

   \[
   P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot e^{-qT} \cdot N(-d_1)
   \]

   - \(P\) is the put option price.
   - Other variables are the same as in the call option formula.

You can add these formulas to your README using LaTeX syntax, which allows you to represent mathematical notation in a clear and standardized way in Markdown. For example:

```markdown
The Black-Scholes formula for calculating the theoretical price of a European call option is as follows:

\[
C = S \cdot e^{-qT} \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
\]

The Black-Scholes formula for a European put option is given by:

\[
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot e^{-qT} \cdot N(-d_1)
\]
```


References
Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. The Journal of Political Economy, 81(3), 637-659.
Merton, R. C. (1973). Theory of rational option pricing. The Bell Journal of Economics and Management Science, 4(1), 141-183.
License
This code is licensed under the MIT License. Please see the LICENSE file for more information.
