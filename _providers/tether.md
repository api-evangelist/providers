---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The API Keys API from Tether — 2 operation(s) for api keys.
  name: Tether API Keys API
  slug: tether-api-keys-api
- description: Supported blockchains and token discovery
  name: Tether Chains API
  slug: tether-chains-api
- description: Server health and status checks
  name: Tether Health API
  slug: tether-health-api
- description: Query current token balances for addresses
  name: Tether Token Balances API
  slug: tether-token-balances-api
- description: Query token transfer history for addresses
  name: Tether Token Transfers API
  slug: tether-token-transfers-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WDK Indexer API Keys API
  slug: open-tether-api-keys-api
- collection_type: open
  name: WDK Indexer Chains API
  slug: open-tether-chains-api
- collection_type: open
  name: WDK Indexer Health API
  slug: open-tether-health-api
- collection_type: open
  name: WDK Indexer Token Balances API
  slug: open-tether-token-balances-api
- collection_type: open
  name: WDK Indexer Token Transfers API
  slug: open-tether-token-transfers-api
common:
- group: company
  title: ''
  type: Website
  url: https://tether.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wdk.tether.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wdk.tether.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wdk.tether.io/sdk/all-modules
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wdk.tether.io/sdk/get-started
- group: operate
  title: ''
  type: Support
  url: https://docs.wdk.tether.io/overview/support
- group: company
  title: ''
  type: Blog
  url: https://tether.io/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tetherto
- group: start
  title: ''
  type: SignUp
  url: https://wdk-api.tether.io/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tether.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tether.io/privacy/
- group: auth
  title: ''
  type: Security
  url: https://tether.io/bug-bounty/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tether-wdk-indexer-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tether-wdk-indexer-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tether-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tether-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tether-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tether-cli.yml
- group: design
  title: ''
  type: Components
  url: components/tether-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tether-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tether-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tether-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tether-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tether-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tether-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tether-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tether-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tether-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tether-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tether-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tether-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tether-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tether-vulnerability-disclosure.yml
created: '2026-08-05'
description: Tether Operations Limited is the issuer of USD₮ (USDT), the largest stablecoin by circulating supply, along with XAU₮ (gold-backed), USA₮ and EUR₮ tokens issued across Ethereum, Tron, TON, Solana, Bitcoin/Liquid, Avalanche, Polygon, Arbitrum, Plasma and other chains. Beyond token issuance, Tether ships a developer surface centred on the open-source Wallet Development Kit (WDK) — a modular, self-custodial multi-chain wallet framework distributed as @tetherto/* npm packages, a WDK CLI, a React Native UI kit, an MCP Toolkit that exposes 35 wallet, pricing, indexer, swap, bridge, lending and fiat tools to AI agents, a published Agent Skill, and the hosted WDK Indexer REST API (wdk-api.tether.io) for token balances and transfer history. Tether also operates the QVAC local-AI SDK, the Tether Wallet app, and a public bug-bounty program.
image: https://tether.io/wp-content/themes/tether-io-theme/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Tether MCP Server
  slug: tether-mcp-server
modified: '2026-08-05'
name: Tether
nav: Providers
network: true
overview: 'Tether publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Chains API, Health API, and 2 more. Tagged areas include Company, Stablecoins, Cryptocurrency, Blockchain, and Wallets.


  Tether''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 27 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 6
  name: Tether Rate Limits
  slug: tether-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 48.4
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 55.0
  provenance:
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tether/refs/heads/main/screenshots/tether-2026-08-17T082328.png
security:
- kind: authentication
  name: Tether Authentication
  slug: tether-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tether Domain Security
  slug: tether-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tether Vulnerability Disclosure
  slug: tether-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: tether
tags:
- Company
- Stablecoins
- Cryptocurrency
- Blockchain
- Wallets
- Digital Assets
- Payments
- Self-Custody
- Multi-Chain
- Agents
- MCP
- Open-Source
website: https://tether.io/
---
