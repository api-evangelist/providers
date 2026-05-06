---
aid: state-street
url: https://raw.githubusercontent.com/api-evangelist/state-street/refs/heads/main/apis.yml
modified: '2026-05-02'
name: State Street
description: State Street Corporation is one of the world's largest financial services companies, headquartered in Boston, Massachusetts. Founded in 1792, State Street provides investment servicing, investment management, investment research, and trading services to institutional investors including mutual funds, collective investment funds, corporate and public retirement plans, insurance companies, foundations, and endowments. State Street manages approximately $4.7 trillion in assets under management through State Street Global Advisors and services nearly $40 trillion in assets under custody. The company operates the State Street Alpha front-to-back investment management platform, Fund Connect for ETF creation and redemption, and Charles River Development for investment management technology. State Street's developer portal at developer.statestreet.com provides OAuth 2.0-secured APIs enabling institutional clients to programmatically access portfolio data, transaction history, NAV calculations, analytics, and ETF order management. APIs follow REST conventions with OpenAPI 3.0 specifications, JSON data format, and JSON Schema documentation.
apis:
  - aid: state-street:alpha-data-platform-api
    name: Alpha Data Platform API
    description: The State Street Alpha Data Platform API provides institutional investment managers with programmatic access to the front-to-back Alpha investment management platform. Clients can retrieve portfolio holdings, positions, investable cash, pledged collateral, securities on loan, risk exposures, performance measurement, and transaction history in near real-time. Built on Snowflake and Microsoft Azure, the Alpha Data Platform enables intraday visibility across geographies, asset classes, and counterparties. Authentication uses OAuth 2.0 Client Credentials.
    humanURL: https://developer.statestreet.com/api-overview
    baseURL: https://api.statestreet.com/v1
    tags:
      - Financial Services
      - Investment Management
      - Portfolio
      - Data Platform
      - Institutional
    properties:
      - type: Documentation
        url: https://developer.statestreet.com/documentation-usage
      - type: OpenAPI
        url: openapi/state-street-alpha-data-platform-openapi.yml
  - aid: state-street:fund-connect-api
    name: Fund Connect API
    description: The State Street Fund Connect API enables authorized participants (APs), fund managers, and custodians to programmatically manage ETF creation and redemption orders through the Fund Connect platform. The API supports FIX protocol and XML for order submission, and has executed the first API-based ETF order in Australian-domiciled ETFs (2025). Fund Connect is a global online portal processing ETF transactions across major markets.
    humanURL: https://developer.statestreet.com/
    baseURL: https://api.statestreet.com/v1/fund-connect
    tags:
      - Financial Services
      - ETF
      - Fund Management
      - Order Management
      - Institutional
    properties:
      - type: Documentation
        url: https://developer.statestreet.com/
      - type: OpenAPI
        url: openapi/state-street-fund-connect-openapi.yml
  - aid: state-street:investment-accounting-api
    name: Investment Accounting API
    description: The State Street Investment Accounting API provides institutional clients with access to portfolio accounting data including net asset value (NAV) calculations, position valuations, corporate actions processing, performance measurement, and attribution analysis. State Street services over 70 types of portfolios including mutual funds, insurance portfolios, alternatives, and pension funds.
    humanURL: https://www.statestreet.com/us/en/solutions/investment-accounting
    baseURL: https://api.statestreet.com/v1/accounting
    tags:
      - Financial Services
      - Accounting
      - NAV
      - Performance
      - Institutional
    properties:
      - type: Documentation
        url: https://developer.statestreet.com/documentation-usage
  - aid: state-street:performance-analytics-api
    name: Performance Analytics API
    description: The State Street Performance Analytics API (TrueView) provides institutional investors and asset managers with access to investment risk analytics, performance attribution, scenario analysis, and reporting. Enables portfolio managers to access benchmark-relative attribution, risk factor decomposition, and regulatory reporting data across all asset classes including fixed income, equities, derivatives, and alternatives.
    humanURL: https://www.statestreet.com/us/en/asset-owner/solutions/performance-and-analytics
    baseURL: https://api.statestreet.com/v1/analytics
    tags:
      - Financial Services
      - Analytics
      - Performance
      - Risk
      - Institutional
    properties:
      - type: Documentation
        url: https://developer.statestreet.com/documentation-usage
  - aid: state-street:sample-transactions-api
    name: Sample Transactions API
    description: The State Street Sample Transactions API is a reference and onboarding API provided in the developer portal to help new integration teams understand the authentication flow, request structure, and response format of State Street's API platform. Developers use this API to perform an initial successful API call and retrieve a sample dataset before progressing to production APIs.
    humanURL: https://developer.statestreet.com/get-started-browser
    baseURL: https://api.statestreet.com/v1
    tags:
      - Financial Services
      - Developer
      - Reference
      - Onboarding
      - Sample
    properties:
      - type: Documentation
        url: https://developer.statestreet.com/get-started-browser
common:
  - type: Website
    url: https://www.statestreet.com
  - type: Developer Portal
    url: https://developer.statestreet.com
  - type: API Catalog
    url: https://developer.statestreet.com/apis-list
  - type: API Overview
    url: https://developer.statestreet.com/api-overview
  - type: Documentation
    url: https://developer.statestreet.com/documentation-usage
  - type: API Standards
    url: https://developer.statestreet.com/api-platform-standards
  - type: Getting Started
    url: https://developer.statestreet.com/get-started-browser
  - type: Support
    url: mailto:api-support@statestreet.com
  - type: LinkedIn
    url: https://www.linkedin.com/company/state-street-corporation
  - type: Twitter
    url: https://twitter.com/StateStreet
  - type: Alpha Platform
    url: https://www.statestreet.com/alpha
  - type: Privacy Policy
    url: https://www.statestreet.com/us/en/individual-investor/tools-and-resources/privacy-notice
  - type: Terms of Service
    url: https://www.statestreet.com/us/en/individual-investor/tools-and-resources/terms-and-conditions
  - type: OpenAPI
    url: openapi/state-street-alpha-data-platform-openapi.yml
  - type: OpenAPI
    url: openapi/state-street-fund-connect-openapi.yml
  - type: JSONSchema
    url: json-schema/state-street-portfolio-schema.json
  - type: JSONSchema
    url: json-schema/state-street-position-schema.json
  - type: JSONStructure
    url: json-structure/state-street-portfolio-structure.json
  - type: JSONLD
    url: json-ld/state-street-context.jsonld
  - type: Vocabulary
    url: vocabulary/state-street-vocabulary.yml
  - type: SpectralRules
    url: rules/state-street-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/portfolio-management.yaml
---
