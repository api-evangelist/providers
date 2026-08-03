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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: Share transaction logs
  name: Teahouse Finance Logs API
  slug: teahouse-logs-api
- description: Vault performance time series
  name: Teahouse Finance Performance API
  slug: teahouse-performance-api
- description: Vault catalog and metadata
  name: Teahouse Finance Vaults API
  slug: teahouse-vaults-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teahouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teahouse.finance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teahouse.finance/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teahouse.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.teahouse.finance/docs/vault-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.teahouse.finance/docs/for-developers/vault-api-introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TeahouseFinance
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@teahouse.finance
- group: operate
  title: ''
  type: Support
  url: https://docs.teahouse.finance/docs/other-information/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://vault.teahouse.finance/
- group: auth
  title: ''
  type: Authentication
  url: authentication/teahouse-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teahouse-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teahouse-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teahouse-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teahouse-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teahouse-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teahouse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teahouse-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Teahouse Finance, founded in 2021, is a multi-strategy DeFi asset-management platform that sits as a simplified layer above protocols such as Uniswap V3, removing the complexity of managing liquidity and crypto assets. It runs audited smart-contract vaults across multiple chains — LP Vaults, Portfolio Vaults, the Easy-Earn delta-neutral strategy, and Tea-REX — for both individual and enterprise clients. Teahouse exposes a public read-only Vault API (HTTP/JSON) over its permissionless vaults: the vault catalog, per-vault performance time series (TVL, fee APR, share-token APR, share price), and account/vault share transaction logs. Vaults are of type V3Pair (a single Uniswap V3 LP pair) or V3Port (a portfolio of multiple positions). Surfaced as a portfolio company of Pantera Capital and enriched into the API Evangelist network from its published developer documentation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teahouse.png
layout: provider
mcp_servers:
- description: ''
  name: teahouse-mcp.yml
  slug: teahouse-mcpyml
modified: '2026-07-21'
name: Teahouse Finance
nav: Providers
network: true
overview: 'Teahouse Finance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Logs API, Performance API, and Vaults API. Tagged areas include Company, Crypto, DeFi, Blockchain, and Vaults.


  Teahouse Finance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 12 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 62.8
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 40.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Teahouse Authentication
  slug: teahouse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Teahouse Domain Security
  slug: teahouse-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: teahouse
tags:
- Company
- Crypto
- DeFi
- Blockchain
- Vaults
- Liquidity Management
- Asset Management
- Uniswap
- Web3
website: https://teahouse.finance/
---
