"""
Pytest configuration and fixtures
"""

import pytest
from datetime import datetime
from portfolio_simulations.asset import Asset
from portfolio_simulations.portfolio import Portfolio


@pytest.fixture
def sample_dates():
    """Sample dates for testing"""
    return [
        datetime(2020, 1, 1),
        datetime(2020, 6, 1),
        datetime(2021, 1, 1),
        datetime(2021, 6, 1),
        datetime(2022, 1, 1)
    ]


@pytest.fixture
def sample_values():
    """Sample values for testing"""
    return [100.0, 105.0, 110.0, 115.0, 120.0]


@pytest.fixture
def sample_asset(sample_dates, sample_values):
    """Sample asset for testing"""
    return Asset("TEST", weight=0.5, values=sample_values, dates=sample_dates)


@pytest.fixture
def sample_portfolio(sample_dates, sample_values):
    """Sample portfolio for testing"""
    portfolio = Portfolio()
    
    # Add two assets
    portfolio.add_asset("ASSET1", weight=0.6, values=sample_values, dates=sample_dates)
    portfolio.add_asset("ASSET2", weight=0.4, values=[v * 1.1 for v in sample_values], dates=sample_dates)
    
    portfolio.add_start_date(datetime(2020, 1, 1))
    portfolio.add_end_date(datetime(2022, 1, 1))
    
    return portfolio
