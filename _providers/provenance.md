---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Public Cosmos SDK REST (LCD / gRPC-gateway), gRPC, and Tendermint RPC interface to the Provenance Blockchain. Query and broadcast transactions against the marker, metadata, exchange, ledger, name, att
  name: Provenance Blockchain API
  slug: provenance-blockchain-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://provenance.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.provenance.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.provenance.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.provenance.io/build/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.provenance.io/build/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/provenance-io
- group: operate
  title: ''
  type: Support
  url: https://docs.provenance.io/community/support
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/grpc/provenance-marker-query.proto
  title: ''
  type: Protobuf
  url: grpc/provenance-marker-query.proto
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/packages/provenance-packages.yml
  title: ''
  type: Packages
  url: packages/provenance-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/packages/provenance-packages.yml
  title: ''
  type: SDKs
  url: packages/provenance-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/mcp/provenance-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/provenance-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/llms/provenance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/provenance-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/conformance/provenance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/provenance-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/lifecycle/provenance-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/provenance-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/changelog/provenance-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/provenance-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/conventions/provenance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/provenance-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/data-model/provenance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/provenance-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/authentication/provenance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/provenance-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/security/provenance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/provenance-domain-security.yml
created: '2026-07-17'
description: Provenance Blockchain is a public, proof-of-stake blockchain purpose-built for financial services and the tokenization of real-world assets. Built on the Cosmos SDK with CometBFT consensus, it exposes its functionality through first-party modules including marker (token/marker issuance), metadata (asset registry and the p8e contract execution environment), exchange (on-chain order book), ledger, name, attribute, hold, trigger, and msgfees/flatfees. Applications integrate over the public Cosmos REST (LCD / gRPC-gateway) API at api.provenance.io, gRPC, and Tendermint RPC at rpc.provenance.io, and via first-party SDKs (Go, Kotlin gRPC client, Rust/CosmWasm provwasm bindings, and JavaScript wallet libraries). HASH is the native staking and gas token. The chain, protobuf data model, and SDKs are open source under the provenance-io GitHub organization.
image: https://avatars.githubusercontent.com/provenance-io
layout: provider
modified: '2026-07-20'
name: Provenance
nav: Providers
network: true
overview: 'Provenance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Financial-Services, Tokenization, and Real World Assets.


  Provenance''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, and 13 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/provenance/refs/heads/main/screenshots/provenance-2026-09-02T152236.png
security:
- kind: authentication
  name: Provenance Authentication
  slug: provenance-authentication
  summary_line: none-for-reads/signature-based-for-writes · 2 schemes
- kind: domain-security
  name: Provenance Domain Security
  slug: provenance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: provenance
tags:
- Company
- Blockchain
- Financial-Services
- Tokenization
- Real World Assets
- Cosmos SDK
- gRPC
- Web3
- DeFi
- Digital Assets
website: https://provenance.io/
---
