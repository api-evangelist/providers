---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Listed issue master, daily and morning-session OHLCV, minute bars and tick trades (add-on), earnings calendar, and weekly trading by investor type for Tokyo Stock Exchange equities, under /v2/equities
  name: J-Quants Equities API
  slug: j-quants-equities-api
- description: Market-structure datasets under /v2/markets/* - trading calendar, short sale position reports, short ratio by sector, weekly margin interest, daily margin alerts, and breakdown trading data.
  name: J-Quants Markets API
  slug: j-quants-markets-api
- description: Daily OHLC for TOPIX and other JPX indices under /v2/indices/* endpoints, with plan-gated access (TOPIX from Light, full index set from Standard).
  name: J-Quants Indices API
  slug: j-quants-indices-api
- description: Corporate financial data under /v2/fins/* - summary report figures (EPS, forecasts), detailed BS/PL/CF statements, and cash dividend data sourced from TDnet disclosures.
  name: J-Quants Financials API
  slug: j-quants-financials-api
- description: Daily OHLC for Osaka Exchange futures and options under /v2/derivatives/*, including Nikkei 225 options (Standard plan) and the full futures/options universe (Premium plan).
  name: J-Quants Derivatives API
  slug: j-quants-derivatives-api
- description: Structured data extracted from EDINET regulatory filings under /v2/edinet/* - major shareholders, cross-shareholdings (policy holdings), and large volume holding reports.
  name: J-Quants EDINET Data API
  slug: j-quants-edinet-api
- description: Add-on access to TDnet timely-disclosure documents - a disclosure index (/td/list), document file retrieval (/td/files), and bulk CSV download (/td/bulk) covering five years of filings.
  name: J-Quants TDnet Disclosure API
  slug: j-quants-tdnet-api
- description: File-based delivery alongside the REST endpoints - list available bulk files (/bulk/list) and download gzipped CSV extracts (/bulk/get) for supported datasets.
  name: J-Quants Bulk Download API
  slug: j-quants-bulk-download-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jpx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jpx-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jpx-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/jpx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jpx-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jpx-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jpx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jpx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jpx-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jpx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jpx-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://jpx-jquants.com/en/help/incident
- group: operate
  title: ''
  type: Deprecation
  url: https://jpx-jquants.com/en/spec/migration-v1-v2
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jpx-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://jpx-jquants.com/en/spec/release
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jpx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jpx-plans.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://jpx-jquants.com/en/spec/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://jpx-jquants.com/en/spec
- group: company
  title: ''
  type: Website
  url: https://www.jpx.co.jp/english/
- group: start
  title: ''
  type: Portal
  url: https://jpx-jquants.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://jpx-jquants.com/en/spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/J-Quants
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/japan-exchange-group
- group: company
  title: ''
  type: Blog
  url: https://qiita.com/j_quants
- group: commercial
  title: ''
  type: Pricing
  url: https://jpx-jquants.com/en#pricing
- group: start
  title: ''
  type: SignUp
  url: https://jpx-jquants.com/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jpx.co.jp/english/term-of-use/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jpx.co.jp/english/corporate/governance/security/personal-information/index.html
- group: operate
  title: ''
  type: Support
  url: https://jpx-jquants.com/en/help
created: '2026-07-21'
description: JPX (Japan Exchange Group) operates the Tokyo Stock Exchange, Osaka Exchange, and Tokyo Commodity Exchange, and sells Japanese market data through its JPX Market Innovation & Research arm. Its developer-facing product is the J-Quants API - a self-serve, subscription REST API (Free/Light/Standard/Premium plans, x-api-key auth, base https://api.jquants.com/v2) delivering historical equities OHLCV/minute/tick bars, indices, derivatives, financial statements, short-selling and margin data, EDINET filings, and TDnet disclosures, plus bulk CSV download, an MCP server, and a CLI - licensed to individual investors only. Institutional real-time data (FLEX Standard and FLEX MBO order-book feeds) and corporate historical data (J-Quants Pro via API/SFTP/Snowflake, J-Quants DataCube) are sales-gated services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jpx.png
layout: provider
mcp_servers:
- description: ''
  name: jpx-mcp.yml
  slug: jpx-mcpyml
modified: '2026-07-22'
name: JPX (Japan Exchange Group)
nav: Providers
network: true
overview: 'JPX (Japan Exchange Group) publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Stocks, Exchange, and Trading.


  JPX (Japan Exchange Group)''s developer surface includes CLI, authentication, changelog, release notes, getting-started guide, API reference, developer portal, and 24 more developer resources.'
plans:
- name: Jpx Plans
  plan_count: 4
  slug: jpx-plans
random_paper: 10
rate_limits:
- limit_count: 8
  name: Jpx Rate Limits
  slug: jpx-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 0.3
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 76.3
  previous_composite: 51.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jpx/refs/heads/main/screenshots/jpx-2026-07-22T202441.png
security:
- kind: authentication
  name: Jpx Authentication
  slug: jpx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jpx Domain Security
  slug: jpx-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: jpx
tags:
- Financial
- Market Data
- Stocks
- Exchange
- Trading
- Derivatives
- Indices
- Reference Data
- Japan
website: https://www.jpx.co.jp/english/
---
