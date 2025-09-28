#TODO Add methods to remove assets and modify weights
#TODO Make updating shared time window not destructive
from datetime import datetime
from portfolio_simulations.asset import Asset
import matplotlib.pyplot as plt
import pandas as pd
import random

class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, 
        asset_name: str,
        weight: float,
        values: list[float] = None,
        dates: list[datetime] = None
    ) -> None:
        """
        Add a new asset to the portfolio. If value and dates are not passed, the asset will be fetched from yfinance.
        """
        asset = Asset(asset_name, weight=weight, values=values, dates=dates)
        self.assets.append(asset)
        self._update_shared_time_window()

    def add_start_date(self, start_date: datetime):
        """
        Add the start date to the portfolio.
        """
        self.start_date = start_date
        self._update_shared_time_window()

    def add_end_date(self, end_date: datetime):
        """
        Add the end date to the portfolio.
        """
        self.end_date = end_date
        self._update_shared_time_window()

    def compute_return_distribution(self,
        rolling_window: int = 5,
        num_simulations: int = 1000,
    ):
        date_upper_limit = max(self.combined_window["Date"]-pd.DateOffset(years=rolling_window))
        available_dates = self.combined_window[self.combined_window["Date"] <= date_upper_limit]
        
        for asset in self.assets:
            asset.set_window(self.start_date, self.end_date)

        self.portfolio_returns = []
        for i in range(num_simulations):
            if available_dates.empty:
                raise ValueError("Not enough data to generate return distribution, reduce rolling_window or num_simulations.")
            simulation_start_date = random.choice(available_dates)
            simulation_end_date = simulation_start_date + pd.DateOffset(years=rolling_window)
        
            available_dates = available_dates[available_dates != simulation_start_date]

            self.portfolio_returns.append(self.compute_portfolio_returns(simulation_start_date, simulation_end_date))

    def _update_shared_time_window(self):
        combined_dates = set()
        earliest_date = 0
        latest_date = 0
        for asset in self.assets:
            combined_dates.update(asset.historical_data['Date'])
            earliest_date = min(earliest_date, asset.historical_data['Date'].min())
            latest_date = max(latest_date, asset.historical_data['Date'].max())
        combined_dates = sorted(combined_dates)
        if self.start_date and self.start_date < earliest_date:
            self.start_date = earliest_date
        if self.end_date and self.end_date > latest_date:
            self.end_date = latest_date
        
        self.combined_window = pd.DataFrame({"Date": combined_dates})
    
    def compute_portfolio_returns(self, start_date: datetime, end_date: datetime):
        """
        Compute the return distribution of the portfolio between two dates.
        """
        for asset in self.assets:
            asset.set_window(start_date, end_date)
            asset.returns = asset.get_returns()
        
        portfolio_returns = sum([asset.weight * asset.returns for asset in self.assets])
        return portfolio_returns

    def plot_return_distributions(self):
        """
        Plot the return distributions of the portfolio.
        """
        plt.hist(self.portfolio_returns)
        plt.title("Portfolio Return Distributions")
        plt.xlabel("Returns")
        plt.ylabel("Frequency")
        plt.show()

    def print_portfolio(self):
        """
        Print the portfolio.
        """	
        print(f"Start date: {self.start_date}")
        print(f"End date: {self.end_date}")
        for asset in self.assets:
            print(f"{asset.asset_name}: {asset.weight}")

    def remove_asset(self, asset_name: str):
        """
        Remove an asset from the portfolio.
        """
        self.assets = [asset for asset in self.assets if asset.asset_name != asset_name]
        self._update_shared_time_window()

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.add_asset("VWCE.DE", 0.8)
    portfolio.add_asset("ZPRX.DE", 0.1)
    portfolio.add_asset("ZPRV.DE", 0.1)
    portfolio.compute_return_distribution()
    portfolio.plot_return_distributions()