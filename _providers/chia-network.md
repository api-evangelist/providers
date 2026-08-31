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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Local JSON-over-HTTPS RPC surface exposed by the chia-blockchain reference node. Each service (full_node, wallet, farmer, harvester, datalayer, crawler, timelord, solver) listens on its own port and i
  name: Chia RPC API
  slug: chia-rpc-api
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Chia-Network/chia-blockchain/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Chia-Network/chia-blockchain/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Chia-Network/chia-blockchain/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Chia-Network/chia-blockchain/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Chia-Network/chia-blockchain/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Chia-Network/chia-blockchain/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://chia.net/
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
  url: https://docs.chia.net/chia-blockchain/introduction/
- group: company
  title: ''
  type: Blog
  url: https://www.chia.net/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chia-Network
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Chia-Network/chia-blockchain
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chia.net/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chia.net/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chia.net/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Chia-Network/chia-blockchain/blob/main/CHANGELOG.md
- group: build
  title: ''
  type: Packages
  url: packages/chia-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chia-network-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/chia-network-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chia-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chia-network-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chia-network-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chia-network-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chia-network-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chia-network-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chia-network-llms.txt
created: '2026-07-17'
description: Chia Network is the company behind an open-source, decentralized blockchain that uses a Proof of Space and Time consensus model, letting participants "farm" with unused disk space instead of energy-intensive mining. Its reference implementation, chia-blockchain, runs a full node, farmer, harvester, timelord, and wallet, and exposes a set of local, TLS-certificate-secured JSON RPC services (full node, wallet, farmer, harvester, DataLayer, crawler, timelord, solver, and a WebSocket daemon) alongside the `chia` command-line interface and the Chialisp smart-contract language. Chia also builds tooling for tokenized carbon and climate applications (Climate Action Data Trust). The developer surface centers on the RPC APIs, official Python and Rust packages, and an extensive GitHub organization rather than a public hosted API.
image: https://www.chia.net/wp-content/uploads/2022/09/chia-logo.svg
layout: provider
modified: '2026-07-18'
name: Chia Network
nav: Providers
network: true
overview: 'Chia Network publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Blockchain, Cryptocurrency, and Decentralized.


  Chia Network''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, CLI, authentication, and 21 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 6.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 100.0
  previous_composite: 30.6
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/chia-network/refs/heads/main/screenshots/chia-network-2026-07-25T205208.png
security:
- kind: authentication
  name: Chia Network Authentication
  slug: chia-network-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Chia Network Domain Security
  slug: chia-network-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chia-network
tags:
- Company
- Frontier Tech
- Blockchain
- Cryptocurrency
- Decentralized
- Web3
- Developer Tools
- Open-Source
website: https://chia.net/
---
