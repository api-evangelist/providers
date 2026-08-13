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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Gallop Agentic Access
  operation_count: 32
  slug: gallop-agentic-access
  summary_line: 32 operations · 32 acting
api_count: 4
apis:
- description: The Ethereum API from Gallop — 28 operation(s) for ethereum.
  name: Gallop Ethereum API
  slug: gallop-ethereum-api
- description: The Polygon API from Gallop — 21 operation(s) for polygon.
  name: Gallop Polygon API
  slug: gallop-polygon-api
- description: The Solana API from Gallop — 18 operation(s) for solana.
  name: Gallop Solana API
  slug: gallop-solana-api
- description: The Starknet API from Gallop — 2 operation(s) for starknet.
  name: Gallop Starknet API
  slug: gallop-starknet-api
artifact_total: 9
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gallop-analytics-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://higallop.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gallop.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://gallop.readme.io
- group: docs
  title: ''
  type: APIReference
  url: https://gallop.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://gallop.readme.io/docs/api-quick-start
- group: start
  title: ''
  type: SignUp
  url: https://higallop.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://higallop.com/terms/
- group: operate
  title: ''
  type: Support
  url: mailto:support@higallop.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gallop-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gallop-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gallop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gallop-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gallop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gallop-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gallop-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gallop-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gallop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gallop-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gallop-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Gallop is an NFT data and analytics platform (backed by Amplify Partners) that provides composable data-aggregation, analytics and insight APIs so data engineers, developers and data scientists can rapidly deploy NFT products and experiences. Its REST APIs cover Ethereum, Solana, Polygon and Starknet across three surfaces: a Data API (collections, tokens, traits, transactions, wallet holdings, live listings, floor prices, ENS lookup), an Analytics API (collection/token summaries, rarity, wash-trade detection, OHLC candlesticks, leaderboards, wallet P&L) and an Insights API (token appraisal/liquidation estimates, wallet activity labels and wallet valuation). Authentication is via an x-api-key header, all operations are POST, and calls are limited to 5 requests/second. Note: as of mid-2026 the primary domain (higallop.com) is in registry redemption and the api.prod.gallop.run backend is unreachable, though the developer documentation remains published on ReadMe.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gallop.png
layout: provider
mcp_servers:
- description: ''
  name: gallop-mcp.yml
  slug: gallop-mcpyml
modified: '2026-07-19'
name: Gallop
nav: Providers
network: true
overview: 'Gallop publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Ethereum API, Polygon API, Solana API, and 1 more. Tagged areas include Company, Developer Tools, NFT, Blockchain, and Web3.


  Gallop''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 39
rate_limits:
- limit_count: 1
  name: Gallop Rate Limits
  slug: gallop-rate-limits
score:
  band: developing
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.2
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gallop/refs/heads/main/screenshots/gallop-2026-07-25T215406.png
security:
- kind: authentication
  name: Gallop Authentication
  slug: gallop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gallop Domain Security
  slug: gallop-domain-security
  summary_line: DMARC
slug: gallop
tags:
- Company
- Developer Tools
- NFT
- Blockchain
- Web3
- Data
- Analytics
- Crypto
- Ethereum
- Solana
website: https://higallop.com
---
