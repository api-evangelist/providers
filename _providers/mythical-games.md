---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: gRPC/Protobuf API of the Mythical Platform (Saga SDK) for issuing, transferring, and burning game items and currencies, managing item/currency types and minting, creating marketplace listings and offe
  name: Mythical Saga Platform API
  slug: mythical-saga-platform-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/MythicalGames/saga-sdk-proto/issues
- group: company
  title: ''
  type: Website
  url: https://mythicalgames.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/MythicalGames
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MythicalGames
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MythicalGames/saga-sdk-proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/saga/
- group: build
  title: ''
  type: Packages
  url: packages/mythical-games-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mythical-games-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mythical-games-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mythical-games-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mythical-games-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mythical-games-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mythical-games-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mythical-games-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mythical-games-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mythical-games-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mythical-games-lifecycle.yml
- group: other
  title: ''
  type: Marketplace
  url: https://mythical.market/
- group: company
  title: ''
  type: Blog
  url: https://mythicalgames.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mythicalgames.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mythicalgames.com/privacy
- group: other
  title: ''
  type: Blockchain
  url: https://mythos.foundation
created: '2026-07-17'
description: 'Mythical Games is a Web3 game-technology studio and platform company (an a16z portfolio company) that builds games with player-owned digital items and a secondary marketplace economy. Its business has two sides: consumer game titles (FIFA Rivals, Pudgy Party, Blankos) and the Mythical Platform, a B2B toolkit that lets any game add a secondary economy of tradeable items and currencies. The platform is exposed to integrating studios primarily through gRPC/Protobuf SDKs — the Saga SDK and the earlier IVI SDK — published for Java, C++, and Python, rather than a public REST/OpenAPI surface. The Saga gRPC API covers items, item types, currencies, currency types, listings, offers, player wallets, reservations, an NFT bridge, and metadata, with cursor-based queries and a server-streaming status channel for confirming asynchronous writes. Assets settle on the Mythos chain, a Polkadot/Substrate gaming parachain (MYTH token) whose node software is open source.'
image: https://mythicalgames.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Mythical Games MCP Server
  slug: mythical-games-mcp-server
modified: '2026-07-20'
name: Mythical Games
nav: Providers
network: true
overview: 'Mythical Games publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Web3, Blockchain, and Digital Assets.


  Mythical Games'' developer surface includes authentication, engineering blog, and 21 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 26.3
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 26.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mythical-games/refs/heads/main/screenshots/mythical-games-2026-08-07T184545.png
security:
- kind: authentication
  name: Mythical Games Authentication
  slug: mythical-games-authentication
  summary_line: sdk-credential · 1 scheme
- kind: domain-security
  name: Mythical Games Domain Security
  slug: mythical-games-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mythical-games
tags:
- Company
- Gaming
- Web3
- Blockchain
- Digital Assets
- NFT
- Marketplace
- gRPC
- SDK
- Game Platform
website: https://mythicalgames.com/
---
