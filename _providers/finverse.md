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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: 'Retrieve real-time financial account information with user consent from over 40 Asian banks. Returns key financial data including real-time account balances, transaction and balance history for up to '
  name: Finverse Bank Data API
  slug: bank-data-api
- description: Automate bank payment collection in Hong Kong and Singapore. Enable customers to pay directly from their bank accounts, cutting transaction fees by up to 85%. Supports payment links, mandates, and dir
  name: Finverse Collect API
  slug: payments-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finverse-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finversetech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finverse
- group: company
  title: ''
  type: Website
  url: https://www.finverse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finverse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.finverse.com
- group: operate
  title: ''
  type: Support Email
  url: mailto:support@finverse.com
- group: other
  title: ''
  type: Payment Links
  url: https://www.finverse.com/payment-links
- group: company
  title: ''
  type: Blog
  url: https://www.finverse.com/blog
created: '2026-03-26'
description: Finverse is a unified open finance API platform providing aggregated access to banking data, payments, and financial services across Asia-Pacific. Often described as the Plaid for Asia, it connects to over 40 banks across Hong Kong, Singapore, Philippines, Vietnam, and other Southeast Asian markets.
finops:
- name: Finverse Finops
  service_category: API
  slug: finverse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finverse.png
layout: provider
modified: '2026-04-28'
name: Finverse
nav: Providers
network: true
overview: 'Finverse publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Aggregation, Asia Pacific, Financial Data, Open Banking, and Open Finance.


  Finverse''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Finverse Plans Pricing
  plan_count: 3
  slug: finverse-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Finverse Rate Limits
  slug: finverse-rate-limits
score:
  band: emerging
  composite: 13.7
  delta: -6.6
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/finverse/refs/heads/main/screenshots/finverse-2026-06-20T181225.png
security:
- kind: domain-security
  name: Finverse Domain Security
  slug: finverse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: finverse
tags:
- API Aggregation
- Asia Pacific
- Financial Data
- Open Banking
- Open Finance
- Payments
- Unified API
website: https://www.finverse.com
---
