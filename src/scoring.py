def compute_deal_score(row, avg_price_per_sqft=450):
    score = 0
    if row.get("sqft") and row.get("price"):
        price_per_sqft = row["price"] / row["sqft"]
        if price_per_sqft < avg_price_per_sqft:
            score += (avg_price_per_sqft - price_per_sqft) * 0.5
    if "as-is" in row.get("description", "").lower() or "fixer" in row.get("description", "").lower():
        score += 10
    if row.get("days_on_market", 0) > 20:
        score += 5
    return round(score, 2)

def add_scores(df):
    df["deal_score"] = df.apply(compute_deal_score, axis=1)
    return df

if __name__ == "__main__":
    import fetch_listings
    listings = fetch_listings.fetch_sample_listings()
    print(f"📦 Fetched {len(listings)} listings:")
    print(listings)
    scored = add_scores(listings)
    print("🔍 Scored listings:")
    print(scored.sort_values("deal_score", ascending=False))