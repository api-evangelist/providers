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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Allium Agentic Access
  operation_count: 8
  slug: allium-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: The Explorer API from Allium — 6 operation(s) for explorer.
  name: Allium Explorer API
  slug: allium-explorer-api
- description: The ping API from Allium — 1 operation(s) for ping.
  name: Allium ping API
  slug: allium-ping-api
- description: The Polygon API from Allium — 1 operation(s) for polygon.
  name: Allium Polygon API
  slug: allium-polygon-api
artifact_total: 13
asyncapis:
- description: ''
  name: Allium Webhooks
  slug: allium-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allium Explorer API
  slug: open-allium-explorer-api
- collection_type: open
  name: Allium Explorer ping API
  slug: open-allium-ping-api
- collection_type: open
  name: Allium Explorer Polygon API
  slug: open-allium-polygon-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/allium-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://allium.so
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.allium.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.allium.so/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.allium.so/api/developer/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.allium.so/api/developer/overview
- group: start
  title: ''
  type: SignUp
  url: https://app.allium.so/join
- group: company
  title: ''
  type: Blog
  url: https://www.allium.so/blog
- group: operate
  title: ''
  type: Support
  url: https://www.allium.so/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.allium.so/ai/machine-payments/endpoints-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allium.so/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allium.so/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.allium.so
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.allium.so/changelog/overview
- group: auth
  title: ''
  type: Compliance
  url: https://trust.allium.so/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/allium-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allium-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allium-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/allium-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allium-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allium-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allium-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allium-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allium-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allium-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allium-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/allium-openapi-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/allium-changelog.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allium-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/allium-webhooks.yml
created: '2026-07-17'
description: 'Allium is an enterprise blockchain data platform that transforms raw on-chain data from 150+ blockchains into verified, decision-grade intelligence for institutional finance. It indexes and decodes activity across 10,000+ protocols and exposes it through Realtime REST APIs (sub-second wallet balances, holdings, PnL, DeFi positions, NFTs, DEX trades and Hyperliquid data), Datastreams (Kafka/Pub-Sub/SNS/websocket event feeds), Beam custom pipelines, the Explorer/Datashares historical layer, and Allium Terminal for research. It also ships an AI layer: a hosted MCP server, packaged Agent Skills, and x402 machine-payment endpoints. Customers include Visa, Grayscale, Phantom, MetaMask, MoonPay and the Federal Reserve. Backed by Amplify Partners, Kleiner Perkins and Theory Ventures.'
image: https://www.allium.so/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Allium MCP Server
  slug: allium-mcp-server
modified: '2026-07-17'
name: Allium
nav: Providers
network: true
overview: 'Allium publishes 3 APIs on the [APIs.io](https://apis.io/) network: Explorer API, ping API, and Polygon API. Tagged areas include Company, Data Analytics, Blockchain, Crypto, and Web3.


  The Allium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Allium''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, pricing, and 24 more developer resources.'
random_paper: 14
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 58.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allium/refs/heads/main/screenshots/allium-2026-07-25T195712.png
security:
- kind: authentication
  name: Allium Authentication
  slug: allium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Allium Domain Security
  slug: allium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Allium Trust Center
  slug: allium-trust-center
  summary_line: SOC 1 Type 1, SOC 1 Type 2, SOC 2 Type 1, SOC 2 Type 2
slug: allium
tags:
- Company
- Data Analytics
- Blockchain
- Crypto
- Web3
- Data Infrastructure
- Real-Time Data
- Stablecoins
- DeFi
- Machine Payments
website: https://allium.so
---
