---
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ajaib Agentic Access
  operation_count: 14
  slug: ajaib-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 3
apis:
- description: Retrieve general exchange information.
  name: Ajaib Market Info API
  slug: ajaib-market-info-api
- description: View, place and cancel spot orders and trades.
  name: Ajaib Spot Trading API
  slug: ajaib-spot-trading-api
- description: Check funds and assets held by the exchange client.
  name: Ajaib Wallet API
  slug: ajaib-wallet-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://ajaib.co.id/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ajaib.gitbook.io/coin-exchange
- group: docs
  title: ''
  type: Documentation
  url: https://ajaib.gitbook.io/coin-exchange
- group: docs
  title: ''
  type: APIReference
  url: https://ajaib.gitbook.io/coin-exchange/api-references/market-info
- group: start
  title: ''
  type: GettingStarted
  url: https://ajaib.gitbook.io/coin-exchange/getting-started/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ajaibid
- group: company
  title: ''
  type: Blog
  url: https://ajaib.co.id/belajar
- group: operate
  title: ''
  type: Support
  url: https://ajaib.co.id/pusat-bantuan
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ajaib.co.id/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ajaib.co.id/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/ajaib-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ajaib-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ajaib-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ajaib-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ajaib-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ajaib-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ajaib-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ajaib-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ajaib-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ajaib-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ajaib-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ajaib-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ajaib-coin-exchange-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: security/ajaib-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ajaib-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ajaib-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/ajaib-stock
created: '2026-08-06'
description: 'Ajaib is an Indonesian fintech and online brokerage founded in 2018 that gives retail investors access to Indonesian stocks, mutual funds, bonds, US stocks and crypto from a single mobile app. It operates PT Ajaib Sekuritas Asia for equities and Ajaib Kripto for digital assets, and became Southeast Asia''s first investment unicorn in 2021. Its one public developer surface is the Ajaib Coin Exchange API, a REST trading interface for the crypto venue, documented on GitBook and organized into Market Info, Wallet and Spot Trading. Access is not self-service: clients generate an ECDSASHA256 keypair, email the public key to Ajaib, and sign every request with X-API-KEY, X-SIGNATURE and X-TIMESTAMP headers. Ajaib publishes no OpenAPI, no SDKs and no status page.'
image: https://avatars.githubusercontent.com/u/45261753?v=4
layout: provider
mcp_servers:
- description: ''
  name: ajaib-mcp.yml
  slug: ajaib-mcpyml
modified: '2026-08-06'
name: Ajaib
nav: Providers
network: true
overview: 'Ajaib publishes 3 APIs on the [APIs.io](https://apis.io/) network: Market Info API, Spot Trading API, and Wallet API. Tagged areas include Company, Financial Services, Investing, Brokerage, and Trading.


  Ajaib''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 35.3
  delta: -0.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 16.4
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ajaib/refs/heads/main/screenshots/ajaib-2026-08-07T161125.png
security:
- kind: authentication
  name: Ajaib Authentication
  slug: ajaib-authentication
  summary_line: apiKey/signed-request · 3 schemes
- kind: domain-security
  name: Ajaib Domain Security
  slug: ajaib-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ajaib Vulnerability Disclosure
  slug: ajaib-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ajaib
tags:
- Company
- Financial Services
- Investing
- Brokerage
- Trading
- Cryptocurrency
- Crypto Exchange
- Stocks
- Mutual Funds
- Fintech
- Indonesia
- Wealth Management
website: https://ajaib.co.id/
---
