---
agent_readiness:
  band: agent-ready
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-09-14'
api_count: 2
apis:
- baseURL: https://mainnet.aeternity.io/v3
  baseurl_source: declared
  description: The public HTTP API of the æternity node (v7.3.0) — 79 unauthenticated operations covering chain and generation queries, transaction submission and inspection, account state and nonces, contract calls
  name: Aeternity Node API
  slug: aeternity-node-api
- baseURL: https://mainnet.aeternity.io/mdw/v3
  baseurl_source: declared
  description: ae_mdw, the æternity middleware (v1.108.2) — an indexing layer over the node exposing 76 unauthenticated REST operations for transactions, blocks, accounts, activities, AEX-9/AEX-141 tokens, DEX swaps
  name: Aeternity Middleware API
  slug: aeternity-middleware-api
- description: A remote Model Context Protocol endpoint published on aeternity.com and advertised through RFC 9728 protected-resource metadata and RFC 8414 authorization-server metadata. The endpoint is OAuth 2.1 ga
  name: Aeternity MCP Server
  slug: aeternity-mcp-server
artifact_total: 10
asyncapis:
- description: The æternity middleware (ae_mdw) WebSocket subscription stream. Clients subscribe to chain events and receive an asynchronous notification each time one occurs. Every event is published TWICE — once w
  name: Aeternity Middleware WebSocket API
  slug: aeternity-middleware-websocket-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://aeternity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aeternity.com/aeternity-developer-tools
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aeternity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.aeternity.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aeternity.com/aeternity-developer-tools/quick-start-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeternity
- group: company
  title: ''
  type: Blog
  url: https://blog.aeternity.com/
- group: operate
  title: ''
  type: Support
  url: https://forum.aeternity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeternity.com/legal-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeternity.com/legal-privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aeternity.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/lifecycle/aeternity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aeternity-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/changelog/aeternity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aeternity-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/packages/aeternity-packages.yml
  title: ''
  type: Packages
  url: packages/aeternity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/packages/aeternity-packages.yml
  title: ''
  type: SDKs
  url: packages/aeternity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/cli/aeternity-cli.yml
  title: ''
  type: CLI
  url: cli/aeternity-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/sandbox/aeternity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aeternity-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/llms/aeternity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeternity-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/well-known/aeternity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeternity-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/conformance/aeternity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeternity-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/security/aeternity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeternity-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/scopes/aeternity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aeternity-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/rate-limits/aeternity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aeternity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/plans/aeternity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeternity-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/authentication/aeternity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aeternity-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/conventions/aeternity-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aeternity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/conventions/aeternity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aeternity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/errors/aeternity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aeternity-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/data-model/aeternity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aeternity-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/mcp/aeternity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aeternity-mcp.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/asyncapi/aeternity-middleware-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/aeternity-middleware-websocket-asyncapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/overlays/aeternity-node-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeternity-node-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aeternity/refs/heads/main/overlays/aeternity-middleware-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeternity-middleware-overlay.yaml
created: '2026-09-12'
description: 'æternity is an open-source layer-1 blockchain platform, launched in 2018 and stewarded by the Aeternity Foundation, whose protocol ships two public, unauthenticated HTTP APIs: the æternity node API (OpenAPI 3.0, 79 operations across chain, transaction, account, contract, oracle, naming-system, state-channel and node-operator surfaces) and the æternity Middleware (ae_mdw) API (OpenAPI 3.0, 76 REST operations plus an open GraphQL endpoint with 85 query fields and a WebSocket subscription stream). The platform adds the Sophia smart-contract language, the FATE virtual machine, state channels, protocol-native oracles, the æternity Naming System (AENS) and Hyperchains, and is consumed through first-party JavaScript/TypeScript, CLI and calldata SDKs published to npm, plus the æScan explorer, ÆStudio IDE and Superhero wallet/DEX.'
image: https://aeternity.com/wp-content/uploads/2022/05/aeternity-social-thumb.webp
layout: provider
mcp_servers:
- description: ''
  name: Aeternity MCP Server
  slug: aeternity-mcp-server
modified: '2026-09-12'
name: Aeternity
nav: Providers
network: true
overview: 'Aeternity publishes 2 APIs on the [APIs.io](https://apis.io/) network: Node API and Middleware API. Tagged areas include Blockchain, Layer 1, Smart Contracts, Cryptocurrency, and Web3.


  The Aeternity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aeternity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, CLI, and 27 more developer resources.'
plans:
- name: Aeternity Plans Pricing
  plan_count: 0
  slug: aeternity-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Aeternity Rate Limits
  slug: aeternity-rate-limits
scopes:
- name: Aeternity Scopes
  scope_count: 0
  slug: aeternity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 56.7
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 65.8
  previous_composite: 50.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aeternity Authentication
  slug: aeternity-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aeternity Domain Security
  slug: aeternity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aeternity
tags:
- Blockchain
- Layer 1
- Smart Contracts
- Cryptocurrency
- Web3
- Distributed Ledger
- Open-Source
- GraphQL
- State Channels
- Oracles
- Naming System
- Developer Tools
website: https://aeternity.com/
---
