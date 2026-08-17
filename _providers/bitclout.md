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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The HTTP API served by every DeSo node. It exposes transaction-construction endpoints (social, financial, NFT, DAO/token, associations, derived keys) and read/data endpoints (users, posts, profiles, N
  name: DeSo Backend API
  slug: deso-backend-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitclout-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.deso.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deso.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deso.org/deso-backend/api
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
- group: company
  title: ''
  type: Blog
  url: https://deso.org
- group: start
  title: ''
  type: SignUp
  url: https://identity.deso.org/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitclout-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/bitclout-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitclout-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitclout-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitclout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitclout-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitclout-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitclout-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitclout-data-model.yml
created: '2026-07-17'
description: 'BitClout is the original social-token network that launched the DeSo (Decentralized Social) blockchain, an open, layer-1 chain purpose-built for storing social data — profiles, posts, follows, creator coins, NFTs, and messages — fully on-chain. Backed by a16z and other top venture firms, the project rebranded to DeSo and exposes everything through an API-first, permissionless developer surface: a JSON HTTP backend API served by every node (transaction construction plus read/data endpoints), the DeSo Identity Service for key management and transaction signing, a first-party TypeScript/JavaScript SDK (deso-protocol), a Rosetta API implementation for exchange integration, an open-source core node, and a hosted MCP server for agent-based development. Openfund, a fully on-chain order-book DEX, is the flagship application built on the stack.'
image: https://avatars.githubusercontent.com/u/72720753?v=4
layout: provider
mcp_servers:
- description: ''
  name: bitclout-mcp.yml
  slug: bitclout-mcpyml
modified: '2026-07-18'
name: BitClout
nav: Providers
network: true
overview: 'BitClout publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Web3, Decentralized Social, and Social.


  BitClout''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 125
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitclout/refs/heads/main/screenshots/bitclout-2026-07-25T203135.png
security:
- kind: authentication
  name: Bitclout Authentication
  slug: bitclout-authentication
  summary_line: derived-keys/transaction-signing · 3 schemes
- kind: domain-security
  name: Bitclout Domain Security
  slug: bitclout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitclout
tags:
- Company
- Blockchain
- Web3
- Decentralized Social
- Social
- Cryptocurrency
- NFT
- Creator Economy
- Identity
- Developer Tools
website: https://docs.deso.org/
---
