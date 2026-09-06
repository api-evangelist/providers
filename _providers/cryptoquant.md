---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cryptoquant Agentic Access
  operation_count: 12
  slug: cryptoquant-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Inflow, outflow, and reserve metrics for major exchanges.
  name: CryptoQuant Exchange Flows API
  slug: cryptoquant-exchange-flows-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Price, open interest, and derivatives metrics.
  name: CryptoQuant Market Data API
  slug: cryptoquant-market-data-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Miner reserve, position index, and outflow metrics.
  name: CryptoQuant Miner API
  slug: cryptoquant-miner-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Network indicators including SOPR, MVRV, NVT, and active addresses.
  name: CryptoQuant On-Chain API
  slug: cryptoquant-on-chain-api
- baseURL: https://api.cryptoquant.com/v1
  baseurl_source: declared
  description: Stablecoin supply ratio and exchange metrics.
  name: CryptoQuant Stablecoins API
  slug: cryptoquant-stablecoins-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CryptoQuant Exchange Flows API
  slug: open-cryptoquant-exchange-flows-api
- collection_type: open
  name: CryptoQuant Exchange Flows Market Data API
  slug: open-cryptoquant-market-data-api
- collection_type: open
  name: CryptoQuant Exchange Flows Miner API
  slug: open-cryptoquant-miner-api
- collection_type: open
  name: CryptoQuant Exchange Flows On-Chain API
  slug: open-cryptoquant-on-chain-api
- collection_type: open
  name: CryptoQuant Exchange Flows Stablecoins API
  slug: open-cryptoquant-stablecoins-api
- collection_type: open
  name: CryptoQuant API
  slug: open-cryptoquant
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptoquant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cryptoquant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cryptoquant-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crypto-quant
- group: company
  title: ''
  type: Website
  url: https://cryptoquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptoquant.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptoquant.com/products/api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cryptoquant-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cryptoquant-timeseries-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cryptoquant-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/cryptoquant-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cryptoquant-vocabulary.yml
created: '2025-02-12'
description: CryptoQuant is a blockchain data analytics platform providing real-time and historical on-chain, exchange flow, miner, derivatives, and stablecoin metrics for Bitcoin, Ethereum, and other major cryptocurrencies. The API delivers time-series data used by traders, funds, and researchers to gauge market sentiment and capital flows.
finops:
- name: Cryptoquant Finops
  service_category: API
  slug: cryptoquant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptoquant.png
json_schemas:
- name: CryptoQuantTimeSeriesResponse
  property_count: 2
  slug: cryptoquant-timeseries
jsonld:
- class_count: 8
  name: Cryptoquant Context
  property_count: 8
  slug: cryptoquant-context
layout: provider
modified: '2026-05-19'
name: CryptoQuant
nav: Providers
network: true
overview: 'CryptoQuant publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Exchange Flows API, Market Data API, Miner API, and 2 more. Tagged areas include Blockchain, Cryptocurrency, On-Chain Analytics, Market Data, and Derivatives.


  The CryptoQuant catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CryptoQuant''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Cryptoquant Plans Pricing
  plan_count: 3
  slug: cryptoquant-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Cryptoquant Rate Limits
  slug: cryptoquant-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CryptoQuant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cryptoquant-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: CryptoQuant API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: cryptoquant-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 59.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 34.1
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
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptoquant/refs/heads/main/screenshots/cryptoquant-2026-06-20T175316.png
security:
- kind: authentication
  name: Cryptoquant Authentication
  slug: cryptoquant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cryptoquant Domain Security
  slug: cryptoquant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cryptoquant
tags:
- Blockchain
- Cryptocurrency
- On-Chain Analytics
- Market Data
- Derivatives
website: https://cryptoquant.com/
---
