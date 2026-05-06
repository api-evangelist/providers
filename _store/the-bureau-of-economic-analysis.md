---
aid: the-bureau-of-economic-analysis
url: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/apis.yml
apis:
  - aid: the-bureau-of-economic-analysis:the-bureau-of-economic-analysis
    name: The Bureau of Economic Analysis API
    tags:
      - Economics
      - Federal Government
      - GDP
      - National Accounts
      - Statistics
    humanURL: https://www.bea.gov/resources/for-developers
    baseURL: https://apps.bea.gov/api/data
    properties:
      - url: https://www.bea.gov/resources/for-developers
        type: Documentation
      - url: https://apps.bea.gov/api/signup/
        type: Sign Up
      - url: https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf
        type: GettingStarted
      - url: https://apps.bea.gov/API/docs/index.htm
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/openapi/the-bureau-of-economic-analysis-openapi.yml
        type: OpenAPI
    description: The Bureau of Economic Analysis (BEA) Data API provides programmatic access to BEA published economic statistics. Methods include retrieving statistical data and metadata from datasets covering National Income and Product Accounts (NIPA), GDP by Industry, Regional economic data by state and metro area, International Transactions Accounts (ITA), International Investment Position (IIP), Fixed Assets, Input-Output tables, Multinational Enterprises (MNE), and International Services Trade. Data is available in JSON or XML formats and requires a free API key.
    contact:
      - FN: BEA Developer Support
        url: https://www.bea.gov/resources/for-developers
        email: BEA.Data.API@bea.gov
    features:
      - Dataset Discovery
      - Parameter Discovery
      - NIPA Tables
      - GDP Data
      - Regional Economic Data
      - International Transactions
      - Fixed Assets
      - Input-Output Tables
      - Multinational Enterprise Data
      - JSON and XML Response Formats
    useCases:
      - Economic Research and Analysis
      - GDP Monitoring and Reporting
      - Regional Economic Development Planning
      - Trade Balance Analysis
      - Business Intelligence and Forecasting
      - Academic Research
      - Government Policy Analysis
    integrations:
      - url: https://github.com/us-bea/beaapi
        name: BEA Python Library
        type: SDK
      - url: https://github.com/us-bea/bea.R
        name: BEA R Library
        type: SDK
name: The Bureau of Economic Analysis
tags:
  - Economics
  - Federal Government
  - GDP
  - National Accounts
  - Open Data
  - Statistics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-05-03'
position: Consuming
description: The Bureau of Economic Analysis (BEA) is an agency within the U.S. Department of Commerce that provides economic data to policymakers, businesses, and the general public. The BEA collects and analyzes a wide range of economic indicators, including gross domestic product (GDP), personal income, and trade data. Through its reports and analysis, the BEA helps inform decision-making at all levels of government and helps businesses and individuals understand the state of the economy. The BEA Data API provides programmatic access to all published economic statistics including NIPA, regional data, international accounts, and industry-level data.
common:
  - type: Website
    url: https://www.bea.gov/
  - type: Documentation
    url: https://www.bea.gov/resources/for-developers
  - type: Sign Up
    url: https://apps.bea.gov/api/signup/
  - type: GettingStarted
    url: https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf
  - type: GitHub Organization
    url: https://github.com/us-bea
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/openapi/the-bureau-of-economic-analysis-openapi.yml
  - type: InteractiveData
    url: https://apps.bea.gov/itable
  - type: RSS
    url: https://apps.bea.gov/rss/rss.xml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
