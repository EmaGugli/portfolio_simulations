"""
Tests for the Asset class
"""

import pytest
from datetime import datetime, timedelta
from portfolio_simulations.asset import Asset


class TestAsset:
    """Test cases for Asset class"""
    
    def test_asset_creation_with_custom_data(self):
        """Test creating asset with custom data"""
        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)]
        values = [100.0, 105.0, 110.0]
        
        asset = Asset("TEST", weight=0.5, values=values, dates=dates)
        
        assert asset.asset_name == "TEST"
        assert asset.weight == 0.5
        assert len(asset.historical_data) == 3
        assert asset.historical_data['Close'].iloc[0] == 100.0
    
    def test_asset_creation_mismatched_data(self):
        """Test that mismatched data lengths raise ValueError"""
        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
        values = [100.0, 105.0, 110.0]  # Different length
        
        with pytest.raises(ValueError, match="The length of values and dates must be the same"):
            Asset("TEST", weight=0.5, values=values, dates=dates)
    
    def test_asset_creation_partial_data(self):
        """Test that partial data raises ValueError"""
        dates = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
        values = None
        
        with pytest.raises(ValueError, match="Both values and dates must be passed"):
            Asset("TEST", weight=0.5, values=values, dates=dates)
    
    def test_set_window(self):
        """Test setting date window"""
        dates = [
            datetime(2020, 1, 1), 
            datetime(2020, 6, 1), 
            datetime(2021, 1, 1),
            datetime(2021, 6, 1)
        ]
        values = [100.0, 105.0, 110.0, 115.0]
        
        asset = Asset("TEST", weight=0.5, values=values, dates=dates)
        
        # Set window to 2020 only
        asset.set_window(datetime(2020, 1, 1), datetime(2020, 12, 31))
        
        assert len(asset.historical_data) == 2  # Only 2020 data
        assert asset.historical_data['Date'].min() == datetime(2020, 1, 1)
        assert asset.historical_data['Date'].max() == datetime(2020, 6, 1)
    
    def test_get_returns(self):
        """Test calculating returns"""
        dates = [datetime(2020, 1, 1), datetime(2021, 1, 1)]
        values = [100.0, 110.0]  # 10% return over 1 year
        
        asset = Asset("TEST", weight=0.5, values=values, dates=dates)
        
        returns = asset.get_returns()
        expected_return = 0.10  # 10% annual return
        
        assert abs(returns - expected_return) < 0.01  # Allow small floating point differences
