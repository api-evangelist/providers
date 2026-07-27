---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: Access Bloomberg ESG scores, environmental KPIs, social metrics, and governance data for thousands of companies globally. Sourced from company disclosures and standardized for comparability across sec
  name: Bloomberg ESG Data API
  slug: esg-data-api
- description: Access comprehensive green, social, sustainability, and sustainability-linked bond data including use of proceeds, project categories, certifications, and post-issuance reporting aligned to ICMA Green
  name: Bloomberg Green Bond API
  slug: green-bond-api
- description: Access physical climate risk scores, transition risk metrics, carbon emissions data, and TCFD-aligned analytics for companies and portfolios. Supports climate stress testing and scenario analysis.
  name: Bloomberg Climate Risk Data API
  slug: climate-risk-api
- description: Access Principal Adverse Indicators (PAIs) and other data points required for EU Sustainable Finance Disclosure Regulation (SFDR) reporting for investment products and portfolios.
  name: Bloomberg SFDR Data API
  slug: sfdr-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-sustainable-finance-products-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Sustainable Finance Products provide comprehensive data, analytics, and tools for sustainable investing, green bond markets, ESG integration, and climate risk assessment. Bloomberg serves as a key data provider for sustainable finance markets, offering green bond data, ESG scores, climate analytics, and impact measurement tools aligned with major regulatory frameworks including SFDR, EU Taxonomy, and TCFD.
features:
- description: Standardized ESG disclosure scores for thousands of public companies.
  name: ESG Scores
- description: Use of proceeds, certifications, and reporting data for green and social bonds.
  name: Green Bond Data
- description: Physical and transition climate risk scores and scenario analysis.
  name: Climate Risk Metrics
- description: Principal Adverse Indicators data for EU SFDR regulatory reporting.
  name: SFDR PAI Indicators
- description: Data on company revenue alignment with EU Taxonomy environmental objectives.
  name: EU Taxonomy Alignment
- description: Environmental and social impact metrics for sustainable investments.
  name: Impact Reporting
finops:
- name: Bloomberg Sustainable Finance Products Finops
  service_category: API
  slug: bloomberg-sustainable-finance-products-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-sustainable-finance-products.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Sustainable Finance Products
nav: Providers
network: true
overview: 'Bloomberg Sustainable Finance Products publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sustainable Finance, ESG, Green Bonds, Climate Risk, and SFDR.


  Bloomberg Sustainable Finance Products'' developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Sustainable Finance Products Plans Pricing
  plan_count: 3
  slug: bloomberg-sustainable-finance-products-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Bloomberg Sustainable Finance Products Rate Limits
  slug: bloomberg-sustainable-finance-products-rate-limits
score:
  band: emerging
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-sustainable-finance-products/refs/heads/main/screenshots/bloomberg-sustainable-finance-products-2026-06-20T173508.png
security:
- kind: domain-security
  name: Bloomberg Sustainable Finance Products Domain Security
  slug: bloomberg-sustainable-finance-products-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-sustainable-finance-products
tags:
- Sustainable Finance
- ESG
- Green Bonds
- Climate Risk
- SFDR
- EU Taxonomy
- Bloomberg
use_cases:
- description: Integrate ESG data into investment analysis and portfolio construction.
  name: ESG Integration
- description: Satisfy SFDR disclosure requirements for EU-domiciled investment products.
  name: SFDR Reporting
- description: Access market data and reporting frameworks for green bond issuance.
  name: Green Bond Issuance
- description: Disclose TCFD-aligned climate risks in investment portfolios.
  name: Climate Risk Disclosure
- description: Measure and report the environmental and social impact of investments.
  name: Impact Measurement
website: https://www.bloomberg.com/professional/
---
