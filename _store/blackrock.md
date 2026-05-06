---
aid: blackrock
url: https://raw.githubusercontent.com/api-evangelist/blackrock/refs/heads/main/apis.yml
name: BlackRock
description: BlackRock is the world's largest asset manager with over $10 trillion in assets under management. Through its Aladdin platform, BlackRock provides institutional investors, wealth managers, and financial services firms with risk analytics, portfolio management, and data capabilities via APIs. The Aladdin platform powers investment operations for many of the world's largest pension funds, insurers, and asset managers.
tags:
  - Asset Management
  - Finance
  - FinTech
  - Investment Management
  - Portfolio Management
  - Risk Analytics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2026-03-21'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: blackrock:aladdin-api
    name: BlackRock Aladdin API
    description: The Aladdin Developer program provides APIs that enable clients to access BlackRock's Aladdin platform capabilities programmatically. Aladdin APIs support portfolio analytics, risk reporting, data access, order management, and workflow automation for institutional asset managers, wealth managers, and financial services clients.
    humanURL: https://www.blackrock.com/aladdin/products/aladdin-developer
    tags:
      - Asset Management
      - Finance
      - Portfolio Management
      - Risk Analytics
    properties:
      - type: Documentation
        url: https://www.blackrock.com/aladdin/products/aladdin-developer
      - type: SDK
        url: https://github.com/blackrock/aladdinsdk
        title: Python SDK (AladdinSDK)
      - type: JSONSchema
        url: json-schema/blackrock-portfolio-schema.json
      - type: JSONSchema
        url: json-schema/blackrock-risk-report-schema.json
      - type: JSONStructure
        url: json-structure/blackrock-portfolio-structure.json
      - type: JSONStructure
        url: json-structure/blackrock-risk-report-structure.json
      - type: JSONLD
        url: json-ld/blackrock-context.jsonld
      - type: Example
        url: examples/blackrock-portfolio-example.json
      - type: Example
        url: examples/blackrock-risk-report-example.json
common:
  - type: Website
    url: https://www.blackrock.com
  - type: Documentation
    url: https://www.blackrock.com/aladdin/products/aladdin-developer
  - type: GitHubOrganization
    url: https://github.com/blackrock
  - type: TermsOfService
    url: https://www.blackrock.com/us/individual/regulatory/privacy-policy
  - type: PrivacyPolicy
    url: https://www.blackrock.com/us/individual/regulatory/privacy-policy
  - type: Blog
    url: https://www.blackrock.com/us/individual/insights
  - type: SpectralRules
    url: rules/blackrock-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/blackrock-aladdin.yaml
  - type: Vocabulary
    url: vocabulary/blackrock-vocabulary.yaml
  - type: Features
    data:
      - name: Aladdin Risk Analytics
        description: Multi-asset risk measurement and attribution capabilities accessible via API, including VaR, factor exposures, stress testing, and scenario analysis.
      - name: Portfolio Management APIs
        description: APIs for portfolio construction, optimization, rebalancing, and compliance monitoring integrated with the Aladdin operating system.
      - name: Data Access Layer
        description: Structured access to market data, security reference data, and portfolio data via RESTful APIs with enterprise data governance.
      - name: Order Management System Integration
        description: APIs for trade order management, execution, and settlement workflows integrating with OMS and EMS systems.
      - name: AladdinSDK
        description: Open-source Python SDK providing programmatic access to Aladdin APIs with authentication, pagination, and data transformation utilities.
      - name: Workflow Automation
        description: Event-driven workflow APIs enabling clients to automate investment operations processes and integrate with third-party systems.
  - type: UseCases
    data:
      - name: Institutional Risk Reporting
        description: Institutional investors use Aladdin APIs to generate regulatory risk reports, UCITS compliance reports, and investor disclosures.
      - name: Portfolio Analytics Integration
        description: Wealth managers and RIAs integrate Aladdin risk analytics into their own client-facing and advisor-facing platforms.
      - name: Fintech Data Integration
        description: FinTech companies access structured investment data through Aladdin APIs to power analytics, research, and advisory products.
      - name: Automated Rebalancing
        description: Portfolio managers automate rebalancing workflows using Aladdin APIs to trigger trades based on drift thresholds and target allocations.
      - name: Multi-Manager Aggregation
        description: Family offices and fund-of-funds use Aladdin APIs to aggregate portfolio data across multiple managers into a single risk view.
  - type: Integrations
    data:
      - name: Charles River Development
        description: Aladdin integrates with Charles River IMS for order management and compliance workflow automation.
      - name: SimCorp Dimension
        description: Integration between Aladdin risk analytics and SimCorp's portfolio management and accounting systems.
      - name: Bloomberg
        description: Market data and analytics integrations with Bloomberg Data License and Bloomberg PORT for risk and performance.
      - name: Refinitiv
        description: Security master data and market data integrations with Refinitiv Datascope and Eikon platforms.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
