"""
Tests for the Portfolio class
"""

import pytest
from datetime import datetime
from portfolio_simulations.portfolio import Portfolio
from portfolio_simulations.asset import Asset


class TestPortfolio:
    """Test cases for Portfolio class"""
    
    def test_portfolio_creation(self):
        """Test creating empty portfolio"""
        portfolio = Portfolio()
        
        assert portfolio.assets == []
        assert not hasattr(portfolio, 'start_date')
        assert not hasattr(portfolio, 'end_date')
    
    def test_add_asset(self):
        """Test adding asset to portfolio"""
        portfolio = Portfolio()
        
        # Create mock asset data
        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
        values = [100.0, 105.0]
        
        portfolio.add_asset("TEST", weight=0.5, values=values, dates=dates)
        
        assert len(portfolio.assets) == 1
        assert portfolio.assets[0].asset_name == "TEST"
        assert portfolio.assets[0].weight == 0.5
    
    def test_add_start_date(self):
        """Test adding start date"""
        portfolio = Portfolio()
        start_date = datetime(2020, 1, 1)
        
        portfolio.add_start_date(start_date)
        
        assert portfolio.start_date == start_date
    
    def test_add_end_date(self):
        """Test adding end date"""
        portfolio = Portfolio()
        end_date = datetime(2023, 12, 31)
        
        portfolio.add_end_date(end_date)
        
        assert portfolio.end_date == end_date
    
    def test_print_portfolio(self, capsys):
        """Test printing portfolio information"""
        portfolio = Portfolio()
        
        # Add some assets
        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
        values = [100.0, 105.0]
        
        portfolio.add_asset("TEST1", weight=0.6, values=values, dates=dates)
        portfolio.add_asset("TEST2", weight=0.4, values=values, dates=dates)
        
        portfolio.add_start_date(datetime(2020, 1, 1))
        portfolio.add_end_date(datetime(2020, 1, 2))
        
        portfolio.print_portfolio()
        
        captured = capsys.readouterr()
        assert "Start date: 2020-01-01" in captured.out
        assert "End date: 2020-01-02" in captured.out
        assert "TEST1: 0.6" in captured.out
        assert "TEST2: 0.4" in captured.out
