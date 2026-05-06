---
aid: southern
name: Southern Company
description: Southern Company is a leading American gas and electric utility holding company headquartered in Atlanta, Georgia. Through its subsidiaries — Alabama Power, Georgia Power, Mississippi Power, Southern Natural Gas, and Southern Company Gas — it serves 9 million gas and electric utility customers across 6 states. Southern Company is a Fortune 500 company with operations spanning electricity generation, transmission, distribution, and natural gas distribution.
url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Fortune 500
  - Electric Utility
  - Natural Gas
  - Energy
apis:
  - aid: southern:southern-company-customer-api
    name: Southern Company Customer Account API
    description: The Southern Company Customer Account API provides access to utility account data for Alabama Power, Georgia Power, and Mississippi Power customers. It supports reading energy usage data, account balances, billing history, and daily consumption data with costs and kilowatt-hour measurements.
    humanURL: https://www.southerncompany.com/
    baseURL: https://customerservice2.southernco.com
    tags:
      - Electric Utility
      - Energy Usage
      - Customer Data
      - Billing
    properties:
      - type: Documentation
        url: https://www.southerncompany.com/
      - type: GitHub
        url: https://github.com/apearson/southern-company-api
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/json-schema/southern-utility-account-schema.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/json-schema/southern-energy-usage-schema.json
  - aid: southern:southern-company-investor-relations
    name: Southern Company Investor Relations
    description: Southern Company's investor relations portal provides financial data, earnings summaries, filings, reports, and shareholder information for investors and analysts.
    humanURL: https://investor.southerncompany.com/
    tags:
      - Investor Relations
      - Financial Data
      - Energy
    properties:
      - type: Website
        url: https://investor.southerncompany.com/home/default.aspx
      - type: Download Library
        url: https://investor.southerncompany.com/news-and-resources/download-library/default.aspx
common:
  - type: Website
    url: https://www.southerncompany.com
  - type: Investor Relations
    url: https://investor.southerncompany.com/
  - type: GitHub Organization
    url: https://github.com/Southern-Company-HA
  - type: LinkedIn
    url: https://www.linkedin.com/company/southern-company
  - type: X
    url: https://twitter.com/SouthernCompany
  - type: Facebook
    url: https://www.facebook.com/SOCompany
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/json-ld/southern-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/vocabulary/southern-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
