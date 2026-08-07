---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.hamsa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hamsa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hamsa.com/docs/hamsa-privacy-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hamsa.com/reference/api-documentation
- group: start
  title: ''
  type: Login
  url: https://developer.hamsa.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.hamsa.com/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hamsa.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hamsa.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hamsa-finance
- group: company
  title: ''
  type: Twitter
  url: https://x.com/hamsafinance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hamsa-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hamsa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hamsa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hamsa-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hamsa-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hamsa-well-known.yml
created: '2026-07-17'
description: Hamsa (formerly HamsaPay) is a San Francisco-based financial infrastructure company "powering the Finternet." It builds the Hamsa Unified Confidential Ledger (UCL), a privacy-enabled, EVM-compatible, permissioned Layer-2 blockchain for banks and financial institutions, plus the Hamsa Privacy module that uses zero-knowledge-proof (ZKP) rollups on Hyperledger Besu to run confidential Delivery-versus-Payment (DvP) and Payment-versus-Payment (PvP) settlement, tokenized deposits, stablecoins, and CBDCs. The developer platform exposes an EVM-standard JSON-RPC API (eth_* methods) and DvP escrow smart contracts, authenticated with Ethereum message signatures and role-based access control. Hamsa has tokenized over $3.2B for Tier-1/Tier-2 banks (including Banco Safra's Safra Dolar stablecoin) and participates in the Brazilian Drex CBDC pilot.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hamsa.png
layout: provider
modified: '2026-07-19'
name: Hamsa
nav: Providers
network: true
overview: 'Hamsa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Blockchain, Payments, and Tokenization.


  Hamsa''s developer surface includes documentation, API reference, engineering blog, authentication, and 12 more developer resources.'
random_paper: 70
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hamsa/refs/heads/main/screenshots/hamsa-2026-07-25T220608.png
security:
- kind: authentication
  name: Hamsa Authentication
  slug: hamsa-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Hamsa Domain Security
  slug: hamsa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hamsa
tags:
- Company
- Financial Services
- Blockchain
- Payments
- Tokenization
- Privacy
- Zero-Knowledge Proofs
- CBDC
- Settlement
- DeFi
- EVM
- JSON-RPC
website: https://www.hamsa.com
---
