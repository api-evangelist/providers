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
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Curve Finance Agentic Access
  operation_count: 43
  slug: curve-finance-agentic-access
  summary_line: 43 operations
api_count: 1
apis:
- description: Public read-only REST API used by the Curve UI and third parties. Endpoints cover /getPools/all, /getSubgraphData, /getFactoryAPYs, /getLendingVaults, /getCrvUsdData, and similar. JSON output. No auth
  name: Curve REST API
  slug: rest-api
- description: Curve's primary surface for swaps and liquidity is a set of audited Vyper smart contracts deployed across multiple chains (StableSwap and CryptoSwap pools, factories, gauges, voting escrow, crvUSD, le
  name: Curve Smart Contracts
  slug: smart-contracts
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The crvUSD API from Curve Finance — 6 operation(s) for crvusd.
  name: Curve Finance crvUSD API
  slug: curve-finance-crvusd-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Deprecated API from Curve Finance — 10 operation(s) for deprecated.
  name: Curve Finance Deprecated API
  slug: curve-finance-deprecated-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Gauges API from Curve Finance — 1 operation(s) for gauges.
  name: Curve Finance Gauges API
  slug: curve-finance-gauges-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Lending API from Curve Finance — 3 operation(s) for lending.
  name: Curve Finance Lending API
  slug: curve-finance-lending-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Misc API from Curve Finance — 5 operation(s) for misc.
  name: Curve Finance Misc API
  slug: curve-finance-misc-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Pools API from Curve Finance — 11 operation(s) for pools.
  name: Curve Finance Pools API
  slug: curve-finance-pools-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Tokens API from Curve Finance — 1 operation(s) for tokens.
  name: Curve Finance Tokens API
  slug: curve-finance-tokens-api
- baseURL: https://api.curve.finance/api
  baseurl_source: declared
  description: The Volumes and APYs API from Curve Finance — 8 operation(s) for volumes and apys.
  name: Curve Finance Volumes and APYs API
  slug: curve-finance-volumes-and-apys-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Curve.finance crvUSD API
  slug: open-curve-finance-crvusd-api
- collection_type: open
  name: Curve.finance crvUSD Deprecated API
  slug: open-curve-finance-deprecated-api
- collection_type: open
  name: Curve.finance crvUSD Gauges API
  slug: open-curve-finance-gauges-api
- collection_type: open
  name: Curve.finance crvUSD Lending API
  slug: open-curve-finance-lending-api
- collection_type: open
  name: Curve.finance crvUSD Misc API
  slug: open-curve-finance-misc-api
- collection_type: open
  name: Curve.finance crvUSD Pools API
  slug: open-curve-finance-pools-api
- collection_type: open
  name: Curve.finance crvUSD Tokens API
  slug: open-curve-finance-tokens-api
- collection_type: open
  name: Curve.finance crvUSD Volumes and APYs API
  slug: open-curve-finance-volumes-and-apys-api
- collection_type: open
  name: Curve.finance API
  slug: open-curve-finance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/curve-finance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/curve-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curve-finance-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://curve.fi/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curve.finance/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/curvefi
- group: operate
  title: ''
  type: Forums
  url: https://gov.curve.finance/
- group: commercial
  title: ''
  type: Plans
  url: plans/curve-finance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/curve-finance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/curve-finance-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.curve.finance/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://news.curve.finance/rss/
created: '2026-05-08'
description: Curve Finance is a DeFi automated market maker (AMM) optimized for low-slippage swaps among stablecoins and pegged assets across multiple chains. Curve maintains a public read-only REST API at api.curve.finance providing pool, gauge, factory, governance, lending, crvUSD, and TVL data. Smart-contract entry points are the primary write path; the REST API is for indexing and analytics.
finops:
- name: Curve Finance Finops
  service_category: DeFi Protocol
  slug: curve-finance-finops
graphqls:
- description: Curve Finance exposes on-chain data through The Graph Protocol subgraphs. The primary production subgraph is maintained by Messari and follows the DEX AMM schema standard (version 1.3.0). It indexes p
  name: Curve Finance GraphQL
  slug: curve-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curve-finance.png
layout: provider
modified: '2026-05-08'
name: Curve Finance
nav: Providers
network: true
overview: 'Curve Finance publishes 8 APIs on the [APIs.io](https://apis.io/) network, including crvUSD API, Deprecated API, Gauges API, and 5 more. Tagged areas include Web3, DeFi, DEX, AMM, and Stablecoins.


  Curve Finance''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Curve Finance Plans Pricing
  plan_count: 2
  slug: curve-finance-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Curve Finance Rate Limits
  slug: curve-finance-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 47.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curve-finance/refs/heads/main/screenshots/curve-finance-2026-06-20T175354.png
security:
- kind: domain-security
  name: Curve Finance Domain Security
  slug: curve-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Curve Finance Vulnerability Disclosure
  slug: curve-finance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: curve-finance
tags:
- Web3
- DeFi
- DEX
- AMM
- Stablecoins
- Pegged Assets
- Multi-Chain
- Open-Source
website: https://curve.fi/
---
