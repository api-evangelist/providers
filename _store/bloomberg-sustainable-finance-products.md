---
aid: bloomberg-sustainable-finance-products
name: Bloomberg Sustainable Finance Products
description: Bloomberg Sustainable Finance Products provide comprehensive data, analytics, and tools for sustainable investing, green bond markets, ESG integration, and climate risk assessment. Bloomberg serves as a key data provider for sustainable finance markets, offering green bond data, ESG scores, climate analytics, and impact measurement tools aligned with major regulatory frameworks including SFDR, EU Taxonomy, and TCFD.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-sustainable-finance-products/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Sustainable Finance
  - ESG
  - Green Bonds
  - Climate Risk
  - SFDR
  - EU Taxonomy
  - Bloomberg
apis:
  - aid: bloomberg-sustainable-finance-products:esg-data-api
    name: Bloomberg ESG Data API
    description: Access Bloomberg ESG scores, environmental KPIs, social metrics, and governance data for thousands of companies globally. Sourced from company disclosures and standardized for comparability across sectors and geographies.
    humanURL: https://www.bloomberg.com/professional/solution/esg-data/
    baseURL: blpapi://localhost:8194
    tags:
      - ESG
      - Environmental
      - Social
      - Governance
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/esg-data/
  - aid: bloomberg-sustainable-finance-products:green-bond-api
    name: Bloomberg Green Bond API
    description: Access comprehensive green, social, sustainability, and sustainability-linked bond data including use of proceeds, project categories, certifications, and post-issuance reporting aligned to ICMA Green Bond Principles.
    humanURL: https://www.bloomberg.com/professional/solution/sustainable-finance/
    baseURL: blpapi://localhost:8194
    tags:
      - Green Bonds
      - Social Bonds
      - Sustainability Bonds
      - ICMA
      - Fixed Income
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/sustainable-finance/
  - aid: bloomberg-sustainable-finance-products:climate-risk-api
    name: Bloomberg Climate Risk Data API
    description: Access physical climate risk scores, transition risk metrics, carbon emissions data, and TCFD-aligned analytics for companies and portfolios. Supports climate stress testing and scenario analysis.
    humanURL: https://www.bloomberg.com/professional/solution/climate-data/
    baseURL: blpapi://localhost:8194
    tags:
      - Climate Risk
      - Physical Risk
      - Transition Risk
      - TCFD
      - Carbon Emissions
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/climate-data/
  - aid: bloomberg-sustainable-finance-products:sfdr-api
    name: Bloomberg SFDR Data API
    description: Access Principal Adverse Indicators (PAIs) and other data points required for EU Sustainable Finance Disclosure Regulation (SFDR) reporting for investment products and portfolios.
    humanURL: https://www.bloomberg.com/professional/solution/regulatory-data/
    baseURL: blpapi://localhost:8194
    tags:
      - SFDR
      - PAI
      - Regulatory
      - EU Taxonomy
      - Disclosure
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/regulatory-data/
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
        description: Standardized ESG disclosure scores for thousands of public companies.
      - name: Green Bond Data
        description: Use of proceeds, certifications, and reporting data for green and social bonds.
      - name: Climate Risk Metrics
        description: Physical and transition climate risk scores and scenario analysis.
      - name: SFDR PAI Indicators
        description: Principal Adverse Indicators data for EU SFDR regulatory reporting.
      - name: EU Taxonomy Alignment
        description: Data on company revenue alignment with EU Taxonomy environmental objectives.
      - name: Impact Reporting
        description: Environmental and social impact metrics for sustainable investments.
  - type: UseCases
    data:
      - name: ESG Integration
        description: Integrate ESG data into investment analysis and portfolio construction.
      - name: SFDR Reporting
        description: Satisfy SFDR disclosure requirements for EU-domiciled investment products.
      - name: Green Bond Issuance
        description: Access market data and reporting frameworks for green bond issuance.
      - name: Climate Risk Disclosure
        description: Disclose TCFD-aligned climate risks in investment portfolios.
      - name: Impact Measurement
        description: Measure and report the environmental and social impact of investments.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
