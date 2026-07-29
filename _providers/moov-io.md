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
- acting_count: 39
  human_in_the_loop: 2
  name: Moov Io Agentic Access
  operation_count: 85
  slug: moov-io-agentic-access
  summary_line: 85 operations · 39 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: Business and individual accounts, the core money-movement identity.
  name: Moov Accounts API
  slug: moov-io-accounts-api
- description: Bank accounts linked as funding sources, with verification.
  name: Moov Bank Accounts API
  slug: moov-io-bank-accounts-api
- description: Money-movement capabilities enabled on an account.
  name: Moov Capabilities API
  slug: moov-io-capabilities-api
- description: Virtual spending cards, authorizations, and card transactions.
  name: Moov Card Issuing API
  slug: moov-io-card-issuing-api
- description: Payment cards linked as funding sources.
  name: Moov Cards API
  slug: moov-io-cards-api
- description: Card disputes, chargebacks, and evidence.
  name: Moov Disputes API
  slug: moov-io-disputes-api
- description: Financial institution lookup by routing number.
  name: Moov Institutions API
  slug: moov-io-institutions-api
- description: Funding-source and rail combinations usable in transfers.
  name: Moov Payment Methods API
  slug: moov-io-payment-methods-api
- description: Refunds and reversals on card transfers.
  name: Moov Refunds API
  slug: moov-io-refunds-api
- description: Beneficial owners and controllers attached to a business account.
  name: Moov Representatives API
  slug: moov-io-representatives-api
- description: Automated sweeps of wallet balances to a bank account.
  name: Moov Sweeps API
  slug: moov-io-sweeps-api
- description: Money movement across ACH, RTP, push-to-card, and card acquiring.
  name: Moov Transfers API
  slug: moov-io-transfers-api
- description: Underwriting details used to enable card acquiring and higher-risk activity.
  name: Moov Underwriting API
  slug: moov-io-underwriting-api
- description: Stored-balance wallets and their ledgered transactions.
  name: Moov Wallets API
  slug: moov-io-wallets-api
artifact_total: 22
collections:
- collection_type: open
  name: Moov API
  slug: open-moov-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moov-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moov-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moov-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moov-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moov-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moov-financial
- group: company
  title: ''
  type: Blog
  url: https://moov.io/blog/index.xml
- group: company
  title: ''
  type: Website
  url: https://moov.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moov.io
- group: commercial
  title: ''
  type: Plans
  url: plans/moov-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moov-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moov-io-finops.yml
created: '2026-07-02'
description: Moov is a money-movement platform that lets software teams accept, store, send, and spend money through a single REST API. The Moov API covers accounts and onboarding, representatives, capabilities and underwriting, funding sources (bank accounts, cards, Apple Pay, Google Pay, wallets), and money movement across ACH, RTP, push-to-card, and card acquiring - plus transfers, refunds, disputes, sweeps, and card issuing. Moov also maintains a well-known open-source GitHub organization (github.com/moov-io) of Go libraries for banking file formats (ACH, wire, IAT, and more); this catalog documents the commercial hosted Moov money-movement API at api.moov.io.
finops:
- name: Moov Io Finops
  service_category: Financial Services
  slug: moov-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moov-io.png
layout: provider
modified: '2026-07-02'
name: Moov
nav: Providers
network: true
overview: 'Moov publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Bank Accounts API, Capabilities API, and 11 more. Tagged areas include Payments, Money Movement, Fintech, ACH, and RTP.


  Moov''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Moov Io Plans Pricing
  plan_count: 2
  slug: moov-io-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Moov Io Rate Limits
  slug: moov-io-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -3.3
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moov Io Authentication
  slug: moov-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moov Io Domain Security
  slug: moov-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Moov Io Trust Center
  slug: moov-io-trust-center
  summary_line: SOC 2
slug: moov-io
tags:
- Payments
- Money Movement
- Fintech
- ACH
- RTP
- Cards
- Wallets
- Embedded Finance
website: https://moov.io
---
