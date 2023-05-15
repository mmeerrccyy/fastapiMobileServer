FROM = "spry-cortex-385701.test_ds.test_table"

QUERY_ALL_TEAMS = f"""
    SELECT Team, COUNT(*) amount
    FROM `{FROM}`
    GROUP BY Team
"""