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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Decentralized JSON-RPC + WebSocket API for the Angstrom DEX. Every Angstrom node runs its own JSON-RPC server (there is no single central API); a load-balanced HTTPS/WebSocket endpoint is recommended '
  name: Angstrom API
  slug: angstrom-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://sorellalabs.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.angstrom.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.angstrom.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.angstrom.xyz/api/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.angstrom.xyz/integrators/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SorellaLabs
- group: company
  title: ''
  type: Blog
  url: https://sorellalabs.xyz/writing
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/M2jPzgUQd2
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.angstrom.xyz
- group: other
  title: ''
  type: X
  url: https://twitter.com/sorellalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sorella-labs/
- group: build
  href: https://artifacts.apis.io/sorella-labs/packages/sorella-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/sorella-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/sorella-labs/packages/sorella-labs-packages.yml
  title: ''
  type: Packages
  url: packages/sorella-labs-packages.yml
- group: auth
  href: https://artifacts.apis.io/sorella-labs/authentication/sorella-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sorella-labs-authentication.yml
- group: design
  href: https://artifacts.apis.io/sorella-labs/conventions/sorella-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sorella-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/sorella-labs/conformance/sorella-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sorella-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/sorella-labs/lifecycle/sorella-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sorella-labs-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/sorella-labs/llms/sorella-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sorella-labs-llms.txt
- group: auth
  href: https://artifacts.apis.io/sorella-labs/security/sorella-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sorella-labs-domain-security.yml
created: '2026-07-17'
description: Sorella Labs is a crypto-infrastructure company building Angstrom, a new kind of decentralized exchange (DEX) built on top of Uniswap V4 that internalizes MEV through application-level sequencing. By enforcing its own transaction ordering, Angstrom redirects value that would normally be extracted by MEV bots and validators back to the actual participants — liquidity providers and swappers. The company also builds Brontes, a Rust blockchain-analytics engine specialized in systematic MEV detection. Angstrom exposes a decentralized JSON-RPC API — each node runs its own JSON-RPC server, with a recommended load-balanced HTTPS/WebSocket endpoint plus a separate on-chain Data API — and ships Rust libraries (angstrom-sdk, angstrom-v4) for integrators, routers, and solvers. Backed by Paradigm.
image: https://sorellalabs.xyz/logo.png
layout: provider
modified: '2026-07-21'
name: Sorella Labs
nav: Providers
network: true
overview: 'Sorella Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Infrastructure, DeFi, Decentralized Exchange, and MEV.


  Sorella Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 22.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sorella-labs/sorella-labs-2026-09-02T160233.png
security:
- kind: authentication
  name: Sorella Labs Authentication
  slug: sorella-labs-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Sorella Labs Domain Security
  slug: sorella-labs-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: sorella-labs
tags:
- Company
- Crypto Infrastructure
- DeFi
- Decentralized Exchange
- MEV
- Ethereum
- Uniswap V4
- JSON-RPC
- Blockchain
- Trading
website: https://sorellalabs.xyz
---
