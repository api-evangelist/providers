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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Okra Africa Agentic Access
  operation_count: 30
  slug: okra-africa-agentic-access
  summary_line: 30 operations · 30 acting
api_count: 12
apis:
- description: Bank accounts a customer has linked.
  name: Okra Accounts API
  slug: okra-africa-accounts-api
- description: Authentication data for linked bank accounts.
  name: Okra Auth API
  slug: okra-africa-auth-api
- description: Real-time and cached account balances.
  name: Okra Balance API
  slug: okra-africa-balance-api
- description: Reference list of connectable banks.
  name: Okra Banks API
  slug: okra-africa-banks-api
- description: End-user (customer) management.
  name: Okra Customers API
  slug: okra-africa-customers-api
- description: Verified identity profiles.
  name: Okra Identity API
  slug: okra-africa-identity-api
- description: Income and affordability signals.
  name: Okra Income API
  slug: okra-africa-income-api
- description: Bank-to-bank payments and direct-debit authorizations.
  name: Okra Payments API
  slug: okra-africa-payments-api
- description: Scheduled financial reports.
  name: Okra Reports API
  slug: okra-africa-reports-api
- description: Categorized transaction history.
  name: Okra Transactions API
  slug: okra-africa-transactions-api
- description: Nigerian KYC checks (BVN, NUBAN, TIN, RC).
  name: Okra Verification API
  slug: okra-africa-verification-api
- description: Billing wallet used to fund API usage.
  name: Okra Wallet API
  slug: okra-africa-wallet-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Okra API (Historical) Accounts API
  slug: open-okra-africa-accounts-api
- collection_type: open
  name: Okra API (Historical) Accounts Auth API
  slug: open-okra-africa-auth-api
- collection_type: open
  name: Okra API (Historical) Accounts Balance API
  slug: open-okra-africa-balance-api
- collection_type: open
  name: Okra API (Historical) Accounts Banks API
  slug: open-okra-africa-banks-api
- collection_type: open
  name: Okra API (Historical) Accounts Customers API
  slug: open-okra-africa-customers-api
- collection_type: open
  name: Okra API (Historical) Accounts Identity API
  slug: open-okra-africa-identity-api
- collection_type: open
  name: Okra API (Historical) Accounts Income API
  slug: open-okra-africa-income-api
- collection_type: open
  name: Okra API (Historical) Accounts Payments API
  slug: open-okra-africa-payments-api
- collection_type: open
  name: Okra API (Historical) Accounts Reports API
  slug: open-okra-africa-reports-api
- collection_type: open
  name: Okra API (Historical) Accounts Transactions API
  slug: open-okra-africa-transactions-api
- collection_type: open
  name: Okra API (Historical) Accounts Verification API
  slug: open-okra-africa-verification-api
- collection_type: open
  name: Okra API (Historical) Accounts Wallet API
  slug: open-okra-africa-wallet-api
- collection_type: open
  name: Okra API (Historical)
  slug: open-okra-africa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/okra-africa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/okra-africa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/okra-africa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okraHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/okrafinance
- group: company
  title: ''
  type: Website
  url: https://okra.ng
- group: docs
  title: ''
  type: Documentation
  url: https://web.archive.org/web/20240418181836/https://docs.okra.ng/reference/api
- group: commercial
  title: ''
  type: Plans
  url: plans/okra-africa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/okra-africa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/okra-africa-finops.yml
created: '2026-07-12'
description: 'Okra was an open finance / open banking infrastructure company for Africa, headquartered in Lagos, Nigeria. Its REST APIs let businesses link end users'' bank accounts (via the Okra Widget and a per-record "record" object) and then retrieve authenticated banking data - account and identity details, real-time balances, transaction history, and income - plus run KYC verifications (BVN, NUBAN, TIN, RC) and move money through bank-to-bank payments and direct debit authorizations. RETIRED: Okra quietly ceased operations in May 2025 and wound the company down; the API hosts (api.okra.ng, dash.okra.ng, docs.okra.ng, identity-api.okra.ng) no longer resolve and the okra.ng domain now serves an unrelated parked page. This entry documents the historical, now-discontinued API surface, grounded in Okra''s official okraHQ/okra-node SDK and archived documentation.'
finops:
- name: Okra Africa Finops
  service_category: Financial Data and Payments
  slug: okra-africa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/okra-africa.png
layout: provider
modified: '2026-07-12'
name: Okra
nav: Providers
network: true
overview: 'Okra publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Balance API, and 9 more. Tagged areas include Open Banking, Open Finance, Financial Data, Payments, and Fintech.


  Okra''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Okra Africa Plans Pricing
  plan_count: 4
  slug: okra-africa-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: Okra Africa Rate Limits
  slug: okra-africa-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/okra-africa/refs/heads/main/screenshots/okra-africa-2026-08-07T190057.png
security:
- kind: authentication
  name: Okra Africa Authentication
  slug: okra-africa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Okra Africa Domain Security
  slug: okra-africa-domain-security
  summary_line: no transport/DNS hardening detected
slug: okra-africa
tags:
- Open Banking
- Open Finance
- Financial Data
- Payments
- Fintech
- Account Linking
- Bank Data
- Africa
- Nigeria
- Financial Infrastructure
- Retired
website: https://okra.ng
---
