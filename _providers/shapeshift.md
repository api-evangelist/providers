---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Shapeshift Agentic Access
  operation_count: 25
  slug: shapeshift-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 1
apis:
- description: The v1 API from Shapeshift — 14 operation(s) for v1.
  name: Shapeshift v1 API
  slug: shapeshift-v1-api
artifact_total: 6
asyncapis:
- description: ''
  name: Shapeshift Unchained Webhooks
  slug: shapeshift-unchained-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shapeshift-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shapeshift-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shapeshift-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://shapeshift.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/shapeshift/unchained
- group: docs
  title: ''
  type: Documentation
  url: https://api.ethereum.shapeshift.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.ethereum.shapeshift.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/shapeshift/unchained#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shapeshift
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/shapeshift/unchained
- group: operate
  title: ''
  type: Support
  url: https://shapeshift.com/support
- group: company
  title: ''
  type: Blog
  url: https://shapeshift.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.shapeshift.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shapeshift.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shapeshift.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/shapeshift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shapeshift-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shapeshift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shapeshift-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/shapeshift-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shapeshift-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shapeshift-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shapeshift-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shapeshift-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shapeshift-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shapeshift-unchained-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shapeshift-ethereum-overlay.yaml
created: '2026-07-17'
description: ShapeShift is a community-owned, non-custodial multichain cryptocurrency platform where users buy, hold, trade, and earn with digital assets across 48+ blockchains and 10,000+ tokens while retaining full custody of their keys. Its open-source "unchained" backend exposes a public, key-free REST and WebSocket API that provides a common interface to many blockchains — account balances, transaction history, UTXOs, raw transaction broadcast, gas/fee estimation, and realtime pending/confirmed transaction updates — behind per-chain hosts such as api.ethereum.shapeshift.com and api.bitcoin.shapeshift.com. ShapeShift was founded in 2014, is backed by Earlybird Venture Capital, and today operates as a DAO with all code public under github.com/shapeshift.
image: https://shapeshift.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: shapeshift-mcp.yml
  slug: shapeshift-mcpyml
modified: '2026-07-21'
name: Shapeshift
nav: Providers
network: true
overview: 'Shapeshift publishes 1 API on the [APIs.io](https://apis.io/) network: v1 API. Tagged areas include Company, Cryptocurrency, Blockchain, Bitcoin, and Ethereum.


  The Shapeshift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shapeshift''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 54
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.8
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Shapeshift Authentication
  slug: shapeshift-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Shapeshift Domain Security
  slug: shapeshift-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: shapeshift
tags:
- Company
- Cryptocurrency
- Blockchain
- Bitcoin
- Ethereum
- Web3
- DeFi
- Wallet
- Trading
- Multichain
- API
website: https://shapeshift.com
---
