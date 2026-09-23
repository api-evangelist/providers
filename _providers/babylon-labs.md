---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Babylon Labs Agentic Access
  operation_count: 19
  slug: babylon-labs-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 1
apis:
- baseURL: https://staking-api.babylonlabs.io
  baseurl_source: declared
  description: Shared API endpoints
  name: Babylon Labs shared API
  slug: babylon-labs-shared-api
- baseURL: https://staking-api.babylonlabs.io
  baseurl_source: declared
  description: Babylon Phase-1 API endpoints (Deprecated)
  name: Babylon Labs v1 API
  slug: babylon-labs-v1-api
- baseURL: https://staking-api.babylonlabs.io
  baseurl_source: declared
  description: Babylon Phase-2 API endpoints
  name: Babylon Labs v2 API
  slug: babylon-labs-v2-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Babylon Staking shared API
  slug: open-babylon-labs-shared-api
- collection_type: open
  name: Babylon Staking shared v1 API
  slug: open-babylon-labs-v1-api
- collection_type: open
  name: Babylon Staking shared v2 API
  slug: open-babylon-labs-v2-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/agentic-access/babylon-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/babylon-labs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/security/babylon-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babylon-labs-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/llms/babylon-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babylon-labs-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/packages/babylon-labs-packages.yml
  title: ''
  type: Packages
  url: packages/babylon-labs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/packages/babylon-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/babylon-labs-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/errors/babylon-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/babylon-labs-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/conventions/babylon-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/babylon-labs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/lifecycle/babylon-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/babylon-labs-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/lifecycle/babylon-labs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/babylon-labs-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/conformance/babylon-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/babylon-labs-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/data-model/babylon-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/babylon-labs-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/mcp/babylon-labs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/babylon-labs-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/overlays/babylon-labs-staking-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/babylon-labs-staking-api-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/changelog/babylon-labs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/babylon-labs-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.babylonlabs.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.babylonlabs.io/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.babylonlabs.io/stakers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/babylonlabs-io
- group: company
  title: ''
  type: Blog
  url: https://babylonlabs.io/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/babylonglobal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babylonlabs.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babylonlabs.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://babylonlabs.io
created: '2026-07-17'
description: Babylon Labs builds the Bitcoin staking protocol that lets BTC holders secure Proof-of-Stake networks without custody, bridges, or wrapping. BTC is locked in time-locked covenant scripts on Bitcoin L1 and delegated to finality providers, providing Bitcoin-grade economic security to Cosmos chains, rollups, and other Bitcoin Supercharged Networks (BSNs) while stakers retain self-custody. Its mainnet, Babylon Genesis, launched April 2025 on CometBFT with CosmWasm smart contracts and the BABY native token. Babylon exposes a public Babylon Staking API for querying delegations, finality providers, network parameters, stats, prices, and APR, plus Go and TypeScript SDKs, node/operator daemons, and CosmWasm contracts.
image: https://avatars.githubusercontent.com/u/175623330?v=4
layout: provider
modified: '2026-07-18'
name: Babylon Labs
nav: Providers
network: true
overview: 'Babylon Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: shared API, v1 API, and v2 API. Tagged areas include Company, Crypto Defi, Bitcoin, Bitcoin Staking, and Blockchain.


  Babylon Labs'' developer surface includes changelog, documentation, getting-started guide, engineering blog, support, and 19 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/babylon-labs/refs/heads/main/screenshots/babylon-labs-2026-07-25T202203.png
security:
- kind: domain-security
  name: Babylon Labs Domain Security
  slug: babylon-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: babylon-labs
tags:
- Company
- Crypto Defi
- Bitcoin
- Bitcoin Staking
- Blockchain
- Cosmos
- Proof of Stake
- DeFi
- Staking
website: https://babylonlabs.io
---
