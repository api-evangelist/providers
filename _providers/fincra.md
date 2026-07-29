---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Fincra Agentic Access
  operation_count: 23
  slug: fincra-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 8
apis:
- description: The Account Resolution API from Fincra — 1 operation(s) for account resolution.
  name: Fincra Account Resolution API
  slug: fincra-account-resolution-api
- description: The Banks API from Fincra — 1 operation(s) for banks.
  name: Fincra Banks API
  slug: fincra-banks-api
- description: The Beneficiaries API from Fincra — 2 operation(s) for beneficiaries.
  name: Fincra Beneficiaries API
  slug: fincra-beneficiaries-api
- description: The Collections API from Fincra — 4 operation(s) for collections.
  name: Fincra Collections API
  slug: fincra-collections-api
- description: The Conversions API from Fincra — 3 operation(s) for conversions.
  name: Fincra Conversions API
  slug: fincra-conversions-api
- description: The Payouts API from Fincra — 3 operation(s) for payouts.
  name: Fincra Payouts API
  slug: fincra-payouts-api
- description: The Quotes API from Fincra — 1 operation(s) for quotes.
  name: Fincra Quotes API
  slug: fincra-quotes-api
- description: The Virtual Accounts API from Fincra — 4 operation(s) for virtual accounts.
  name: Fincra Virtual Accounts API
  slug: fincra-virtual-accounts-api
artifact_total: 15
collections:
- collection_type: open
  name: Fincra API
  slug: open-fincra
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fincra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fincra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fincra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fincra
- group: company
  title: ''
  type: Website
  url: https://www.fincra.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fincra.com
- group: commercial
  title: ''
  type: Plans
  url: plans/fincra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fincra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fincra-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.fincra.com/feed/
created: '2026-06-21'
description: Fincra is an African cross-border payments infrastructure provider whose REST API lets businesses collect, hold, convert, and disburse money across multiple currencies. The platform covers collections (virtual accounts and direct charges), payouts/disbursements to banks and mobile money, FX conversions with quotes, beneficiary management, and webhooks, secured with an api-key plus Bearer token.
finops:
- name: Fincra Finops
  service_category: Payments and Financial Services
  slug: fincra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fincra.png
layout: provider
modified: '2026-06-21'
name: Fincra
nav: Providers
network: true
overview: 'Fincra publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account Resolution API, Banks API, Beneficiaries API, and 5 more. Tagged areas include Payments, Cross-Border, Collections, Payouts, and FX.


  Fincra''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Fincra Plans Pricing
  plan_count: 2
  slug: fincra-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 3
  name: Fincra Rate Limits
  slug: fincra-rate-limits
score:
  band: thin
  composite: 33.2
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fincra/refs/heads/main/screenshots/fincra-2026-07-25T214519.png
security:
- kind: authentication
  name: Fincra Authentication
  slug: fincra-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fincra Domain Security
  slug: fincra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fincra
tags:
- Payments
- Cross-Border
- Collections
- Payouts
- FX
- Fintech
- Africa
website: https://www.fincra.com
---
