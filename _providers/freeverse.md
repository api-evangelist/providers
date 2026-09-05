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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Public GraphQL API maintained by the LAOS Foundation for Bridgeless Minting and Evolution of NFTs. Create collections, mint up to 700 NFTs atomically, evolve assets, broadcast to marketplaces, and run
  name: LAOS Network API
  slug: laos-network-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.laosnetwork.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.laosnetwork.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.laosnetwork.io/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.laosnetwork.io/api/write-queries/GettingStarted
- group: company
  title: ''
  type: Website
  url: https://laosnetwork.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freeverseio
- group: company
  title: ''
  type: Blog
  url: https://laosnetwork.io/blog
- group: operate
  title: ''
  type: Support
  url: https://laosnetwork.io/community
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/laosnetwork
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/freeverseio/LAOS-roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.laosnetwork.io/tokenomics/change-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/freeverse-changelog.yml
- group: other
  title: ''
  type: Whitepaper
  url: https://github.com/freeverseio/laos-whitepaper
- group: build
  title: ''
  type: SDKs
  url: packages/freeverse-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/freeverse-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freeverse-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/freeverse-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/freeverse-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/freeverse-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/freeverse-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/freeverse-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/freeverse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freeverse-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freeverse-domain-security.yml
created: '2026-07-17'
description: Freeverse is the team behind the LAOS Network, an EVM-compatible Polkadot parachain and public blockchain protocol for Bridgeless Minting and Evolution of digital assets (NFTs). Rather than bridging tokens between chains, LAOS lets applications mint and dynamically evolve NFTs whose ownership is enforced on established chains such as Ethereum and Polygon while the asset logic and gas costs live on LAOS. The LAOS Foundation maintains a public GraphQL API at api.laosnetwork.io that lets developers create collections, mint up to 700 NFTs in a single atomic operation, evolve existing assets, broadcast assets to marketplaces, and run read queries over an on-chain indexer. Read queries are open; write mutations require an API key. Freeverse originated as a Barcelona blockchain gaming and digital-ownership company (Living Assets, Crypto-soccer) and is a portfolio company of Earlybird Venture Capital.
image: https://laosnetwork.io/favicon.ico
layout: provider
modified: '2026-07-19'
name: Freeverse
nav: Providers
network: true
overview: 'Freeverse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, NFT, Web3, and Digital Assets.


  Freeverse''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 18 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 42.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 33.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freeverse/refs/heads/main/screenshots/freeverse-2026-07-25T215145.png
security:
- kind: authentication
  name: Freeverse Authentication
  slug: freeverse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freeverse Domain Security
  slug: freeverse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freeverse
tags:
- Company
- Blockchain
- NFT
- Web3
- Digital Assets
- Gaming
- GraphQL
- Polkadot
- Ethereum
- Tokenization
website: https://laosnetwork.io/
---
