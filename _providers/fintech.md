---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.fin.tech/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fin.tech/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fin.tech/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fintech-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fintech-domain-security.yml
created: '2026-07-17'
description: 'Fin (fin.tech) is a crypto-native payments company that lets users and businesses move millions of dollars instantly — to other Fin users, directly into bank accounts, or across crypto rails. It provides business-grade payment rails that feel like a consumer payment app rather than crypto: instant global settlement in seconds, native support to deposit and withdraw to bank accounts, and send/receive of USDT, USDC, ETH, and BTC, while Fin abstracts the underlying crypto settlement behind a clean fintech interface. Backed by Sequoia, Multicoin, and Pantera Capital, Fin operates a private, auth-gated production API surface (api.fin.tech) and publishes an llms.txt for agents; it does not currently publish a public developer portal, OpenAPI, or SDKs. Surfaced in the API Evangelist network as a Pantera Capital portfolio company (sector: crypto) and enriched from its public web surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fintech.png
layout: provider
modified: '2026-07-19'
name: Fintech
nav: Providers
network: true
overview: Fintech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Payments, Stablecoins, and Banking.
random_paper: 2
score:
  band: minimal
  composite: 8.0
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fintech/refs/heads/main/screenshots/fintech-2026-07-25T214549.png
security:
- kind: domain-security
  name: Fintech Domain Security
  slug: fintech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fintech
tags:
- Company
- Crypto
- Payments
- Stablecoins
- Banking
- Cross-Border Payments
- Settlement
- Fintech
website: https://www.fin.tech/
---
