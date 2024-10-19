from datetime import datetime

class TimeSeries:
    def __init__(self, asset_name: str, values: list[float], time: list[datetime]):
        """
        Initialize the TimeSeries object.

        :param asset_name: The name of the asset (e.g., ticker symbol).
        :param values: A list of float values representing the asset's value at each time point.
        :param time: A list of datetime objects representing the time for each value.
        """
        if len(values) != len(time):
            raise ValueError("The length of values and time must be the same.")
        
        self.asset_name = asset_name
        self.values = values
        self.time = time

    def get_returns(self) -> list[float]:
        """
        Calculate and return the series of percentage returns.

        :return: A list of percentage returns.
        """
        return [(self.values[i+1] - self.values[i]) / self.values[i] for i in range(len(self.values) - 1)]

    def __repr__(self):
        return f"TimeSeries({self.asset_name}, {len(self.values)} data points)"
