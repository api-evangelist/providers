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
  - '{''url'': ''https://qiwi.com'', ''status'': 302, ''note'': ''declared website redirects to https://qplus.ru/ — a different registrable domain (qiwi.com -> qplus.ru), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
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
- baseURL: https://api.qiwi.com
  baseurl_source: spec
  description: The Partner API from Qiwi — 16 operation(s) for partner.
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/qiwi-capability-edges.yml
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
overview: 'Qiwi publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Payments, Wallets, Payouts, Fintech, and Banking.


  Qiwi''s developer surface includes authentication, developer portal, support, and 7 more developer resources.'
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
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 35.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Wallets
- Payouts
- Fintech
- Banking
website: https://qiwi.com
---
