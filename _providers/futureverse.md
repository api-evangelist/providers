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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Relay-compliant GraphQL API for the Asset Register — a metadata ledger that defines what an asset is, what it can do, and which environments it works in, across chains and for off-chain assets. 29 que
  name: Futureverse Asset Register API
  slug: futureverse-asset-register-api
- description: FuturePass is Futureverse's smart-wallet identity system, exposed to developers as a standards compliant OpenID Connect provider. The discovery document at login.futureverse.app advertises authorizati
  name: FuturePass Identity (OpenID Connect)
  slug: futurepass-identity-openid-connect
- description: Public archive-node RPC for The Root Network mainnet, exposing both the Substrate JSON-RPC surface (author, babe, chain, state, system and custom nft/dex/fee-proxy methods over HTTP and WebSocket) and
  name: The Root Network Node RPC
  slug: the-root-network-node-rpc
- description: Remote, unauthenticated Model Context Protocol server on the documentation host exposing three tools — documentation search, a read-only virtual filesystem over the docs corpus, and a feedback submitt
  name: The Root Network Documentation MCP Server
  slug: the-root-network-documentation-mcp-server
- description: Public campaign detail. Campaigns group quests but hold no balances.
  name: Futureverse Campaigns API
  slug: futureverse-campaigns-api
- description: Quest detail, public quest discovery, and point allocation.
  name: Futureverse Quests API
  slug: futureverse-quests-api
artifact_total: 14
asyncapis:
- description: ''
  name: Futureverse Asset Register Events
  slug: futureverse-asset-register-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.futureverse.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.therootnetwork.com/intro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.therootnetwork.com/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.therootnetwork.com/build/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.therootnetwork.com/build/substrate/api-reference/json-rpc
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.therootnetwork.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/futureverse-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/futureverse-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/futureverse-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/futureverse-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/futureverse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/futureverse-packages.yml
- group: design
  title: ''
  type: Components
  url: components/futureverse-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/futureverse-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/futureverse-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/futureverse-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/futureverse-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/futureverse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/futureverse-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/futureverse-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/futureverse-asset-register-events.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/futureverse-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/futureverse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/futureverse-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/futureverse-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/TheRootNetwork
- group: other
  title: ''
  type: Listing
  url: https://www.hiive.com/securities/futureverse-stock
created: '2026-08-16'
description: 'Futureverse is a New Zealand-founded "open metaverse" technology company that rolled up eleven startups after a US$54M raise in 2023 and built The Root Network (TRN), a Substrate-based layer-1 blockchain with an EVM layer, any-token gas, and native NFT/SFT, DEX and bridge protocols. Its developer surface is three products: the Asset Register, a Relay-compliant GraphQL API for cross-chain asset metadata, schemas and asset-to-asset links; FuturePass, an OpenID Connect identity and smart-wallet provider; and RootRewards, a points/quest REST API for partner applications. Futureverse Corporation was placed in receivership on 2025-09-30 and in liquidation on 2025-12-16. Its corporate website and its original developer documentation host are both offline, but the TRN documentation, the Asset Register GraphQL endpoint, the FuturePass OIDC provider, the mainnet RPC nodes and 35 npm packages remain live and publicly reachable.'
image: https://mintlify.s3.us-west-1.amazonaws.com/therootnetwork/images/trn-hero.png
layout: provider
mcp_servers:
- description: ''
  name: Futureverse MCP Server
  slug: futureverse-mcp-server
- description: ''
  name: The Root Network
  slug: the-root-network
modified: '2026-08-16'
name: Futureverse
nav: Providers
network: true
overview: 'Futureverse publishes 2 APIs on the [APIs.io](https://apis.io/) network: Campaigns API and Quests API. Tagged areas include Blockchain, Web3, metaverse, digital-assets, and nft.


  The Futureverse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Futureverse''s developer surface includes documentation, getting-started guide, API reference, changelog, authentication, sandbox, support, and 21 more developer resources.'
plans:
- name: Futureverse Plans Pricing
  plan_count: 0
  slug: futureverse-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Futureverse Rate Limits
  slug: futureverse-rate-limits
scopes:
- name: Futureverse Scopes
  scope_count: 0
  slug: futureverse-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 30.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 32.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/futureverse/refs/heads/main/screenshots/futureverse-2026-08-17T080945.png
security:
- kind: authentication
  name: Futureverse Authentication
  slug: futureverse-authentication
  summary_line: openIdConnect/oauth2/apiKey/http · 6 schemes
- kind: domain-security
  name: Futureverse Domain Security
  slug: futureverse-domain-security
  summary_line: TLSv1.3 · HSTS
slug: futureverse
tags:
- Blockchain
- Web3
- metaverse
- digital-assets
- nft
- graphql
- Identity
- openid-connect
- asset-registry
- layer-1
- EVM
- Gaming
- agent-native
- MCP
website: https://www.futureverse.com/
---
