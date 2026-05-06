---
aid: bureau-of-economic-analysis
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-economic-analysis/refs/heads/main/apis.yml
name: Bureau of Economic Analysis
tags:
  - Economics
  - Federal Government
  - GDP
  - National Accounts
  - Statistics
  - Trade
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-21'
position: Consumer
description: The U.S. Bureau of Economic Analysis (BEA) is a principal federal statistical agency that produces accurate and objective data about the U.S. economy. BEA publishes GDP, personal income, corporate profits, international trade and investment data, and industry-level economic accounts. The BEA Data API provides programmatic access to these economic statistics.
apis:
  - aid: bureau-of-economic-analysis:bureau-of-economic-analysis-api
    name: Bureau of Economic Analysis (BEA) Data API
    tags:
      - Economics
      - Federal Government
      - GDP
      - National Accounts
      - Statistics
    humanURL: https://www.bea.gov/tools/
    baseURL: https://apps.bea.gov/api/data
    properties:
      - url: https://www.bea.gov/tools/
        type: Documentation
      - url: https://apps.bea.gov/API/docs/index.htm
        type: Reference
      - type: OpenAPI
        url: properties/bureau-of-economic-analysis-bea-api-openapi.yml
      - url: https://apps.bea.gov/API/signup/index.cfm
        type: SignUp
    description: The BEA Data API provides programmatic access to BEA's published economic statistics including GDP, national income, personal income, corporate profits, international trade and investment, and industry accounts. Supports multiple datasets including NIPA, Fixed Assets, ITA, IIP, GDPbyIndustry, Regional, and more.
    x-features:
      - National Income and Product Accounts (NIPA) data
      - GDP by Industry datasets
      - Regional economic data by state and metro area
      - International Trade in Goods and Services (ITA)
      - International Investment Position (IIP)
      - Fixed Assets accounts
      - Underlying Detail Tables
      - API key authentication
    x-use-cases:
      - Economic research and analysis
      - Financial modeling with GDP components
      - Regional economic development planning
      - International trade and investment analysis
      - Academic and government research
  - aid: bureau-of-economic-analysis:bea-gdp-data
    name: BEA GDP Data
    tags:
      - Economics
      - GDP
      - Federal Government
      - National Accounts
    humanURL: https://www.bea.gov/data/gdp/gross-domestic-product
    baseURL: https://apps.bea.gov/api/data
    properties:
      - url: https://www.bea.gov/data/gdp/gross-domestic-product
        type: Documentation
      - url: https://apps.bea.gov/api/data?UserID=YOUR_KEY&method=GetData&DataSetName=NIPA&TableName=T10101&Frequency=Q&Year=X&ResultFormat=JSON
        type: DataAPI
    description: Gross Domestic Product (GDP) data from the BEA, available quarterly and annually. Includes GDP growth rates, GDP by expenditure components, and real vs. nominal GDP measures.
common:
  - type: Portal
    url: https://www.bea.gov/tools/
  - type: Documentation
    url: https://apps.bea.gov/API/docs/index.htm
  - type: Getting Started
    url: https://www.bea.gov/tools/faq
  - type: Website
    url: https://www.bea.gov/
  - type: SignUp
    url: https://apps.bea.gov/API/signup/index.cfm
  - type: Data Visualizations
    url: https://www.bea.gov/itable/
  - type: Press Releases
    url: https://www.bea.gov/news
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
