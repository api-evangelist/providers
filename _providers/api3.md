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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Api3 Agentic Access
  operation_count: 4
  slug: api3-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Managed decentralized API (dAPI) data feeds sourced directly from first-party oracle nodes operated by the data providers themselves. Each feed aggregates signed data from multiple Airnode operators a
  name: API3 dAPI Data Feeds
  slug: dapi-data-feeds
- description: Oracle Extractable Value (OEV) Rewards is API3's revenue-sharing mechanism for dApps that integrate OEV-enabled Api3ReaderProxyV1 proxy contracts. When liquidation or arbitrage opportunities arise aro
  name: API3 OEV Rewards
  slug: oev-rewards
- description: 'The Airnode HTTP gateway exposes a REST endpoint that allows authorized callers to query an Airnode operator''s API data off-chain without sending a blockchain transaction. API providers configure the '
  name: API3 Airnode HTTP Gateway
  slug: airnode-http-gateway
- description: Airnode address discovery
  name: API3 Airnodes API
  slug: api3-airnodes-api
- description: Reading and writing cryptographically signed oracle data
  name: API3 Signed Data API
  slug: api3-signed-data-api
- description: Health and deployment information
  name: API3 Status API
  slug: api3-status-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API3 Signed Airnodes API
  slug: open-api3-airnodes-api
- collection_type: open
  name: API3 Signed Airnodes Signed Data API
  slug: open-api3-signed-data-api
- collection_type: open
  name: API3 Signed Airnodes Status API
  slug: open-api3-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/api3-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/api3-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://api3.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api3.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.api3.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api3dao
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/qnRrcfnm5W
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/API3DAO
- group: other
  title: ''
  type: Telegram
  url: https://t.me/API3DAO
- group: operate
  title: ''
  type: Forums
  url: https://forum.api3.org/
- group: other
  title: ''
  type: Staking
  url: https://stake.api3.org/
- group: other
  title: ''
  type: Market
  url: https://market.api3.org/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/api3-signed-api-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/api3-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/api3-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/api3-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/api3-finops.yml
created: '2026-06-13'
description: API3 is a first-party blockchain oracle network that connects real-world APIs directly to smart contracts without intermediary nodes. Its core technology is Airnode, a serverless oracle node that API providers operate themselves, cryptographically signing data before serving it on-chain. The API3 Market enables dApp developers to subscribe to managed decentralized APIs (dAPIs) — aggregated, multi-source data feeds covering 150+ price pairs across 40+ EVM chains — without speaking to a sales rep or signing a contract. API3's OEV (Oracle Extractable Value) mechanism captures MEV that traditionally leaks to bots around oracle updates and redistributes 80% of that revenue to the dApps reading the feeds, creating a net-positive oracle revenue model. The DAO governs the network via staked API3 tokens.
finops:
- name: Api3 Finops
  service_category: Blockchain & Data Infrastructure
  slug: api3-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api3.png
jsonld:
- class_count: 6
  name: Api3 Context
  property_count: 8
  slug: api3-context
layout: provider
modified: '2026-06-13'
name: API3
nav: Providers
network: true
overview: 'API3 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Airnodes API, Signed Data API, and Status API. Tagged areas include Blockchain, Oracle, Decentralized, Data Feeds, and Price Feeds.


  The API3 catalog on APIs.io includes 1 JSON-LD context.


  API3''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Api3 Plans
  plan_count: 3
  slug: api3-plans
random_paper: 8
rate_limits:
- limit_count: 3
  name: Api3 Rate Limits
  slug: api3-rate-limits
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 62.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api3/refs/heads/main/screenshots/api3-2026-06-20T172222.png
security:
- kind: authentication
  name: Api3 Authentication
  slug: api3-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Api3 Domain Security
  slug: api3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: api3
tags:
- Blockchain
- Oracle
- Decentralized
- Data Feeds
- Price Feeds
- Web3
- DeFi
- Smart Contracts
- OEV
- dAPI
website: https://api3.org/
---
