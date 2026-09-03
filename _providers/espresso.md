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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The public REST and WebSocket API served by Espresso query services and nodes (Tide Disco framework). Comprises independent modules — availability (Tiramisu DA blocks/headers/payloads/VID), node, stat
  name: Espresso Network Query Service API
  slug: espresso-network-query-service-api
artifact_total: 4
asyncapis:
- description: ''
  name: Espresso Events Webhooks
  slug: espresso-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.espressosys.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.espressosys.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.espressosys.com/network/developer/espresso-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.espressosys.com/network/developer/espresso-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.espressosys.com/network/learn/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EspressoSystems
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@espressosys
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.espressosys.com/network/network/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.espressosys.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/DRfcHRnnBz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/espresso-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/espresso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/espresso-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/espresso-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/espresso-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/espresso-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/espresso-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/espresso-events-webhooks.yml
created: '2026-07-17'
description: Espresso Systems builds the Espresso Network, a high-performance consensus and sequencing layer that gives rollups and institution-grade financial applications real-time settlement (~3 second finality) without sacrificing control, privacy, or connectivity to global onchain liquidity. The network is a permissionless delegated-proof-of-stake system (Mainnet 1.0, live) built on the HotShot BFT consensus protocol and the Tiramisu data-availability layer, confirming transactions for integrated Arbitrum Nitro/Orbit and OP Stack chains. Espresso nodes and query services expose a public, no-auth REST + WebSocket API (built on the Tide Disco framework) across modules for availability, node state, consensus status, catchup, explorer, events streaming, and transaction submission. The API is served on both the Ethereum-mainnet-anchored Mainnet and the Sepolia-anchored Decaf testnet, with content negotiation between JSON and binary and URL-path major versioning (v0 → v1).
image: https://www.espressosys.com/
layout: provider
modified: '2026-07-19'
name: Espresso
nav: Providers
network: true
overview: 'Espresso publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Web3, Infrastructure, and Consensus.


  The Espresso catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Espresso''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, authentication, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 35.5
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/espresso/refs/heads/main/screenshots/espresso-2026-07-25T213631.png
security:
- kind: authentication
  name: Espresso Authentication
  slug: espresso-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Espresso Domain Security
  slug: espresso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: espresso
tags:
- Company
- Blockchain
- Web3
- Infrastructure
- Consensus
- Sequencer
- Rollup
- Data Availability
- Ethereum
- DeFi
- REST API
- Cryptography
website: https://www.espressosys.com/
---
