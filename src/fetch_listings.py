import pandas as pd

def fetch_sample_listings():
    return pd.DataFrame([
        {
            "listing_id": "1001",
            "address": "123 Main St",
            "city": "Toronto",
            "price": 450000,
            "bedrooms": 3,
            "bathrooms": 2,
            "sqft": 1200,
            "days_on_market": 12,
            "description": "Great investment property!"
        },
        {
            "listing_id": "1002",
            "address": "456 Oak Ave",
            "city": "Toronto",
            "price": 375000,
            "bedrooms": 2,
            "bathrooms": 1,
            "sqft": 900,
            "days_on_market": 25,
            "description": "Fixer-upper, sold as-is"
        }
    ])