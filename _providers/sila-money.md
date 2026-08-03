---
access_model:
  confidence: high
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Sila Money Agentic Access
  operation_count: 19
  slug: sila-money-agentic-access
  summary_line: 19 operations · 19 acting
api_count: 6
apis:
- description: Sila's Virtual Accounts product issues each user a dedicated account and routing number, giving a program a real bank-account surface for receiving and settling funds. Virtual accounts appear as a pay
  name: Sila Virtual Accounts API
  slug: sila-money-virtual-accounts-api
- description: Linked external bank accounts used as funding sources.
  name: Sila Accounts API
  slug: sila-money-accounts-api
- description: Handle reservation, registration, and KYC / KYB verification.
  name: Sila Identity API
  slug: sila-money-identity-api
- description: Enumerated payment instruments and debit-card linking.
  name: Sila Payment Methods API
  slug: sila-money-payment-methods-api
- description: Money movement via issue / transfer / redeem over ACH.
  name: Sila Payments API
  slug: sila-money-payments-api
- description: ECDSA keypair (wallet) registration and management.
  name: Sila Wallets API
  slug: sila-money-wallets-api
artifact_total: 13
collections:
- collection_type: open
  name: Sila Money API
  slug: open-sila-money
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sila-money-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sila-money-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sila-money-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.silamoney.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.silamoney.com/docs/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sila-Money
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silamoney
- group: commercial
  title: ''
  type: Plans
  url: plans/sila-money-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sila-money-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sila-money-finops.yml
created: '2026-07-12'
description: Sila is an embedded-finance / banking-as-a-service platform that exposes a money API for fintech developers. A single REST API covers identity verification (KYC/KYB), digital wallets, linked bank accounts, virtual accounts, debit-card payment methods, and money movement over the ACH network via an issue / transfer / redeem model. Every request is signed client-side with ECDSA (secp256k1) signatures over a Keccak-256 hash of the JSON message body, sent in "authsignature" and "usersignature" (and "businesssignature" for KYB) headers. As of the review date (2026-07-12) the sandbox and production hosts, the ReadMe-hosted docs, and multiple SDKs are live and actively maintained.
finops:
- name: Sila Money Finops
  service_category: Embedded Finance and Payments
  slug: sila-money-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sila-money.png
layout: provider
modified: '2026-07-12'
name: Sila
nav: Providers
network: true
overview: 'Sila publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Identity API, Payment Methods API, and 2 more. Tagged areas include Embedded Finance, Banking as a Service, Payments, Digital Wallet, and ACH.


  Sila''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Sila Money Plans Pricing
  plan_count: 2
  slug: sila-money-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Sila Money Rate Limits
  slug: sila-money-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sila Money Authentication
  slug: sila-money-authentication
  summary_line: signature · 3 schemes
- kind: domain-security
  name: Sila Money Domain Security
  slug: sila-money-domain-security
  summary_line: HSTS · DMARC
slug: sila-money
tags:
- Embedded Finance
- Banking as a Service
- Payments
- Digital Wallet
- ACH
- KYC
- KYB
- Money Transfer
- Fintech
- Banking API
- Virtual Accounts
website: https://www.silamoney.com/
---
