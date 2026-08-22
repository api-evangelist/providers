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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Qiwi Agentic Access
  operation_count: 21
  slug: qiwi-agentic-access
  summary_line: 21 operations · 12 acting
api_count: 10
apis:
- description: API for legal entities to issue payouts to wallets, cards, and bank accounts with batch and individual transfer support.
  name: Qiwi Legal Entity Payouts
  slug: qiwi-legal-entity-payouts
- description: API for sending payouts directly to Qiwi wallets.
  name: Qiwi Wallet Payouts
  slug: qiwi-wallet-payouts
- description: API for issuing payouts to bank cards, wallets, and SBP (Faster Payments System) recipients.
  name: Qiwi Card Wallet SBP Payouts
  slug: qiwi-card-wallet-sbp-payouts
- description: API for topping up mobile phone balances across telecom operators.
  name: Qiwi Mobile Topups
  slug: qiwi-mobile-topups
- description: Banking-as-a-Service platform for issuing accounts, cards, and banking operations on top of Qiwi infrastructure.
  name: Qiwi Banking Platform
  slug: qiwi-baas
- description: API for client identification and KYC verification workflows.
  name: Qiwi Client Identification Service
  slug: qiwi-identification-service
- description: API to retrieve Qiwi terminal locations and their service capabilities.
  name: Qiwi Terminal Map
  slug: qiwi-terminal-map
- description: Personal Qiwi Wallet API for managing balance, transfers, payments, and transaction history for end users.
  name: Qiwi Wallet Personal
  slug: qiwi-wallet-personal
- description: Peer-to-peer payment API for accepting payments from individuals via payment forms and invoices.
  name: Qiwi P2P Payments
  slug: qiwi-p2p-payments
- description: The Partner API from Qiwi — 16 operation(s) for partner.
  name: Qiwi Partner API
  slug: qiwi-partner-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QIWI Payments Partner API
  slug: open-qiwi-partner-api
- collection_type: open
  name: QIWI Payments API
  slug: open-qiwi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qiwi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qiwi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qiwi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qiwi
- group: start
  title: ''
  type: Portal
  url: https://developer.qiwi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QIWI-API
- group: company
  title: ''
  type: Website
  url: https://qiwi.com
- group: operate
  title: ''
  type: Support
  url: https://qiwi.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qiwi.com/legal
created: '2026-03-16'
description: Qiwi provides payment reception, payouts, and banking platform APIs for processing wallet, card, mobile, and SBP transactions across Russia and CIS markets.
finops:
- name: Qiwi Finops
  service_category: API
  slug: qiwi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qiwi.png
layout: provider
modified: '2026-05-19'
name: Qiwi
nav: Providers
network: true
overview: 'Qiwi publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Payments, Wallet, Payouts, Fintech, and Banking.


  Qiwi''s developer surface includes authentication, developer portal, support, and 6 more developer resources.'
plans:
- name: Qiwi Plans Pricing
  plan_count: 3
  slug: qiwi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Qiwi Rate Limits
  slug: qiwi-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: -4.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qiwi/refs/heads/main/screenshots/qiwi-2026-06-20T192337.png
security:
- kind: authentication
  name: Qiwi Authentication
  slug: qiwi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qiwi Domain Security
  slug: qiwi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qiwi
tags:
- Payments
- Wallet
- Payouts
- Fintech
- Banking
website: https://qiwi.com
---
