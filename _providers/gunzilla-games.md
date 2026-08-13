---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The public Ethereum-compatible JSON-RPC endpoint for the GUNZ L1 chain, an Avalanche subnet running Subnet-EVM. It inherits the full EVM API surface of an Ethereum node (eth_*, net_*, web3_*), plus th
  name: GUNZ Chain JSON-RPC API
  slug: gunz-chain-json-rpc-api
- description: 'GUNZScan is the GUNZ chain block explorer, referenced from Gunzilla''s own chain documentation as the official explorer. It runs Blockscout and exposes three anonymous, machine-readable read surfaces: '
  name: GUNZScan Explorer API
  slug: gunzscan-explorer-api
artifact_total: 8
asyncapis:
- description: ''
  name: Gunzilla Games Gunzscan Events
  slug: gunzilla-games-gunzscan-events
common:
- group: company
  title: ''
  type: Website
  url: https://gunzillagames.com/en/
- group: other
  title: ''
  type: Profile
  url: https://www.hiive.com/securities/gunzilla-games-stock
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gunbygunz.com/develop/
- group: docs
  title: ''
  type: Documentation
  url: https://gunbygunz.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://gunzscan.io/api-docs
- group: company
  title: ''
  type: Blog
  url: https://gameoffthegrid.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gunbygunz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gunbygunz.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gunbygunz.com/gunz-terms/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gunzilla-games-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gunzilla-games-security.txt
- group: auth
  title: ''
  type: Security
  url: security/gunzilla-games-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gunzilla-games-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gunzilla-games-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gunzilla-games-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gunzilla-games-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gunzilla-games-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gunzilla-games-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gunzilla-games-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gunzilla-games-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gunzilla-games-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gunzilla-games-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gunzilla-games-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/gunzilla-games-packages.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/gunzilla-games-gunzscan.graphql
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gunzilla-games-gunzscan-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gunzilla-games-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gunzilla-games-llms.txt
created: '2026-08-04'
description: 'Gunzilla Games is a AAA game developer founded in 2020 with studios in Frankfurt, Kyiv and London, best known for the cyberpunk battle-royale shooter Off The Grid. Alongside the game the studio operates GUNZ, a permissioned Avalanche L1 (subnet) blockchain purpose-built for game developers, with GUN as its native gas coin. The public technical surface is EVM-shaped: a public Ethereum/Subnet-EVM JSON-RPC node at rpc.gunzchain.io (chain ID 43419), a mirrored Avalanche-hosted RPC, and the GUNZScan block explorer at gunzscan.io, which exposes a Blockscout REST v2 API, an Etherscan-compatible module/action API, an open GraphQL endpoint and a WebSocket subscription surface. A gated marketplace/minting API sits behind api.gunztoken.io.'
image: https://storage.gunbygunz.com/gunz_symbol_320x320.png
layout: provider
mcp_servers:
- description: ''
  name: gunzilla-games-mcp.yml
  slug: gunzilla-games-mcpyml
modified: '2026-08-04'
name: Gunzilla Games
nav: Providers
network: true
overview: 'Gunzilla Games publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Blockchain, Web3, and EVM.


  The Gunzilla Games catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gunzilla Games'' developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 23 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 2
  name: Gunzilla Games Rate Limits
  slug: gunzilla-games-rate-limits
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 63.0
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 45.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gunzilla-games/refs/heads/main/screenshots/gunzilla-games-2026-08-07T165902.png
security:
- kind: authentication
  name: Gunzilla Games Authentication
  slug: gunzilla-games-authentication
  summary_line: none/network-allowlist/wallet-signature · 5 schemes
- kind: domain-security
  name: Gunzilla Games Domain Security
  slug: gunzilla-games-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gunzilla Games Vulnerability Disclosure
  slug: gunzilla-games-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gunzilla-games
tags:
- Company
- Gaming
- Blockchain
- Web3
- EVM
- Avalanche
- JSON-RPC
- GraphQL
- Block Explorer
- NFT
- Video Games
website: https://gunzillagames.com/en/
---
