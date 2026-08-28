---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'Relationship-based, partner-onboarded API and integration options for treasury and ERP connectivity — including ConnectNow embedded banking for Sage and NetSuite, direct platform integrations, custom '
  name: Texas Capital Bank Treasury & ERP Integration APIs
  slug: treasury-erp-integration
- description: Consumer-permissioned account and transaction data is made available to third parties through the Finicity (Mastercard) data aggregator rather than a first-party Texas Capital Bank API. This is the ho
  name: Consumer Data Access (Aggregator)
  slug: consumer-data-access
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/texas-capital-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://texascapitalbank.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/texas-capital-bank
- group: company
  title: ''
  type: Blog
  url: https://texascapitalbank.com/insights
- group: operate
  title: ''
  type: Support
  url: https://www.texascapitalbank.com/helpful-information/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://texascapitalbank.com/online-privacy-policy-url
created: '2026-07-23'
description: 'Texas Capital Bank, National Association is the banking subsidiary of Texas Capital Bancshares, Inc. (NASDAQ: TCBI), a Dallas-headquartered full-service financial services firm founded in 1998 with roughly $31.5 billion in assets (FYE 2025). As a nationally chartered commercial bank it serves businesses, entrepreneurs, and institutions across Texas and the United States with commercial and business banking, treasury management, mortgage/warehouse finance, and investment banking. On the open-finance dimension the bank is relationship-first rather than developer-first: it markets treasury and ERP API integrations (including its ConnectNow embedded banking for Sage and NetSuite, direct platform integrations, and SFTP/XChange file transfer) but exposes them through partner onboarding with dedicated bankers, not a public self-serve developer portal. There is no public first-party developer portal, no downloadable OpenAPI/Swagger, and no self-serve API signup. Consumer account and
  transaction data is made available to permissioned third parties through the Finicity (Mastercard) aggregator rather than a first-party API, which is the honest posture for most US regional banks under the voluntary, fragmented US open-banking landscape (CFPB Section 1033 and the industry FDX standard).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Texas Capital Bank
nav: Providers
network: true
overview: 'Texas Capital Bank publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Commercial Banking, and Treasury Management.


  Texas Capital Bank''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.6
  delta: 1.9
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Texas Capital Bank Domain Security
  slug: texas-capital-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: texas-capital-bank
tags:
- Financial-Services
- Banking
- United States
- Commercial Banking
- Treasury Management
- Regional Bank
- Open Finance
- Data Aggregation
website: https://texascapitalbank.com/
---
