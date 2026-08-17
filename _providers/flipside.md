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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Flipside Agentic Access
  operation_count: 1
  slug: flipside-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The JSON-RPC API from Flipside Crypto — 1 operation(s) for json-rpc.
  name: Flipside Crypto JSON-RPC API
  slug: flipside-json-rpc-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flipside Crypto Data JSON-RPC API
  slug: open-flipside-json-rpc-api
- collection_type: open
  name: Flipside Crypto Data API
  slug: open-flipside
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flipside-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flipside-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flipside-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlipsideCrypto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flipside-crypto
- group: company
  title: ''
  type: Website
  url: https://flipsidecrypto.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flipsidecrypto.xyz
- group: commercial
  title: ''
  type: Plans
  url: plans/flipside-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flipside-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flipside-finops.yml
created: '2026-06-21'
description: Flipside Crypto is a blockchain analytics platform that lets analysts and developers run SQL queries against curated, Snowflake-backed on-chain datasets covering Ethereum, Solana, and 20+ other chains. The Data API exposes query execution and result retrieval over a JSON-RPC-style HTTP interface at api-v2.flipsidecrypto.xyz, authenticated with an x-api-key. In May 2026 Flipside sold its blockchain data business to SonarX and refocused on its edisyl enterprise AI platform; this catalog documents the Flipside Data API as published.
finops:
- name: Flipside Finops
  service_category: Analytics
  slug: flipside-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flipside.png
layout: provider
modified: '2026-06-21'
name: Flipside Crypto
nav: Providers
network: true
overview: 'Flipside Crypto publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include Blockchain, Analytics, SQL, Web3, and Data.


  Flipside Crypto''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Flipside Plans Pricing
  plan_count: 4
  slug: flipside-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 4
  name: Flipside Rate Limits
  slug: flipside-rate-limits
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.2
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flipside/refs/heads/main/screenshots/flipside-2026-07-25T214804.png
security:
- kind: authentication
  name: Flipside Authentication
  slug: flipside-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flipside Domain Security
  slug: flipside-domain-security
  summary_line: TLSv1.3 · HSTS
slug: flipside
tags:
- Blockchain
- Analytics
- SQL
- Web3
- Data
website: https://flipsidecrypto.xyz
---
