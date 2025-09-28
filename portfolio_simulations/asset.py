from datetime import datetime
import yfinance as yf
import pandas as pd

class Asset:
    def __init__(self,
        asset_name: str,
        weight: float,
        values: list[float] = None,
        dates: list[datetime] = None
    ):
        self.asset_name = asset_name
        self.weight = weight
        if values is not None and dates is not None:
            if len(values) != len(dates):
                raise ValueError("The length of values and dates must be the same.")
            self.historical_data = pd.DataFrame({"Date": dates, "Close": values})
        elif values is not None or dates is not None:
            raise ValueError("Both values and dates must be passed to the constructor. Or you can pass both as None and the asset will be fetched from yfinance.")
        else:
            ticker = yf.Ticker(asset_name)
            self.historical_data = ticker.history(period="max")
            if self.historical_data.empty:
                raise ValueError("The ticker passed is not valid. Please pass a valid ticker or a custom name and its values and dates.")
        
        self.historical_data = self.historical_data.fillna(self.historical_data.mean())

    def set_window(self,
        start_date: datetime,
        end_date: datetime
    ) -> pd.DataFrame:
        """
        Get the window of values as a subset of historical_data
        """
        if (self.historical_data['Date'].min() - start_date).days > 0:
            raise ValueError(f"The earliest date of the asset {self.asset_name} is {self.historical_data['Date'].min()}. Please insert a start date after that.")
        if (end_date - self.historical_data['Date'].max()).days > 0:
            raise ValueError(f"The latest date of the asset {self.asset_name} is {self.historical_data['Date'].max()}. Please insert an end date before that.")
        
        self.historical_data = self.historical_data[(self.historical_data['Date'] >= start_date) & (self.historical_data['Date'] <= end_date)].reset_index(drop=True)

    def get_returns(self):
        """
        Compute annualized return of the asset between two dates.
        """
        time_series = self.historical_data.sort_values('Date')

        initial_price = time_series['Close'].iloc[0]
        final_price = time_series['Close'].iloc[-1]

        years = (time_series['Date'].iloc[-1] - time_series['Date'].iloc[0]).days / 365.25

        annualized_return = (final_price / initial_price) ** (1 / years) - 1

        return annualized_return
