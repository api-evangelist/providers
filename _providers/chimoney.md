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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Chimoney Agentic Access
  operation_count: 52
  slug: chimoney-agentic-access
  summary_line: 52 operations · 39 acting
api_count: 9
apis:
- description: Retrieve transactions, public profiles, transfer between accounts, and issue wallet addresses.
  name: Chimoney Account API
  slug: chimoney-account-api
- description: 'Reference lookups: supported banks, assets, exchange rates, currency conversion, and bank account verification.'
  name: Chimoney Info API
  slug: chimoney-info-api
- description: The Interledger API from Chimoney — 5 operation(s) for interledger.
  name: Chimoney Interledger API
  slug: chimoney-interledger-api
- description: Create and manage multicurrency wallets and transfer between them.
  name: Chimoney MultiCurrency Wallets API
  slug: chimoney-multicurrency-wallets-api
- description: Initiate and verify inbound payment (collection) requests.
  name: Chimoney Payments API
  slug: chimoney-payments-api
- description: Send money to banks, mobile money, airtime, gift cards, Chimoney wallets, Interac, and Interledger wallet addresses.
  name: Chimoney Payouts API
  slug: chimoney-payouts-api
- description: Redeem issued Chimoney, airtime, gift cards, and mobile money.
  name: Chimoney Redeem API
  slug: chimoney-redeem-api
- description: Create and manage sub-accounts (wallet accounts) and communities under your organization.
  name: Chimoney SubAccount API
  slug: chimoney-subaccount-api
- description: List, look up, and transfer between Chimoney wallets.
  name: Chimoney Wallet API
  slug: chimoney-wallet-api
artifact_total: 16
collections:
- collection_type: open
  name: Chimoney API
  slug: open-chimoney
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chimoney-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chimoney-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chimoney-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chimoney
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chimoney
- group: company
  title: ''
  type: Website
  url: https://chimoney.io
- group: docs
  title: ''
  type: Documentation
  url: https://chimoney.readme.io
- group: commercial
  title: ''
  type: Plans
  url: plans/chimoney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chimoney-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chimoney-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://chimoney.io/blogs
created: '2026-07-12'
description: Chimoney is a developer-first global payouts and disbursement platform with deep coverage across Africa and 130+ countries. Its REST API sends money to bank accounts, mobile money wallets, airtime, gift cards, Chimoney wallets, and Interledger wallet addresses, and manages multicurrency wallets, sub-accounts, redemption, inbound payment collection, and reference lookups (supported banks, assets, exchange rates). Authentication is an API key passed in the X-API-KEY header, issued self-serve from the Chimoney developer dashboard, with a separate sandbox host for testing.
finops:
- name: Chimoney Finops
  service_category: Payments and Money Movement
  slug: chimoney-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chimoney.png
layout: provider
modified: '2026-07-12'
name: Chimoney
nav: Providers
network: true
overview: 'Chimoney publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Info API, Interledger API, and 6 more. Tagged areas include Payouts, Disbursements, Payments, Africa, and Global Payouts.


  Chimoney''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chimoney Plans Pricing
  plan_count: 3
  slug: chimoney-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Chimoney Rate Limits
  slug: chimoney-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chimoney/refs/heads/main/screenshots/chimoney-2026-07-25T205233.png
security:
- kind: authentication
  name: Chimoney Authentication
  slug: chimoney-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chimoney Domain Security
  slug: chimoney-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chimoney
tags:
- Payouts
- Disbursements
- Payments
- Africa
- Global Payouts
- Wallets
- Multicurrency
- Gift Cards
- Mobile Money
- Fintech
website: https://chimoney.io
---
