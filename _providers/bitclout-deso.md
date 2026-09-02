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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The HTTP JSON API served by every DeSo node — data endpoints (profiles, posts, users, NFTs, creator/DAO coins, messages) plus transaction-construction endpoints. The public node is node.deso.org; tran
  name: DeSo Backend API
  slug: deso-backend-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.deso.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.deso.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deso.org/deso-backend/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deso.org/deso-backend/construct-transactions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deso.org/deso-tutorial-build-apps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deso-protocol
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.deso.org/deso-roadmap
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/HFxzBkW5BJ
- group: docs
  title: ''
  type: GraphQL
  url: https://graphql-prod.deso.com/graphql
- group: build
  title: ''
  type: Packages
  url: packages/bitclout-deso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitclout-deso-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitclout-deso-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitclout-deso-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitclout-deso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitclout-deso-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitclout-deso-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitclout-deso-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bitclout-deso-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitclout-deso-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bitclout-deso-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitclout-deso-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitclout-deso-domain-security.yml
created: '2026-07-17'
description: DeSo (Decentralized Social, formerly BitClout) is an open-source layer-1 blockchain purpose-built for storage-heavy applications such as social media, NFTs, creator coins, and on-chain financial primitives. It exposes a permissionless HTTP JSON API served by any DeSo node (the public node runs at node.deso.org/api/v0), a GraphQL endpoint, the DeSo Identity service for derived-key authentication and transaction signing, a client-side TypeScript SDK (deso-protocol), a Python SDK, a Rosetta API implementation for exchange integrations, and an official MCP server for AI-assisted development. Originally launched as the BitClout prototype and backed by Pantera Capital, the project rebranded to DeSo and now powers a broad ecosystem of decentralized social apps.
image: https://node.deso.org/assets/deso/camelcase_logo_og.jpg
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for DeSo blockchain development — exposes DeSo API documentation, SDK guidance, code generation, architecture, and UI/GraphQL helpers to AI coding agents.
  name: BitClout (DeSo) MCP Server
  slug: bitclout-deso-mcp-server
modified: '2026-07-18'
name: BitClout (DeSo)
nav: Providers
network: true
overview: 'BitClout (DeSo) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Decentralized Social, and Web3.


  BitClout (DeSo)''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, sandbox, and 15 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitclout-deso/refs/heads/main/screenshots/bitclout-deso-2026-07-25T203136.png
security:
- kind: authentication
  name: Bitclout Deso Authentication
  slug: bitclout-deso-authentication
  summary_line: derived-keys/message-signing · 3 schemes
- kind: domain-security
  name: Bitclout Deso Domain Security
  slug: bitclout-deso-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitclout-deso
tags:
- Company
- Crypto
- Blockchain
- Decentralized Social
- Web3
- Social-Media
- NFT
- Creator Economy
website: https://www.deso.com/
---
