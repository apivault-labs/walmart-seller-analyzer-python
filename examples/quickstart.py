from walmart_seller_analyzer import WalmartSellerAnalyzerClient

client = WalmartSellerAnalyzerClient()
rows = client.run({'mode': 'niche', 'searchQueries': ['wireless earbuds'], 'maxResultsPerQuery': 20})
print(rows[0] if rows else "No results")
