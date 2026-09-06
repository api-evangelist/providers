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
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Native GraphQL API served by the Mina daemon (default port 3085) to query blockchain data — accounts, blocks, transactions, pending pool, daemon status — and submit signed transactions including zkApp
  name: Mina GraphQL API
  slug: mina-graphql-api
- description: First-party implementation of the Coinbase Rosetta API (Data API + Construction API) for blockchain integration, historical data queries, and exchange support.
  name: Mina Rosetta API
  slug: mina-rosetta-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mina-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://minaprotocol.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.minaprotocol.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.minaprotocol.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.minaprotocol.com/node-operators/validator-node/querying-data
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.minaprotocol.com/zkapps/writing-a-zkapp/introduction-to-zkapps/getting-started-zkapps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MinaProtocol
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mina-protocol-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/mina-protocol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mina-protocol-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mina-protocol-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mina-protocol-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mina-protocol-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mina-protocol-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mina-protocol-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mina-protocol-llms.txt
created: '2026-07-17'
description: Mina Protocol is a lightweight, layer-1 blockchain powered by zero-knowledge proofs (zk-SNARKs) that maintains a constant ~22KB chain size regardless of usage, using the Ouroboros Samasika proof-of-stake consensus. Developers build privacy-preserving smart contracts called zkApps in TypeScript with the o1js framework, sign transactions with mina-signer, scaffold and deploy projects with the zkApp CLI, and integrate with the network through the Mina daemon's native GraphQL API and a first-party Coinbase Rosetta API implementation for exchanges and data indexing. Originally surfaced as a portfolio company of Multicoin Capital and enriched here from Mina's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mina-protocol.png
layout: provider
modified: '2026-07-20'
name: Mina Protocol
nav: Providers
network: true
overview: 'Mina Protocol publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Blockchain, Zero-Knowledge Proofs, and zk-SNARKs.


  Mina Protocol''s developer surface includes documentation, API reference, getting-started guide, changelog, CLI, sandbox, authentication, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mina-protocol/refs/heads/main/screenshots/mina-protocol-2026-08-07T172922.png
security:
- kind: authentication
  name: Mina Protocol Authentication
  slug: mina-protocol-authentication
  summary_line: signature · 2 schemes
- kind: domain-security
  name: Mina Protocol Domain Security
  slug: mina-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mina-protocol
tags:
- Company
- Crypto Web3
- Blockchain
- Zero-Knowledge Proofs
- zk-SNARKs
- Smart Contracts
- GraphQL
- Rosetta API
- Developer Tools
website: https://minaprotocol.com
---
