---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Local JSON-RPC servers exposed by the Chia reference client for the full node, wallet, farmer, harvester, DataLayer, DID, NFT, offers, DAO, VC and simulator services. All calls are POST JSON over HTTP
  name: Chia JSON-RPC API
  slug: chia-json-rpc-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.chia.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chia.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chia.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chia.net/rpc/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chia.net/guides/crash-course/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.chia.net/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chia-Network
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chia.net/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chia.net/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/chia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/chia-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/chia-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chia-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chia-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chia-llms.txt
created: '2026-07-17'
description: Chia Network is the company behind the Chia blockchain, a decentralized layer-1 network whose native coin is XCH. Chia replaces energy-intensive Proof of Work with Nakamoto-consensus Proof of Space and Time, letting participants "farm" with standard disk hardware. The open-source Python reference client runs a full node, farmer, harvester, timelord and wallet and exposes a local JSON-RPC API (secured with mutual TLS) across full-node, wallet, farmer, harvester, DataLayer, DID, NFT, offers, DAO, VC and simulator services, plus the `chia` command-line client. On-chain smart transactions are authored in Chialisp / CLVM, and the network supports CATs (tokens), NFTs, DIDs, offers, DataLayer and DAOs. Chia was surfaced as a portfolio company of a16z and Greylock and enriched from its public developer surface.
image: https://www.chia.net/wp-content/uploads/2022/09/chia-logo.svg
layout: provider
modified: '2026-07-18'
name: Chia
nav: Providers
network: true
overview: 'Chia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Cryptocurrency, Web3, and Decentralized.


  Chia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, sandbox, authentication, and 13 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 28.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chia/refs/heads/main/screenshots/chia-2026-07-25T205207.png
security:
- kind: authentication
  name: Chia Authentication
  slug: chia-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Chia Domain Security
  slug: chia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chia
tags:
- Company
- Blockchain
- Cryptocurrency
- Web3
- Decentralized
- JSON-RPC
- Developer Tools
- Open-Source
website: https://www.chia.net/
---
