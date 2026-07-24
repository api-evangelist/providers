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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Integration-specific datasets (Kelp, ether.fi).
  name: Sommelier Integrations API
  slug: sommelier-integrations-api
- description: Protocol-wide metrics such as total value locked.
  name: Sommelier Protocol API
  slug: sommelier-protocol-api
- description: Daily and hourly performance snapshots of Sommelier vaults (cellars).
  name: Sommelier Vault Data API
  slug: sommelier-vault-data-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.somm.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sommelier.finance/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sommelier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sommelier-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sommelier-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sommelier-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sommelier-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sommelier-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sommelier-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sommelier-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sommelier (rebranding to "Somm") is a decentralized asset-management and DeFi vault protocol whose smart-contract "cellars" run automated yield strategies on Ethereum. It publishes a public, read-only HTTP API that exposes on-chain vault performance data — daily and hourly snapshots (APY, TVL, share price, total assets), protocol-wide total value locked, per-cellar snapshots, and integration datasets for Kelp and ether.fi points and balances. All endpoints are unauthenticated GET requests with path-based parameters and a { "Response": ... } envelope; the API currently serves the ethereum network. Backed by Multicoin Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sommelier.png
layout: provider
mcp_servers:
- description: ''
  name: sommelier-mcp.yml
  slug: sommelier-mcpyml
modified: '2026-07-21'
name: Sommelier
nav: Providers
network: true
overview: 'Sommelier publishes 3 APIs on the [APIs.io](https://apis.io/) network: Integrations API, Protocol API, and Vault Data API. Tagged areas include Company, Crypto Web3, DeFi, Blockchain, and Ethereum.


  Sommelier''s developer surface includes authentication and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 49.3
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sommelier Authentication
  slug: sommelier-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Sommelier Domain Security
  slug: sommelier-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: sommelier
tags:
- Company
- Crypto Web3
- DeFi
- Blockchain
- Ethereum
- Vaults
- Yield
- Analytics
website: https://www.somm.finance
---
