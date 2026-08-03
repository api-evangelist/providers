---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Commerce Bank's corporate API program, published through a registration-gated external developer portal and the CommercePayments developer platform, covering payments, treasury, and embedded-banking i
  name: Commerce Bank Developer APIs
  slug: commerce-developer-apis
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commerce-bancshares-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commercebank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.commercebank.com/
- group: company
  title: ''
  type: Blog
  url: https://www.commercebank.com/business/trends-and-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commercebank.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commercebank.com/security-center/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://www.commercebank.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commerce_bank
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commerce-bancshares-llms.txt
created: '2026-07-23'
description: 'Commerce Bank is the principal banking subsidiary of Commerce Bancshares, Inc. (NASDAQ CBSH), a Missouri-based regional bank holding company with roughly $32 billion in assets and dual headquarters in Kansas City and St. Louis. Commerce Bank is a Missouri state-chartered bank and Federal Reserve member, founded in 1865, offering personal, business, commercial, and wealth-management services across the U.S. Midwest. Its API posture is corporate/embedded-banking oriented rather than a fully open public program: it runs a registration-gated external developer portal (developers.commercebank.com) and a CommercePayments developer platform, and delivers ERP-embedded banking via Commerce Connections Direct. Consumer-permissioned data sharing is largely intermediated through aggregators such as Plaid and platforms like Modern Treasury rather than a documented first-party, self-serve open-banking API. No public FDX or CFPB Section 1033 data-access posture is documented, and no downloadable
  OpenAPI/Swagger is publicly available.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Commerce Bank
nav: Providers
network: true
overview: 'Commerce Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Regional Bank, and Payments.


  Commerce Bank''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commerce-bancshares/refs/heads/main/screenshots/commerce-bancshares-2026-07-25T210127.png
security:
- kind: domain-security
  name: Commerce Bancshares Domain Security
  slug: commerce-bancshares-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commerce-bancshares
tags:
- Financial Services
- Banking
- United States
- Regional Bank
- Payments
- Treasury Management
- Embedded Banking
- Open Finance
- Data Aggregation
website: https://www.commercebank.com/
---
