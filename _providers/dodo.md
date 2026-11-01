---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-31'
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
  name: DODO / Route Trade API
  slug: open-dodo-trade-api
common:
- group: other
  href: https://artifacts.apis.io/dodo/overlays/dodo-trade-overlay.yaml
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
  href: https://artifacts.apis.io/dodo/authentication/dodo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dodo-authentication.yml
- group: agent
  href: https://artifacts.apis.io/dodo/agentic-access/dodo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dodo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dodo/security/dodo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dodo-domain-security.yml
- group: build
  href: https://artifacts.apis.io/dodo/packages/dodo-packages.yml
  title: ''
  type: Packages
  url: packages/dodo-packages.yml
- group: build
  href: https://artifacts.apis.io/dodo/packages/dodo-packages.yml
  title: ''
  type: SDKs
  url: packages/dodo-packages.yml
- group: agent
  href: https://artifacts.apis.io/dodo/mcp/dodo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dodo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dodo/llms/dodo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dodo-llms.txt
- group: design
  href: https://artifacts.apis.io/dodo/conventions/dodo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dodo-conventions.yml
- group: design
  href: https://artifacts.apis.io/dodo/lifecycle/dodo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dodo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dodo/conformance/dodo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dodo-conformance.yml
- group: design
  href: https://artifacts.apis.io/dodo/errors/dodo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dodo-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dodo/data-model/dodo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dodo-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dodo/skills/_index.yml
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
overview: 'DODO publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Trade API. Tagged areas include Company, Cryptocurrency, DeFi, Decentralized Exchange, and Blockchain.


  DODO''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.5
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 19.6
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
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dodo/dodo-2026-07-25T212227.png
security:
- kind: authentication
  name: Dodo Authentication
  slug: dodo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dodo Domain Security
  slug: dodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Get a DODO swap route quote
  slug: dodo-get-swap-route
slug: dodo
tags:
- Company
- Cryptocurrency
- DeFi
- Decentralized Exchange
- Blockchain
- Trading
- Liquidity
- Web3
- Swap
website: https://dodoex.io/
---
