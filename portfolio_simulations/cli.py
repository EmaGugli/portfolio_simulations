"""
Command Line Interface for Portfolio Simulations
"""

import argparse
from datetime import datetime
from .portfolio import Portfolio
from .asset import Asset


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Portfolio Simulations CLI")
    
    parser.add_argument(
        "--assets", 
        nargs="+", 
        help="Asset tickers to include in portfolio"
    )
    parser.add_argument(
        "--weights", 
        nargs="+", 
        type=float,
        help="Weights for each asset (must sum to 1.0)"
    )
    parser.add_argument(
        "--start-date", 
        type=str,
        help="Start date for analysis (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--end-date", 
        type=str,
        help="End date for analysis (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--simulations", 
        type=int, 
        default=1000,
        help="Number of Monte Carlo simulations"
    )
    parser.add_argument(
        "--rolling-window", 
        type=int, 
        default=5,
        help="Rolling window in years"
    )
    parser.add_argument(
        "--plot", 
        action="store_true",
        help="Display plot of return distributions"
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.assets and args.weights:
        if len(args.assets) != len(args.weights):
            print("Error: Number of assets must match number of weights")
            return 1
        
        if abs(sum(args.weights) - 1.0) > 0.001:
            print("Error: Weights must sum to 1.0")
            return 1
    
    # Create portfolio
    portfolio = Portfolio()
    
    # Add assets
    if args.assets and args.weights:
        for asset, weight in zip(args.assets, args.weights):
            portfolio.add_asset(asset, weight)
    
    # Set date range
    if args.start_date:
        start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        portfolio.add_start_date(start_date)
    
    if args.end_date:
        end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
        portfolio.add_end_date(end_date)
    
    # Run simulation
    try:
        portfolio.compute_return_distribution(
            rolling_window=args.rolling_window,
            num_simulations=args.simulations
        )
        
        # Print results
        portfolio.print_portfolio()
        print(f"\nSimulation completed with {args.simulations} simulations")
        
        if args.plot:
            portfolio.plot_return_distributions()
            
    except Exception as e:
        print(f"Error during simulation: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
