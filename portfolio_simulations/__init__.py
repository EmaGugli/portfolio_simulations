"""
Portfolio Simulations Package

A Python package for simulating portfolio returns and analyzing investment strategies.
"""

from .asset import Asset
from .portfolio import Portfolio
from .utils import calculate_portfolio_statistics

__version__ = "0.0.0"
__author__ = "Emanuele Gugliandolo"
__email__ = "emanuelegugliandolo@gmail.com"

__all__ = [
    "Asset",
    "Portfolio", 
    "calculate_portfolio_statistics"
]
