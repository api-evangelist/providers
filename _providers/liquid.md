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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Co-Invest is Liquid delivered as a remote Model Context Protocol (MCP) server. Once connected, an MCP client can research markets (live prices, funding rates, open interest, whale positioning, liquida
  name: Liquid Co-Invest MCP
  slug: co-invest-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryliquid.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.liquid.trade/coinvest
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liquid.trade
- group: docs
  title: ''
  type: APIReference
  url: https://www.liquid.trade/coinvest-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryliquid.xyz/about-liquid/quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://www.liquid.trade/support
- group: company
  title: ''
  type: Blog
  url: https://www.liquid.trade/learn
- group: start
  title: ''
  type: SignUp
  url: https://app.liquid.trade/?login=true
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.tryliquid.xyz/trading/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquid.trade/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquid.trade/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.liquid.trade/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/liquid-changelog.yml
- group: auth
  title: ''
  type: SecurityAudit
  url: https://www.liquid.trade/audits
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/liquidtrading
- group: other
  title: ''
  type: Telegram
  url: https://t.me/liquid_perps
- group: company
  title: ''
  type: Twitter
  url: https://x.com/liquidtrading
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/107723236
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Liquid-Perps
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/liquid
- group: other
  title: ''
  type: BrandKit
  url: https://www.liquid.trade/brand
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liquid-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liquid-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquid-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liquid-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liquid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liquid-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquid-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liquid-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/liquid-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Liquid (liquid.trade, formerly tryliquid.xyz) is a perpetual-futures trading platform and perp-DEX aggregator that lets retail traders go long or short on 500+ markets — crypto perps, US and international equities, commodities, FX, indices, pre-IPO names such as OpenAI, Anthropic and SpaceX, and event/prediction contracts — 24/7 with up to 50x multipliers, routing orders through venues including Hyperliquid while keeping funds in the user's own non-custodial wallet. Its programmable surface is Co-Invest, a published remote Model Context Protocol (MCP) server at coinvest.liquid.trade that puts market research, portfolio state and confirmed trade execution inside Claude, ChatGPT, Cursor and any MCP-compatible client, secured with OAuth 2.1 (PKCE + dynamic client registration) and two scopes, read and trade. Liquid raised an $18M Series Seed led by Neo and Left Lane Capital in April 2026, following a $7.6M seed led by Paradigm.
image: https://www.liquid.trade/images/liquid-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: liquid-mcp.yml
  slug: liquid-mcpyml
modified: '2026-07-19'
name: Liquid
nav: Providers
network: true
overview: 'Liquid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Defi, Trading, Perpetual Futures, and Prediction Markets.


  Liquid''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 26 more developer resources.'
random_paper: 18
scopes:
- name: Liquid Scopes
  scope_count: 2
  slug: liquid-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 38.6
  delta: 0.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 38.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquid/refs/heads/main/screenshots/liquid-2026-07-25T225311.png
security:
- kind: authentication
  name: Liquid Authentication
  slug: liquid-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Liquid Domain Security
  slug: liquid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: liquid
tags:
- Company
- Crypto Defi
- Trading
- Perpetual Futures
- Prediction Markets
- Fintech
- MCP
- Agentic Commerce
- OAuth
website: https://tryliquid.xyz
---
