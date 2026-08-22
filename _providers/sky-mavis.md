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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: REST Web3 data API on the Ronin blockchain — query accounts, NFTs, tokens, collections, blocks, smart contracts and transactions. Authenticated with an X-API-KEY issued from the Ronin Developer Consol
  name: Ronin Skynet Web3 API
  slug: ronin-skynet-web3-api
- description: Ethereum-compatible JSON-RPC endpoint for the Ronin network — read chain state, submit transactions, call contracts, and subscribe to events. The public mainnet endpoint is openly reachable; gateway J
  name: Ronin JSON-RPC API
  slug: ronin-json-rpc-api
- description: OAuth2 / OpenID Connect account service and keyless wallet for onboarding players into Ronin games. Discovery is published at the athena.skymavis.com issuer; supports authorization_code, client_creden
  name: Ronin Waypoint Account Service
  slug: ronin-waypoint-account-service
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.roninchain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skymavis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skymavis.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skymavis.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skymavis
- group: operate
  title: ''
  type: StatusPage
  url: https://skymavis.statuspage.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.roninchain.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.skymavis.com/files/skymavis-terms-of-use-09012025.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.skymavis.com/files/skymavis-privacypolicy-10122024.pdf
- group: start
  title: ''
  type: SignUp
  url: https://developers.roninchain.com/
- group: build
  title: ''
  type: Packages
  url: packages/sky-mavis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sky-mavis-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sky-mavis-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sky-mavis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sky-mavis-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sky-mavis-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sky-mavis-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sky-mavis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sky-mavis-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sky-mavis-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/sky-mavis-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sky-mavis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sky-mavis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sky-mavis-domain-security.yml
created: '2026-07-17'
description: 'Sky Mavis is the studio behind Axie Infinity and Ronin, an EVM blockchain crafted for developers building games with player-owned economies. Its developer platform exposes a set of API-gateway products for building on Ronin: the Skynet Web3 API (query accounts, NFTs, tokens, blocks, contracts and transactions), a Ronin JSON-RPC API for node connectivity, the Axie Infinity Origins and AXP game-data APIs, Ronin Market and Ronin Store partner APIs, and Ronin Waypoint, an OAuth2/OIDC account service and keyless wallet for game onboarding. Access to gateway products is authenticated with an X-API-KEY issued from the Ronin Developer Console, while public JSON-RPC and the Waypoint OIDC surface are openly reachable. Official SDKs ship for JavaScript/TypeScript, Unity, Android and iOS.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sky-mavis.png
layout: provider
mcp_servers:
- description: ''
  name: sky-mavis-mcp.yml
  slug: sky-mavis-mcpyml
modified: '2026-07-21'
name: Sky Mavis
nav: Providers
network: true
overview: 'Sky Mavis publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Web3, Gaming, and NFT.


  Sky Mavis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, sandbox, and 18 more developer resources.'
random_paper: 8
scopes:
- name: Sky Mavis Scopes
  scope_count: 3
  slug: sky-mavis-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 36.1
  delta: 0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 68.5
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 35.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Sky Mavis Authentication
  slug: sky-mavis-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Sky Mavis Domain Security
  slug: sky-mavis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sky-mavis
tags:
- Company
- Blockchain
- Web3
- Gaming
- NFT
- Wallet
- JSON-RPC
- Cryptocurrency
- Developer Tools
website: https://developers.roninchain.com/
---
