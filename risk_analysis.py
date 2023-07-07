import numpy as np

class RiskAnalysisTool:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def calculate_var(self, confidence_level=0.95):
        returns = self.portfolio.calculate_portfolio_returns()
        var = -np.percentile(returns, 100 * (1 - confidence_level))
        return var

    def calculate_cvar(self, confidence_level=0.95):
        returns = self.portfolio.calculate_portfolio_returns()
        var_index = int((1 - confidence_level) * len(returns))
        cvar = -np.mean(np.sort(returns)[:var_index+1])
        return cvar

    def perform_monte_carlo_simulation(self, num_simulations):
        portfolio_values = []
        returns = self.portfolio.calculate_portfolio_returns()
        for _ in range(num_simulations):
            simulated_portfolio_value = 1000000  # Starting portfolio value
            for ret in returns:
                simulated_portfolio_value *= 1 + ret
            portfolio_values.append(simulated_portfolio_value)
        return portfolio_values
