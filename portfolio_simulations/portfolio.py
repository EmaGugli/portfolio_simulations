from datetime import datetime
from time_series import TimeSeries
from utils import calculate_portfolio_statistics
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, 
        time_series_list: list[TimeSeries],
        start_date: datetime,
        end_date: datetime
        ):
        self.time_series_list = time_series_list
        self.start_date = start_date
        self.end_date = end_date

    def add_time_series(self, time_series: TimeSeries):
        """
        Add a new TimeSeries to the portfolio.

        :param time_series: A TimeSeries object representing a new asset to add.
        """
        self.time_series_list.append(time_series)

    def compute_statistics(self) -> dict:
        """
        Compute portfolio statistics such as mean return, variance, and Sharpe ratio.

        :return: A dictionary containing portfolio statistics.
        """
        return calculate_portfolio_statistics(self.time_series_list)

    def run_simulation(self, num_simulations: int = 1000):
        """
        Simulate portfolio returns using Monte Carlo simulations or other methods.

        :param num_simulations: The number of simulations to run.
        """
        # Placeholder for simulation logic
        simulated_results = []
        for _ in range(num_simulations):
            # Simulate returns and add to the list
            pass
        return simulated_results

    def plot_return_distributions(self):
        """
        Plot the return distributions of the portfolio.

        :return: A matplotlib plot showing the return distributions.
        """
        all_returns = []
        for ts in self.time_series_list:
            all_returns += ts.get_returns()
        
        plt.hist(all_returns, bins=50)
        plt.title("Portfolio Return Distributions")
        plt.xlabel("Returns")
        plt.ylabel("Frequency")
        plt.show()

    def __repr__(self):
        return f"Portfolio({len(self.time_series_list)} assets, from {self.start_date} to {self.end_date})"
