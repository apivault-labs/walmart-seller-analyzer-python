from walmart_seller_analyzer import WalmartSellerAnalyzerClient

client = WalmartSellerAnalyzerClient()
payload = {'mode': 'niche', 'searchQueries': ['wireless earbuds'], 'maxResultsPerQuery': 20}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
