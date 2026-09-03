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
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.mainnet.valora.xyz
  baseurl_source: declared
  description: Divvi Hooks API (positions and shortcuts), served under /hooks-api
  name: Valora hooks API
  slug: valora-hooks-api
- baseURL: https://api.mainnet.valora.xyz
  baseurl_source: declared
  description: NFTs held by an address
  name: Valora nfts API
  slug: valora-nfts-api
- baseURL: https://api.mainnet.valora.xyz
  baseurl_source: declared
  description: Swap quotes
  name: Valora swaps API
  slug: valora-swaps-api
- baseURL: https://api.mainnet.valora.xyz
  baseurl_source: declared
  description: Token metadata and prices
  name: Valora tokens API
  slug: valora-tokens-api
- baseURL: https://api.mainnet.valora.xyz
  baseurl_source: declared
  description: Transaction simulation
  name: Valora transactions API
  slug: valora-transactions-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Valora hooks API
  slug: open-valora-hooks-api
- collection_type: open
  name: Valora hooks nfts API
  slug: open-valora-nfts-api
- collection_type: open
  name: Valora hooks swaps API
  slug: open-valora-swaps-api
- collection_type: open
  name: Valora hooks tokens API
  slug: open-valora-tokens-api
- collection_type: open
  name: Valora hooks transactions API
  slug: open-valora-transactions-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valora.xyz
- group: company
  title: ''
  type: Blog
  url: https://valora.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://support.valoraapp.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valora.xyz/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valora.xyz/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valora-xyz
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/valora-xyz/wallet/tree/main/docs
- group: build
  title: ''
  type: Packages
  url: packages/valora-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/valora-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/valora-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valora-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/valora-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/valora-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/valora-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valora-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/valora-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/valora-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valora-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/valora-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valora-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/valora-price-defi-positions.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/valora-discover-and-trigger-shortcuts.md
created: '2026-07-17'
description: Valora is an open-source, self-custodial mobile crypto wallet focused on making digital assets and peer-to-peer payments simple and accessible from a phone. Born in the Celo ecosystem and now multichain (Celo, Ethereum, Arbitrum, Optimism, Base, Polygon), it pairs the wallet app with a public API for token prices, swap quotes, NFTs, and transaction simulation, plus the Divvi Hooks platform that lets developers extend the app with position-pricing and shortcut hooks. Valora Inc is backed by a16z and Polychain.
image: https://avatars.githubusercontent.com/u/85907816?v=4
layout: provider
mcp_servers:
- description: ''
  name: Valora MCP Server
  slug: valora-mcp-server
modified: '2026-07-21'
name: Valora
nav: Providers
network: true
overview: 'Valora publishes 5 APIs on the [APIs.io](https://apis.io/) network, including hooks API, nfts API, swaps API, and 2 more. Tagged areas include Company, Cryptocurrency, Wallets, Payments, and DeFi.


  Valora''s developer surface includes engineering blog, support, documentation, sandbox, changelog, authentication, and 17 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 12.7
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 27.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valora/refs/heads/main/screenshots/valora-2026-09-02T165333.png
security:
- kind: authentication
  name: Valora Authentication
  slug: valora-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Valora Domain Security
  slug: valora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: valora
tags:
- Company
- Cryptocurrency
- Wallets
- Payments
- DeFi
- Blockchain
- Celo
- Mobile
website: https://valora.xyz
---
