from walmart_seller_analyzer import WalmartSellerAnalyzerClient

for count in (10, 100, 1000):
    print(count, WalmartSellerAnalyzerClient.estimate_cost(count), "USD estimated result charges")
