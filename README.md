# Walmart Seller Analyzer — Python SDK

Python client for the [Walmart Seller Analyzer Apify Actor](https://apify.com/apivault_labs/walmart-seller-revenue-product-opportunity-analyzer). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/walmart-seller-revenue-product-opportunity-analyzer)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Seller and product revenue estimates
- Profit, margin and ROI scenarios
- Buy Box and offer signals
- Product opportunity ranking

The Actor uses public marketplace signals and returns estimates or ranges where a platform does not publish exact figures.

## Install

```bash
pip install git+https://github.com/apivault-labs/walmart-seller-analyzer-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from walmart_seller_analyzer import WalmartSellerAnalyzerClient

client = WalmartSellerAnalyzerClient(api_token="apify_api_xxxxxx")
rows = client.run({'mode': 'niche', 'searchQueries': ['wireless earbuds'], 'maxResultsPerQuery': 20})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | `string` | `niche` | Choose seller portfolio analysis, individual product analysis, or keyword-based niche research. |
| `sellerUrls` | `array` | `—` | Public Walmart seller storefront URLs used in seller mode. |
| `productUrls` | `array` | `—` | Public Walmart product URLs used in product mode. |
| `productIds` | `array` | `—` | Numeric Walmart US item IDs used in product mode. |
| `searchQueries` | `array` | `—` | Product keywords searched on Walmart in niche mode. |
| `maxProductsPerSeller` | `integer` | `25` | Maximum number of unique seller products included in one report. |
| `maxResultsPerQuery` | `integer` | `40` | Maximum number of unique Walmart search products returned for each keyword. |
| `includeProductDetails` | `boolean` | `True` | Add UPC, seller, offer, price, fulfillment, and additional market intelligence when available. |
| `maxDetailedProducts` | `integer` | `20` | Maximum number of products enriched with additional market intelligence per seller or query. |
| `postalCode` | `string` | `95829` | Requested location context. Compare it with locationText in the output because Walmart may retain a different public-session location. |
| `storeId` | `string` | `—` | Requested Walmart store context recorded alongside the observed location. |
| `costOfGoodsPercent` | `number` | `30` | Estimated product acquisition cost as a percentage of selling price. |
| `shippingCostPerOrderUsd` | `number` | `0` | Average seller-paid shipping cost per order in USD. |
| `wfsFeePerOrderUsd` | `number` | `0` | Estimated Walmart Fulfillment Services cost per order in USD. |
| `advertisingRatePercent` | `number` | `0` | Estimated advertising spend as a percentage of product revenue. |
| `refundRatePercent` | `number` | `2` | Estimated refunds and returns allowance as a percentage of revenue. |
| `maxConcurrency` | `integer` | `4` | Controls parallel processing. The default provides a reliable speed/cost balance. |
| `proxyConfiguration` | `object` | `{"useApifyProxy":true,"apifyProxyGroups":["RESIDENTIAL"]}` | Apify Residential Proxy is recommended for reliable Walmart access. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/walmart-seller-revenue-product-opportunity-analyzer).

## Pricing

Pay per delivered result through Apify, starting around **$5/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
