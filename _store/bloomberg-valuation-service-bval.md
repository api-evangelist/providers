---
aid: bloomberg-valuation-service-bval
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-valuation-service-bval/refs/heads/main/apis.yml
apis:
- name: BVAL Pricing API
  description: Retrieve end-of-day and intraday valuations for fixed income securities including corporate bonds, government bonds, and structured products.
  image: https://www.bloomberg.com/company/press/bloomberg-logo/
  humanURL: https://www.bloomberg.com/professional/product/valuation-service/
  baseURL: https://api.bloomberg.com/bval/v1
  tags:
  - Bonds
  - Fixed Income
  - Pricing
  - Valuations
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Authentication
    url: https://www.bloomberg.com/professional/support/api-library/
  contact:
  - FN: Bloomberg Support
    email: support@bloomberg.com
    url: https://www.bloomberg.com/professional/support/
- name: BVAL Reference Data API
  description: Access security master data, identifiers, and characteristics for securities covered by BVAL including ISINs, CUSIPs, and security attributes.
  image: https://www.bloomberg.com/company/press/bloomberg-logo/
  humanURL: https://www.bloomberg.com/professional/product/valuation-service/
  baseURL: https://api.bloomberg.com/bval/v1/reference
  tags:
  - Identifiers
  - Master Data
  - Reference Data
  - Securities
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: OpenAPI
    url: https://api.bloomberg.com/bval/v1/reference/openapi.json
  contact:
  - FN: Bloomberg Support
    email: support@bloomberg.com
- name: BVAL Spread Analytics API
  description: Retrieve spread calculations, yield curves, and analytics for credit analysis including OAS, Z-spreads, and G-spreads.
  image: https://www.bloomberg.com/company/press/bloomberg-logo/
  humanURL: https://www.bloomberg.com/professional/product/valuation-service/
  baseURL: https://api.bloomberg.com/bval/v1/analytics
  tags:
  - Analytics
  - Credit Analysis
  - Spreads
  - Yield Curves
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Swagger
    url: https://api.bloomberg.com/bval/v1/analytics/swagger.json
  contact:
  - FN: Bloomberg Support
    email: support@bloomberg.com
- name: BVAL Curve Data API
  description: Access benchmark curves, swap curves, and government curves used in BVAL's valuation methodology across multiple currencies and markets.
  image: https://www.bloomberg.com/company/press/bloomberg-logo/
  humanURL: https://www.bloomberg.com/professional/product/valuation-service/
  baseURL: https://api.bloomberg.com/bval/v1/curves
  tags:
  - Benchmarks
  - Curves
  - Swap Curves
  - Yield Curves
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: API Terms of Service
    url: https://www.bloomberg.com/professional/support/api-terms/
  contact:
  - FN: Bloomberg Support
    email: support@bloomberg.com
name: Bloomberg Valuation Service (BVAL)
tags:
- Bonds
- Derivatives
- Financial Data
- Fixed Income
- Market Data
- Pricing
- Valuations
type: Contract
image: https://www.bloomberg.com/company/press/bloomberg-logo/
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg Valuation Service (BVAL) provides independent, transparent evaluations for fixed income and derivative instruments. BVAL delivers pricing for over 2.5 million securities across multiple asset classes including corporate bonds, municipal bonds, structured products, and OTC derivatives.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

