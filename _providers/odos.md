---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Odos Agentic Access
  operation_count: 17
  slug: odos-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 5
apis:
- description: The Odos Token Pricing API provides real-time price data for 100,000+ DeFi assets across 15 supported blockchain networks. The pricing data is DeFi-native and sourced directly from on-chain liquidity,
  name: Odos Token Pricing API
  slug: odos-token-pricing-api
- description: 'The Odos Liquidity Zaps API enables streamlined single-transaction liquidity provisioning with optimized routing. Users can provide liquidity to DeFi protocols using any token combination in a single '
  name: Odos Liquidity Zaps API
  slug: odos-liquidity-zaps-api
- description: General information about the Odos service offerings
  name: Odos Information API
  slug: odos-information-api
- description: Query Odos' price for any token with liquidity
  name: Odos Pricing API
  slug: odos-pricing-api
- description: Swap tokens
  name: Odos Smart Order Routing API
  slug: odos-smart-order-routing-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/odos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odos-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://enterprise.odos.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.odos.xyz/
- group: company
  title: ''
  type: About
  url: https://docs.odos.xyz/home/about
- group: operate
  title: ''
  type: FAQ
  url: https://docs.odos.xyz/resources/faq
- group: commercial
  title: ''
  type: Plans
  url: https://docs.odos.xyz/build/api_pricing
- group: operate
  title: ''
  type: Status
  url: https://status.odos.xyz
- group: build
  title: ''
  type: GitHub
  url: https://github.com/odos-xyz
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/odos
- group: company
  title: ''
  type: Twitter
  url: https://x.com/odosprotocol
- group: other
  title: ''
  type: Telegram
  url: https://t.me/OdosProtocol
- group: operate
  title: ''
  type: Forums
  url: https://forum.odos.xyz
- group: other
  title: ''
  type: App
  url: https://app.odos.xyz
- group: agent
  title: ''
  type: MCP
  url: https://github.com/odos-xyz/odos-mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.odos.xyz/resources/terms-of-service
created: '2026-06-14'
description: Odos is a DEX aggregator and smart order routing platform that uses a sophisticated optimization algorithm to unify fragmented liquidity and maximize the output of every trade. The platform scans 1050+ liquidity pools across 15 EVM-compatible chains to find optimal swap routes while accounting for gas costs. Since launching in 2022, Odos has facilitated over $100B in transaction volume and served 3.2M+ unique wallets. Odos provides REST APIs for token swap quotes, optimal routing, slippage management, multi-token transaction execution, token pricing, and liquidity zap operations.
examples:
- key_count: 2
  name: Examples
  slug: examples
finops:
- name: Apis
  service_category: ''
  slug: apis
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odos.png
json_schemas:
- name: Odos API Schemas
  property_count: 0
  slug: schemas
jsonld:
- class_count: 4
  name: context Context
  property_count: 44
  slug: context
layout: provider
modified: '2026-06-14'
name: Odos
nav: Providers
network: true
overview: 'Odos publishes 3 APIs on the [APIs.io](https://apis.io/) network: Information API, Pricing API, and Smart Order Routing API. Tagged areas include DEX, Aggregator, DeFi, Token Swaps, and Liquidity.


  The Odos catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Odos'' developer surface includes developer portal, documentation, FAQ, status page, GitHub presence, and 11 more developer resources.'
plans:
- name: Apis
  plan_count: 4
  slug: apis
random_paper: 57
rate_limits:
- limit_count: 0
  name: Apis
  slug: apis
rules:
- name: Odos API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: odos-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.6
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/odos/refs/heads/main/screenshots/odos-2026-06-20T190622.png
security:
- kind: domain-security
  name: Odos Domain Security
  slug: odos-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: odos
tags:
- DEX
- Aggregator
- DeFi
- Token Swaps
- Liquidity
- Routing
- Blockchain
- EVM
- Web3
website: https://enterprise.odos.xyz
---
