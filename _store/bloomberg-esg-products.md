---
aid: bloomberg-esg-products
name: Bloomberg ESG Products
description: Bloomberg ESG Products provide environmental, social, and governance data, analytics, and scores to help investors assess sustainability risks and opportunities. Bloomberg collects ESG data from thousands of companies globally, offering ESG scores, climate data, green bond data, and sustainable finance analytics through the Bloomberg Terminal and API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-esg-products/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - ESG
  - Sustainability
  - Environmental Data
  - Social Data
  - Governance Data
  - Climate Data
  - Bloomberg
apis:
  - aid: bloomberg-esg-products:esg-data-api
    name: Bloomberg ESG Data API
    description: Access Bloomberg ESG scores, environmental metrics, social indicators, and governance data for thousands of publicly listed companies globally. Data sourced directly from company disclosures and standardized for comparability.
    humanURL: https://www.bloomberg.com/professional/solution/esg-data/
    baseURL: blpapi://localhost:8194
    tags:
      - ESG
      - Environmental
      - Social
      - Governance
      - Scores
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/esg-data/
  - aid: bloomberg-esg-products:climate-data-api
    name: Bloomberg Climate Data API
    description: Access physical and transition climate risk data, carbon emissions data, TCFD-aligned metrics, and scenario analysis tools through Bloomberg's climate data solutions.
    humanURL: https://www.bloomberg.com/professional/solution/climate-data/
    baseURL: blpapi://localhost:8194
    tags:
      - Climate
      - Carbon Emissions
      - TCFD
      - Physical Risk
      - Transition Risk
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/climate-data/
  - aid: bloomberg-esg-products:green-bond-data
    name: Bloomberg Green Bond Data
    description: Comprehensive data on green, social, sustainability, and sustainability-linked bonds including use of proceeds, certifications, and post-issuance reporting aligned to ICMA principles.
    humanURL: https://www.bloomberg.com/professional/solution/sustainable-finance/
    baseURL: blpapi://localhost:8194
    tags:
      - Green Bonds
      - Sustainable Finance
      - Fixed Income
      - ICMA
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/sustainable-finance/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: ESG Scores
        description: Standardized ESG scores for thousands of companies based on disclosed data.
      - name: Environmental Metrics
        description: Carbon emissions, water usage, energy consumption, and waste data.
      - name: Social Indicators
        description: Employee relations, diversity metrics, health and safety, and community data.
      - name: Governance Data
        description: Board composition, executive compensation, shareholder rights, and audit data.
      - name: Climate Risk Analytics
        description: Physical and transition climate risk metrics aligned to TCFD framework.
      - name: Sustainable Finance Data
        description: Green bond, social bond, and sustainability-linked loan data.
  - type: UseCases
    data:
      - name: ESG Integration
        description: Integrate ESG factors into investment analysis and portfolio construction.
      - name: Regulatory Reporting
        description: Support SFDR, EU Taxonomy, and other ESG regulatory reporting requirements.
      - name: Stewardship and Engagement
        description: Use ESG data to support shareholder engagement and proxy voting decisions.
      - name: Sustainable Product Development
        description: Develop ESG-linked financial products and indices.
      - name: Climate Risk Assessment
        description: Assess and disclose climate-related financial risks in portfolios.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
