#!/usr/bin/env python3
"""
Basic usage example for portfolio_simulations package
"""

from datetime import datetime
from portfolio_simulations import Portfolio, Asset, calculate_portfolio_statistics


def main():
    """Demonstrate basic package usage"""
    print("Portfolio Simulations - Basic Usage Example")
    print("=" * 50)
    
    # Create a portfolio
    portfolio = Portfolio()
    
    # Add some assets with custom data (for demonstration)
    # In real usage, you would use ticker symbols like "AAPL", "GOOGL", etc.
    dates = [
        datetime(2020, 1, 1),
        datetime(2020, 6, 1),
        datetime(2021, 1, 1),
        datetime(2021, 6, 1),
        datetime(2022, 1, 1),
        datetime(2022, 6, 1),
        datetime(2023, 1, 1)
    ]
    
    # Asset 1: Steady growth
    values1 = [100, 105, 110, 115, 120, 125, 130]
    portfolio.add_asset("SteadyGrowth", weight=0.6, values=values1, dates=dates)
    
    # Asset 2: More volatile
    values2 = [200, 190, 220, 210, 230, 225, 240]
    portfolio.add_asset("VolatileAsset", weight=0.4, values=values2, dates=dates)
    
    # Set analysis period
    portfolio.add_start_date(datetime(2020, 1, 1))
    portfolio.add_end_date(datetime(2023, 1, 1))
    
    # Print portfolio information
    print("\nPortfolio Configuration:")
    portfolio.print_portfolio()
    
    # Calculate portfolio statistics
    print("\nCalculating portfolio statistics...")
    stats = calculate_portfolio_statistics(
        assets=portfolio.assets,
        start_date=datetime(2020, 1, 1),
        end_date=datetime(2023, 1, 1),
        num_simulations=1000
    )
    
    print(f"\nPortfolio Statistics:")
    print(f"Mean Return: {stats['mean_return']:.4f} ({stats['mean_return']*100:.2f}%)")
    print(f"Variance: {stats['variance']:.6f}")
    print(f"Sharpe Ratio: {stats['sharpe_ratio']:.4f}")
    
    # Run Monte Carlo simulation
    print("\nRunning Monte Carlo simulation...")
    portfolio.compute_return_distribution(
        rolling_window=2,  # 2-year rolling window
        num_simulations=1000
    )
    
    print(f"Simulation completed with {len(portfolio.portfolio_returns)} scenarios")
    print(f"Average portfolio return: {sum(portfolio.portfolio_returns)/len(portfolio.portfolio_returns):.4f}")
    
    # Note: Uncomment the next line to display the plot
    # portfolio.plot_return_distributions()


if __name__ == "__main__":
    main()
