---
aid: blackstone
url: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/apis.yml
name: Blackstone
description: Blackstone is the world's largest alternative asset manager with over $1 trillion in assets under management across private equity, real estate, credit, and hedge fund strategies. Blackstone serves institutional investors including pension funds, sovereign wealth funds, endowments, and foundations, as well as accredited individual investors through its private wealth solutions. Technology and data platforms are central to Blackstone's investment operations and portfolio company management.
tags:
  - Alternative Assets
  - Finance
  - Investment Management
  - Private Equity
  - Real Estate
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2026-03-21'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: blackstone:blackstone-investor-portal
    name: Blackstone Investor Portal
    description: Blackstone provides institutional and individual investors with access to portfolio information, capital account statements, fund documents, and reporting through its Investor Portal. API integrations may be available for institutional investors and data aggregation platforms under direct agreement with Blackstone.
    humanURL: https://www.blackstone.com/investor-resources/
    tags:
      - Alternative Assets
      - Finance
      - Investment Management
      - Private Equity
    properties:
      - type: Documentation
        url: https://www.blackstone.com/investor-resources/
      - type: Login
        url: https://investor.blackstone.com
      - type: JSONSchema
        url: json-schema/blackstone-fund-schema.json
      - type: JSONSchema
        url: json-schema/blackstone-investor-account-schema.json
      - type: JSONStructure
        url: json-structure/blackstone-fund-structure.json
      - type: JSONStructure
        url: json-structure/blackstone-investor-account-structure.json
      - type: JSONLD
        url: json-ld/blackstone-context.jsonld
      - type: Example
        url: examples/blackstone-fund-example.json
      - type: Example
        url: examples/blackstone-investor-account-example.json
common:
  - type: Website
    url: https://www.blackstone.com
  - type: Documentation
    url: https://www.blackstone.com/investor-resources/
  - type: Login
    url: https://investor.blackstone.com
  - type: TermsOfService
    url: https://www.blackstone.com/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.blackstone.com/privacy-policy/
  - type: Blog
    url: https://www.blackstone.com/insights/
  - type: SpectralRules
    url: rules/blackstone-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/blackstone-investor-portal.yaml
  - type: Vocabulary
    url: vocabulary/blackstone-vocabulary.yaml
  - type: Features
    data:
      - name: Investor Portal
        description: Web-based portal providing investors with access to fund performance, capital account statements, distributions, and investor documents.
      - name: Fund Reporting
        description: Quarterly and annual fund-level reporting including audited financials, NAV calculations, and investor-level P&L attribution.
      - name: Alternative Data Integration
        description: Blackstone's data science and technology teams develop proprietary data products and integrations to support portfolio company operations and investment research.
      - name: Portfolio Company Technology
        description: Blackstone actively supports portfolio companies in technology transformation, digital infrastructure buildout, and enterprise software adoption.
      - name: Capital Call and Distribution Notices
        description: Automated delivery of capital call and distribution notices to investors via the portal, email, and data feed integrations.
      - name: Tax Document Delivery
        description: Annual K-1 and other tax documents delivered electronically to limited partners through the Investor Portal.
  - type: UseCases
    data:
      - name: Institutional Investor Reporting
        description: Institutional LPs access fund reporting, capital call and distribution notices, and tax documents through the investor portal or via data integrations.
      - name: Portfolio Monitoring
        description: Blackstone's investment teams use proprietary data platforms to monitor portfolio company performance metrics, market signals, and risk indicators.
      - name: Data Aggregation
        description: Third-party data aggregators and institutional investor platforms may access Blackstone investor data via direct data feed agreements.
      - name: Wealth Management Distribution
        description: Registered investment advisors and wealth managers access Blackstone alternative products through platform integrations for accredited investor clients.
  - type: Integrations
    data:
      - name: iCapital Network
        description: Blackstone distributes alternative investments to wealth management clients through iCapital Network's feeder fund and technology platform.
      - name: CAIS
        description: Blackstone alternative investment products are available through the CAIS platform for independent and institutional advisors.
      - name: Yardi
        description: Blackstone Real Estate uses Yardi for property management, accounting, and data reporting across its real estate portfolio.
      - name: Allvue Systems
        description: Blackstone's credit and private equity operations use Allvue for portfolio monitoring, investor reporting, and fund accounting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
