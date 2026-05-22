"""
Author: Jijeesh Valappil
Module: Data Center Energy Optimization & Infrastructure Balancer
"""
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [Jijeesh Valappil] - %(levelname)s - %(message)s")

def calculate_energy_savings(decommissioned_hosts: int) -> float:
    """Calculates datacenter environmental and maintenance cost metrics.

    Args:
        decommissioned_hosts (int): Total count of physical server blocks removed.

    Returns:
        float: Estimated operational expenditure savings percentage.
    """
    if decommissioned_hosts <= 0:
        return 0.0
    savings_ratio = decommissioned_hosts * 2.5
    logging.info(f"Consolidation metrics parsed. Estimated savings calculated at: {savings_ratio}%")
    return round(savings_ratio, 2)