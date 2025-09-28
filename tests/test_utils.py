"""
Tests for utility functions
"""

import pytest
from datetime import datetime
from portfolio_simulations.utils import calculate_portfolio_statistics
from portfolio_simulations.asset import Asset


class TestUtils:
    """Test cases for utility functions"""
    
    def test_calculate_portfolio_statistics(self):
        """Test calculating portfolio statistics"""
        # Create mock assets
        dates = [datetime(2020, 1, 1), datetime(2021, 1, 1)]
        values1 = [100.0, 110.0]  # 10% return
        values2 = [200.0, 220.0]  # 10% return
        
        asset1 = Asset("TEST1", weight=0.6, values=values1, dates=dates)
        asset2 = Asset("TEST2", weight=0.4, values=values2, dates=dates)
        
        assets = [asset1, asset2]
        
        stats = calculate_portfolio_statistics(
            assets=assets,
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2021, 1, 1),
            num_simulations=100
        )
        
        # Check that all expected keys are present
        assert "mean_return" in stats
        assert "variance" in stats
        assert "sharpe_ratio" in stats
        
        # Check that values are reasonable
        assert isinstance(stats["mean_return"], float)
        assert isinstance(stats["variance"], float)
        assert isinstance(stats["sharpe_ratio"], float)
        
        # Variance should be non-negative
        assert stats["variance"] >= 0
