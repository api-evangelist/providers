---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dodo Agentic Access
  operation_count: 1
  slug: dodo-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://route-api.dodoex.io
  baseurl_source: declared
  description: The Trade API from DODO — 1 operation(s) for trade.
  name: DODO Trade API
  slug: dodo-trade-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DODO / Route Trade API
  slug: open-dodo-trade-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dodo-trade-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dodoex.io/en/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dodoex.io/en/developer
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dodoex.io/en/developer/developer-portal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DODOEX
- group: auth
  title: ''
  type: Authentication
  url: authentication/dodo-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dodo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dodo-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dodo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dodo-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dodo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dodo-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/dodo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dodo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dodo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dodo-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dodo-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://dodoex.io/
created: '2026-07-17'
description: DODO is a decentralized exchange (DEX) and on-chain liquidity provider built on the Proactive Market Maker (PMM) algorithm, engineered for capital-efficient liquidity and low slippage across many EVM blockchains. Its Trade / Route API aggregates prices across DODO v1/v2, 1inch, 0x, ParaSwap, professional market makers, and DODO's own aggregation algorithm, returning real-time swap quotes plus executable ABI calldata that developers send directly to the DODORouteProxy / DODOV2Proxy contracts. DODO is backed by Pantera Capital and ships open-source smart contracts, JavaScript/TypeScript SDKs, a contract request library, and embeddable swap widgets.
image: https://github.com/DODOEX.png
layout: provider
modified: '2026-07-18'
name: DODO
nav: Providers
network: true
overview: 'DODO publishes 1 API on the [APIs.io](https://apis.io/) network: Trade API. Tagged areas include Company, Crypto, DeFi, DEX, and Decentralized Exchange.


  DODO''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.5
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dodo/refs/heads/main/screenshots/dodo-2026-07-25T212227.png
security:
- kind: authentication
  name: Dodo Authentication
  slug: dodo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dodo Domain Security
  slug: dodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dodo
tags:
- Company
- Crypto
- DeFi
- DEX
- Decentralized Exchange
- Blockchain
- Trading
- Liquidity
- Web3
- Swap
website: https://dodoex.io/
---
