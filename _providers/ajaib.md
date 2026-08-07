---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ajaib Agentic Access
  operation_count: 14
  slug: ajaib-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: REST trading API for the Ajaib Coin Exchange (Ajaib Kripto). Provides market information (server time, exchange info, order book depth, latest price), wallet portfolio balances, and spot trading (view
  name: Ajaib Coin Exchange API
  slug: coin-exchange
artifact_total: 6
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
overview: 'Ajaib publishes 1 API on the [APIs.io](https://apis.io/) network: Coin Exchange API. Tagged areas include Company, Financial Services, Investing, Brokerage, and Trading.


  Ajaib''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 51
score:
  band: developing
  composite: 48.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 64.1
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
