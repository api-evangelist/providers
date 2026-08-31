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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://woodstock.co/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/woodstock-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/woodstock-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/woodstock-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/woodstock-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/woodstock-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/woodstock-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://woodstock.co/ja/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://woodstock.co/ja/mcp/installation/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://woodstock.co/ja/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://woodstock.co/ja/fees
- group: operate
  title: ''
  type: Support
  url: https://woodstock.co/ja/faq
- group: company
  title: ''
  type: Blog
  url: https://zenn.dev/p/woodstock_tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/woodstock-tokyo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://woodstock.co/ja/legal/term-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woodstock.co/ja/legal/privacy-policy
created: '2026-07-17'
description: Woodstock (Woodstock K.K., Tokyo) is a Japanese investment platform offering zero-commission, 24-hour US stock trading in JPY with fractional shares down to 0.0001-share increments. A Financial Products Intermediary registered with the Kanto Financial Bureau (No. 965), with customer assets held by affiliated broker AlpacaJapan, Woodstock's programmatic surface is a hosted Model Context Protocol server that lets AI agents like Claude, ChatGPT, and Grok manage portfolios, research US stocks, and place real trades after OAuth plus passkey authorization. Backed by Kindred Ventures, Coinbase, and Sony.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/woodstock.png
layout: provider
mcp_servers:
- description: ''
  name: Woodstock MCP Server
  slug: woodstock-mcp-server
modified: '2026-07-21'
name: Woodstock
nav: Providers
network: true
overview: 'Woodstock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investing, Stock Trading, Brokerage, and Fintech.


  Woodstock''s developer surface includes authentication, documentation, getting-started guide, signup flow, pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Woodstock Authentication
  slug: woodstock-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Woodstock Domain Security
  slug: woodstock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: woodstock
tags:
- Company
- Investing
- Stock Trading
- Brokerage
- Fintech
- Japan
- MCP
- AI Agents
website: https://woodstock.co/
---
