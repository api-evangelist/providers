---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Accept payments globally across 900+ local payment methods including cards, bank transfers, eWallets and cash.
  name: Rapyd Collect API
  slug: rapyd-collect-api
- description: Send mass payouts to bank accounts, cards and wallets in 190+ countries.
  name: Rapyd Disburse API
  slug: rapyd-disburse-api
- description: Create and manage multi-currency eWallets for end users and merchants.
  name: Rapyd Wallet API
  slug: rapyd-wallet-api
- description: Issue physical and virtual prepaid and debit cards.
  name: Rapyd Issuing API
  slug: rapyd-issuing-api
- description: Open multi-currency virtual accounts to receive funds locally in major markets.
  name: Rapyd Global Accounts API
  slug: rapyd-global-accounts-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapyd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RapydPayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rapydpayments
- group: company
  title: ''
  type: Website
  url: https://www.rapyd.net/
- group: commercial
  title: ''
  type: Plans
  url: plans/rapyd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rapyd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rapyd-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.rapyd.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.rapyd.net/feed/
created: '2026-05-08'
description: Rapyd is a global Fintech-as-a-Service network offering collect, disburse, hold, and issue capabilities across 100+ countries with local payment methods, cards, and bank transfers.
finops:
- name: Rapyd Finops
  service_category: Fintech
  slug: rapyd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rapyd.png
layout: provider
modified: '2026-05-08'
name: Rapyd
nav: Providers
network: true
overview: 'Rapyd publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Cross-Border, Cards, and Wallets.


  Rapyd''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Rapyd Plans Pricing
  plan_count: 1
  slug: rapyd-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Rapyd Rate Limits
  slug: rapyd-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rapyd/refs/heads/main/screenshots/rapyd-2026-06-20T192606.png
security:
- kind: domain-security
  name: Rapyd Domain Security
  slug: rapyd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rapyd
tags:
- Fintech
- Payments
- Cross-Border
- Cards
- Wallets
website: https://www.rapyd.net/
---
