---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.timeswap.io
  baseurl_source: declared
  description: The FastAPI API from Timeswap — 1 operation(s) for fastapi.
  name: Timeswap FastAPI API
  slug: timeswap-fastapi-api
- baseURL: https://api.timeswap.io
  baseurl_source: declared
  description: The Paulygon API from Timeswap — 1 operation(s) for paulygon.
  name: Timeswap Paulygon API
  slug: timeswap-paulygon-api
- baseURL: https://api.timeswap.io
  baseurl_source: declared
  description: The Pools API from Timeswap — 10 operation(s) for pools.
  name: Timeswap Pools API
  slug: timeswap-pools-api
- baseURL: https://api.timeswap.io
  baseurl_source: declared
  description: The TaskON API from Timeswap — 1 operation(s) for taskon.
  name: Timeswap TaskON API
  slug: timeswap-taskon-api
- baseURL: https://api.timeswap.io
  baseurl_source: declared
  description: The Token API from Timeswap — 1 operation(s) for token.
  name: Timeswap Token API
  slug: timeswap-token-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast FastAPI API
  slug: open-timeswap-fastapi-api
- collection_type: open
  name: Fast FastAPI Paulygon API
  slug: open-timeswap-paulygon-api
- collection_type: open
  name: Fast FastAPI Pools API
  slug: open-timeswap-pools-api
- collection_type: open
  name: Fast FastAPI TaskON API
  slug: open-timeswap-taskon-api
- collection_type: open
  name: Fast FastAPI Token API
  slug: open-timeswap-token-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/timeswap-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timeswap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://timeswap.io
- group: docs
  title: ''
  type: Documentation
  url: https://timeswap.gitbook.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Timeswap-Labs
- group: company
  title: ''
  type: Blog
  url: https://timeswap.medium.com/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/timeswap
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TimeswapLabs
- group: other
  title: ''
  type: Telegram
  url: https://t.me/timeswap
- group: other
  title: ''
  type: Whitepaper
  url: https://timeswap.io/whitepaper.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://timeswap.io/terms/
- group: build
  title: ''
  type: Packages
  url: packages/timeswap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/timeswap-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/timeswap-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/timeswap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/timeswap-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/timeswap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://timeswap.gitbook.io/docs/audits
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/timeswap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/timeswap-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timeswap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/timeswap-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/timeswap-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Timeswap is a decentralized fixed-maturity lending and borrowing protocol built by Timeswap Labs. Its AMM lets lenders earn fixed interest, borrowers take non-liquidatable loans against any ERC-20 collateral, and liquidity providers act as the counterparty, across pools on multiple EVM chains. Alongside the on-chain V2 contracts, Timeswap runs a public backend API at api.timeswap.io serving pools, caps, tokens, and spot prices to its dApp, and publishes TypeScript SDK packages under the @timeswap-labs npm scope.
image: https://avatars.githubusercontent.com/u/75018723?v=4
layout: provider
modified: '2026-07-21'
name: Timeswap
nav: Providers
network: true
overview: 'Timeswap publishes 5 APIs on the [APIs.io](https://apis.io/) network, including FastAPI API, Paulygon API, Pools API, and 2 more. Tagged areas include Company, Crypto Web3, DeFi, Lending, and Borrowing.


  Timeswap''s developer surface includes documentation, engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 43.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 33.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timeswap/refs/heads/main/screenshots/timeswap-2026-09-02T163804.png
security:
- kind: authentication
  name: Timeswap Authentication
  slug: timeswap-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Timeswap Domain Security
  slug: timeswap-domain-security
  summary_line: TLSv1.3 · HSTS
slug: timeswap
tags:
- Company
- Crypto Web3
- DeFi
- Lending
- Borrowing
- Liquidity Pools
- Fixed Income
- Blockchain
website: https://timeswap.io
---
