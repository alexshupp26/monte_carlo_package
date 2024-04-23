"""
Unit and regression test for the monte_carlo_package package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import monte_carlo_package


def test_monte_carlo_package_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "monte_carlo_package" in sys.modules
