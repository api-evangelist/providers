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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Huuray Agentic Access
  operation_count: 9
  slug: huuray-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
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
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Huuray Balance API
  slug: open-huuray-balance-api
- collection_type: open
  name: Huuray Balance Cancel API
  slug: open-huuray-cancel-api
- collection_type: open
  name: Huuray Balance Catalogue API
  slug: open-huuray-catalogue-api
- collection_type: open
  name: Huuray Balance ExchangeRates API
  slug: open-huuray-exchangerates-api
- collection_type: open
  name: Huuray Balance Order API
  slug: open-huuray-order-api
- collection_type: open
  name: Huuray Balance Resend API
  slug: open-huuray-resend-api
- collection_type: open
  name: Huuray Balance Search API
  slug: open-huuray-search-api
- collection_type: open
  name: Huuray Balance Stock API
  slug: open-huuray-stock-api
- collection_type: open
  name: Huuray Balance Template API
  slug: open-huuray-template-api
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
random_paper: 19
rate_limits:
- limit_count: 5
  name: Huuray Rate Limits
  slug: huuray-rate-limits
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huuray/refs/heads/main/screenshots/huuray-2026-08-07T182120.png
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
