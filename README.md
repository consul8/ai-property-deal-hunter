# AI Property Deal Hunter

AI-powered engine to identify real estate listings on Realtor.ca that are priced below market value.

## 🔍 Features

- Scrapes listings using Realtor.ca wrapper
- Calculates deal score based on price/sqft, price drops, days on market
- Stores and indexes listings in a local SQLite DB
- CLI-based interface for fast results
- Modular Python design for future AI model enhancements

## 🧠 Deal Scoring Logic

- Compares $/sqft to neighborhood averages
- Detects large price drops
- Considers DOM (days on market)
- Flags keywords like "fixer", "motivated", "as-is"

## ⚙️ Getting Started

```bash
git clone https://github.com/consul8/ai-property-deal-hunter.git
cd ai-property-deal-hunter
pip install -r requirements.txt
python src/main.py
```

## 📂 Directory Structure

```
src/
├── fetch_listings.py     # Realtor.ca scraping logic
├── scoring.py            # Deal score logic
├── database.py           # SQLite schema and operations
└── main.py               # CLI runner
```

## 📄 License

MIT — see `LICENSE` for details.
