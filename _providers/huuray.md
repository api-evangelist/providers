---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Huuray Agentic Access
  operation_count: 9
  slug: huuray-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 9
apis:
- description: The Balance API from Huuray — 1 operation(s) for balance.
  name: Huuray Balance API
  slug: huuray-balance-api
- description: The Cancel API from Huuray — 1 operation(s) for cancel.
  name: Huuray Cancel API
  slug: huuray-cancel-api
- description: The Catalogue API from Huuray — 1 operation(s) for catalogue.
  name: Huuray Catalogue API
  slug: huuray-catalogue-api
- description: The ExchangeRates API from Huuray — 1 operation(s) for exchangerates.
  name: Huuray ExchangeRates API
  slug: huuray-exchangerates-api
- description: The Order API from Huuray — 1 operation(s) for order.
  name: Huuray Order API
  slug: huuray-order-api
- description: The Resend API from Huuray — 1 operation(s) for resend.
  name: Huuray Resend API
  slug: huuray-resend-api
- description: The Search API from Huuray — 1 operation(s) for search.
  name: Huuray Search API
  slug: huuray-search-api
- description: The Stock API from Huuray — 1 operation(s) for stock.
  name: Huuray Stock API
  slug: huuray-stock-api
- description: The Template API from Huuray — 1 operation(s) for template.
  name: Huuray Template API
  slug: huuray-template-api
artifact_total: 16
collections:
- collection_type: open
  name: Huuray API
  slug: open-huuray
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/huuray-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huuray-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/huuray-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huuray-
- group: company
  title: ''
  type: Website
  url: https://huuray.com/
- group: docs
  title: ''
  type: Documentation
  url: https://huuray.com/solutions/developers-gift-card-api/
- group: docs
  title: ''
  type: SwaggerUI
  url: https://api.huuray.com/swagger/index.html
- group: company
  title: ''
  type: Blog
  url: https://huuray.com/inspiration/
created: '2025-02-08'
description: Huuray is a global gift card API platform that enables businesses to offer gift card buying and redemption without leaving their website. The platform allows businesses to quickly and easily send gifts without having to manage multiple accounts.
finops:
- name: Huuray Finops
  service_category: API
  slug: huuray-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huuray.png
layout: provider
modified: '2026-05-19'
name: Huuray
nav: Providers
network: true
overview: 'Huuray publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Cancel API, Catalogue API, and 6 more. Tagged areas include E-Commerce, Gift Cards, Payments, and Rewards.


  Huuray''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Huuray Plans Pricing
  plan_count: 3
  slug: huuray-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Huuray Rate Limits
  slug: huuray-rate-limits
score:
  band: thin
  composite: 32.8
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Huuray Authentication
  slug: huuray-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Huuray Domain Security
  slug: huuray-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huuray
tags:
- E-Commerce
- Gift Cards
- Payments
- Rewards
website: https://huuray.com/
---
