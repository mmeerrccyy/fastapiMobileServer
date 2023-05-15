FROM = "ippt-tsd.phones_data.ukrainian-market-mobile-phones-data"

QUERY_ALL_OS = f"""
    SELECT DISTINCT os
    FROM `{FROM}`
"""

QUERY_AMOUNT_DEVICES_PER_OS = f"""
    SELECT os, COUNT(*) amount_devices
    FROM `{FROM}`
    GROUP BY os
"""