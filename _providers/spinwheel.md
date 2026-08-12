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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Spinwheel Agentic Access
  operation_count: 36
  slug: spinwheel-agentic-access
  summary_line: 36 operations · 24 acting
api_count: 7
apis:
- description: Add and manage user bank accounts.
  name: Spinwheel Bank Accounts API
  slug: spinwheel-bank-accounts-api
- description: Order and retrieve Equifax-backed debt profiles and credit reports.
  name: Spinwheel Credit Data API
  slug: spinwheel-credit-data-api
- description: Request, poll, and update liability data and refresh subscriptions.
  name: Spinwheel Liabilities API
  slug: spinwheel-liabilities-api
- description: Manage payment requests, payers, and transactions.
  name: Spinwheel Payments API
  slug: spinwheel-payments-api
- description: Constants and vehicle reference data.
  name: Spinwheel Reference API
  slug: spinwheel-reference-api
- description: Connect and manage users via SMS, KBA, phone, profile, or network token.
  name: Spinwheel Users API
  slug: spinwheel-users-api
- description: Register and manage webhook endpoints.
  name: Spinwheel Webhooks API
  slug: spinwheel-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Spinwheel Embedded Debt Solutions API
  slug: open-spinwheel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spinwheel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spinwheel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spinwheel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spinwheel
- group: company
  title: ''
  type: Website
  url: https://www.spinwheel.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spinwheel.io
- group: commercial
  title: ''
  type: Plans
  url: plans/spinwheel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spinwheel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spinwheel-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.spinwheel.io/blog
created: '2026-06-20'
description: Spinwheel is an embedded credit and debt data platform. Its REST API and drop-in modules connect a consumer (via SMS, KBA, phone, or network token), pull an Equifax-backed debt profile across credit cards, student, auto, home, and personal loans, refresh real-time liability balances and payoff quotes, and originate bank-account-funded payments - all surfaced to partners as user-scoped endpoints and webhook events.
finops:
- name: Spinwheel Finops
  service_category: Financial Services
  slug: spinwheel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spinwheel.png
layout: provider
modified: '2026-06-20'
name: Spinwheel
nav: Providers
network: true
overview: 'Spinwheel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Credit Data API, Liabilities API, and 4 more. Tagged areas include Fintech, Credit Data, Debt, Liabilities, and Payments.


  Spinwheel''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Spinwheel Plans Pricing
  plan_count: 2
  slug: spinwheel-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Spinwheel Rate Limits
  slug: spinwheel-rate-limits
score:
  band: thin
  composite: 32.6
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spinwheel/refs/heads/main/screenshots/spinwheel-2026-06-20T194318.png
security:
- kind: authentication
  name: Spinwheel Authentication
  slug: spinwheel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spinwheel Domain Security
  slug: spinwheel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spinwheel
tags:
- Fintech
- Credit Data
- Debt
- Liabilities
- Payments
- Embedded Finance
website: https://www.spinwheel.io
---
