import json
from walmart_seller_analyzer import WalmartSellerAnalyzerClient

rows = WalmartSellerAnalyzerClient().run({'mode': 'niche', 'searchQueries': ['wireless earbuds'], 'maxResultsPerQuery': 20})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
