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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: Asset metadata lookup
  name: Bitpanda assets API
  slug: bitpanda-assets-api
- description: Live ticker prices
  name: Bitpanda market-data API
  slug: bitpanda-market-data-api
- description: Transaction history across all asset types
  name: Bitpanda transactions API
  slug: bitpanda-transactions-api
- description: Wallet balances across all asset types
  name: Bitpanda wallets API
  slug: bitpanda-wallets-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitpanda-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bitpanda.com/en/security
- group: company
  title: ''
  type: Website
  url: https://bitpanda.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bitpanda.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitpanda.com/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bitpanda.com/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bitpanda.com/platform/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitpanda-labs
- group: company
  title: ''
  type: Blog
  url: https://blog.bitpanda.com/en
- group: operate
  title: ''
  type: Support
  url: https://support.bitpanda.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://support.bitpanda.com/hc/en-us/articles/16259273206044-Bitpanda-s-fees-and-premiums-explained
- group: start
  title: ''
  type: SignUp
  url: https://web.bitpanda.com/
- group: start
  title: ''
  type: Login
  url: https://web.bitpanda.com/my-account/apikey
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitpanda.com/en/legal/bitpanda-group-general-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitpanda.com/en/legal/bitpanda-group-privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitpanda.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bitpanda-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitpanda-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitpanda-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/bitpanda-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitpanda-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitpanda-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitpanda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitpanda-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitpanda-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitpanda-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitpanda-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitpanda-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitpanda-llms.txt
created: '2026-07-17'
description: Bitpanda is a European retail investment platform, founded in Vienna in 2014, that lets users buy, sell, and hold cryptocurrencies, stocks, ETFs, precious metals, commodities, and crypto indices from a single account. Its developer surface centres on the read-only Bitpanda Platform API (developer.bitpanda.com) for portfolio, wallet balances, transactions, asset metadata, and live ticker prices, authenticated with an X-Api-Key header and cursor-based pagination, and on Bitpanda Fusion, the automated-trading product offering programmatic order execution across aggregated liquidity. Bitpanda Labs maintains an official MCP server, an Agent Skill, and a Go CLI (bp) as first-party ways for developers and AI agents to reach the API. This profile was surfaced as a portfolio company of Speedinvest and enriched by the API Evangelist pipeline from Bitpanda's public developer surface.
image: https://logo.clearbit.com/bitpanda.com
layout: provider
mcp_servers:
- description: ''
  name: bitpanda-mcp.yml
  slug: bitpanda-mcpyml
modified: '2026-07-18'
name: Bitpanda
nav: Providers
network: true
overview: 'Bitpanda publishes 4 APIs on the [APIs.io](https://apis.io/) network, including assets API, market-data API, transactions API, and 1 more. Tagged areas include Company, Cryptocurrency, Fintech, Trading, and Investing.


  Bitpanda''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 57.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 57.9
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitpanda/refs/heads/main/screenshots/bitpanda-2026-07-25T203204.png
security:
- kind: authentication
  name: Bitpanda Authentication
  slug: bitpanda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitpanda Domain Security
  slug: bitpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bitpanda Trust Center
  slug: bitpanda-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: bitpanda
tags:
- Company
- Cryptocurrency
- Fintech
- Trading
- Investing
- Stocks
- ETFs
- Precious Metals
- Portfolio
- Market Data
- MCP
- Agent Skills
website: https://bitpanda.com
---
