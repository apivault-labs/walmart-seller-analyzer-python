import os
from walmart_seller_analyzer import WalmartSellerAnalyzerClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = WalmartSellerAnalyzerClient()
print(client.run_one({'mode': 'niche', 'searchQueries': ['wireless earbuds'], 'maxResultsPerQuery': 20}))
