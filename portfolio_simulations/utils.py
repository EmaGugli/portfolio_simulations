import numpy as np
from datetime import datetime
from typing import Dict, List

def calculate_portfolio_statistics(assets: List, 
    start_date: datetime,
    end_date: datetime,
    num_simulations: int = 1000
) -> Dict[str, float]:
    """
    Calculate portfolio statistics using Monte Carlo simulation.
    
    Args:
        assets: List of Asset objects
        start_date: Start date for analysis
        end_date: End date for analysis
        num_simulations: Number of Monte Carlo simulations
        
    Returns:
        Dictionary containing mean return, variance, and Sharpe ratio
    """
    # Get the time series data for each asset
    returns_list = []
    weights = []
    
    for asset in assets:
        asset.set_window(start_date, end_date)
        returns_list.append(asset.get_returns())
        weights.append(asset.weight)

    # Calculate the weighted average returns
    weighted_returns = np.average(returns_list, weights=weights)

    # Run the Monte Carlo simulation
    simulations = np.random.normal(loc=weighted_returns, scale=np.std(returns_list), size=num_simulations)

    # Calculate the portfolio statistics
    mean_return = np.mean(simulations)
    variance = np.var(simulations)
    sharpe_ratio = mean_return / np.sqrt(variance) if variance > 0 else 0

    # Return the statistics
    return {
        "mean_return": mean_return,
        "variance": variance,
        "sharpe_ratio": sharpe_ratio
    }