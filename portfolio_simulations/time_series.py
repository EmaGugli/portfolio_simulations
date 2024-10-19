from datetime import datetime
import yfinance as yf

class TimeSeries:
    def __init__(self,
        asset_name: str,
        values: list[float] = None,
        dates: list[datetime] = None
        ):
        self.asset_name = asset_name
        if values is not None and dates is not None:
            if len(values) != len(dates):
                raise ValueError("The length of values and dates must be the same.")
            self.values = values
            self.dates = dates
        elif values is not None or dates is not None:
            raise ValueError("Both values and dates must be passed to the constructor.")
        else:
            try:
                ticker = yf.Ticker(asset_name)
                self.historical_data = ticker.history(period="max")
            except Exception:
                raise ValueError("The ticker passed is not valid. Please pass a valid ticker or values and dates.")

    def get_returns(self) -> list[float]:
        """
        Calculate and return the series of percentage returns.

        :return: A list of percentage returns.
        """
        return [(self.values[i+1] - self.values[i]) / self.values[i] for i in range(len(self.values) - 1)]

    def __repr__(self):
        return f"TimeSeries({self.asset_name}, {len(self.values)} data points)"
