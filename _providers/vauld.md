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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Enterprise API for partner organisations covering fiat<>crypto trading on India INR rails (deposits via Cards/UPI/NEFT/IMPS/RTGS), automated KYC verification (Aadhar/PAN/VoterID/Passport), crypto<>cry
  name: Vauld Enterprise API
  slug: vauld-enterprise-api
artifact_total: 4
asyncapis:
- description: ''
  name: Vauld Webhooks
  slug: vauld-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vauld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vauld.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vauld.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vauld.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vauld.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vauld.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.vauld.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vauld
- group: commercial
  title: ''
  type: Pricing
  url: https://vauld.com/fees
- group: auth
  title: ''
  type: Authentication
  url: authentication/vauld-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vauld-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vauld-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vauld-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vauld-problem-types.yml
- group: design
  title: ''
  type: Components
  url: components/vauld-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vauld-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vauld-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vauld-llms.txt
created: '2026-07-17'
description: Vauld (formerly Bank of Hodlers) is a crypto asset management platform founded in India and headquartered in Singapore, backed by Peter Thiel's Valar Ventures, Pantera Capital, and Coinbase Ventures. Its Enterprise API exposes wallets, INR fiat rails, KYC verification, crypto swaps, borrowing, and lending to partner organisations, authenticated with HMAC-SHA256 request signing. Vauld suspended customer withdrawals in July 2022 and entered creditor-protection restructuring in Singapore; the API documentation remains published and the platform API still responds, though the documented testnet hosts no longer resolve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vauld.png
layout: provider
modified: '2026-07-21'
name: Vauld
nav: Providers
network: true
overview: 'Vauld publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Lending, Borrowing, and Trading.


  The Vauld catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vauld''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 11 more developer resources.'
random_paper: 93
score:
  band: thin
  composite: 31.5
  delta: -2.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 52.4
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Vauld Authentication
  slug: vauld-authentication
  summary_line: hmac · 1 scheme
- kind: domain-security
  name: Vauld Domain Security
  slug: vauld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vauld
tags:
- Company
- Crypto
- Lending
- Borrowing
- Trading
- Wallets
- KYC
- Fintech
- India
- Singapore
website: https://www.vauld.com/
---
