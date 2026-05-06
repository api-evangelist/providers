---
aid: valero-energy
name: Valero Energy
description: Valero Energy Corporation is the world's largest independent petroleum refiner and a leading producer of low-carbon transportation fuels. Headquartered in San Antonio, Texas, Valero operates 14 petroleum refineries with 3 million barrels per day capacity, 12 ethanol plants, and renewable diesel production facilities across the US, Canada, and UK. The company trades on NYSE as VLO and is a Fortune 100 company.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Petroleum
  - Refining
  - Renewable Fuels
  - Fortune 100
  - Ethanol
  - Renewable Diesel
created: '2026-03-21'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: valero-energy:sec-edgar
    name: Valero Energy SEC EDGAR Data
    description: Valero Energy Corporation SEC filings and financial data available through the SEC EDGAR system. Includes 10-K, 10-Q, earnings releases, and other regulatory filings. Accessible via the SEC EDGAR API using CIK 0001035002.
    humanURL: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001035002
    tags:
      - SEC
      - EDGAR
      - Financial Data
      - Regulatory Filings
      - Investor Relations
    properties:
      - type: Documentation
        url: https://efts.sec.gov/LATEST/search-index?q=%22valero%22&dateRange=custom&startdt=2024-01-01
      - type: InvestorRelations
        url: https://investorvalero.com/
      - type: SECFilings
        url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001035002&type=10-K&dateb=&owner=include&count=10
  - aid: valero-energy:investor-relations
    name: Valero Investor Relations Portal
    description: Valero Energy investor relations portal providing access to financial data, quarterly results, SEC filings, stock information, dividend history, and corporate governance documents.
    humanURL: https://investorvalero.com/
    tags:
      - Investor Relations
      - Financial Data
      - Stock Data
      - Dividends
    properties:
      - type: InvestorRelations
        url: https://investorvalero.com/
      - type: StockQuote
        url: https://investorvalero.com/stock-information/stock-quote
      - type: SECFilings
        url: https://investorvalero.com/financials/sec-filings
common:
  - type: Website
    url: https://www.valero.com/
  - type: InvestorRelations
    url: https://investorvalero.com/
  - type: SECEdgar
    url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001035002
  - type: PrivacyPolicy
    url: https://www.valero.com/privacy-policy
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/vocabulary/valero-energy-vocabulary.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/json-schema/valero-energy-refinery-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
