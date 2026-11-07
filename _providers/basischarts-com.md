---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Basis Charts providing crypto market data, charting, and analysis tools. Documentation is at the Docs site.
  name: Basis Charts API
  slug: basis-charts-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/basischarts-com/plans/basischarts-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/basischarts-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/basischarts-com/authentication/basischarts-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/basischarts-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/basischarts-com/llms/basischarts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basischarts-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/basischarts-com/mcp/basischarts-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/basischarts-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/basischarts-com/hosts/basischarts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basischarts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/basischarts-com/vendors/basischarts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basischarts-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.basischarts.com/news
- group: start
  title: ''
  type: Login
  url: https://www.basischarts.com/login
- group: auth
  href: https://artifacts.apis.io/basischarts-com/security/basischarts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basischarts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.basischarts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.basischarts.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.basischarts.com/docs/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.basischarts.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.basischarts.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.basischarts.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://www.basischarts.com/contact
created: '2026-11-02'
description: Basis Charts provides a free, browser‑based crypto trading terminal that aggregates live market data, charting, order‑flow, derivatives, AI‑assisted analysis, and research tools. Users can build no‑code strategies, back‑test, and generate reports without needing an account, while the platform integrates data from exchanges like Binance, Bybit, OKX, and Hyperliquid. The service emphasizes transparency, traceability, and independent research, offering extensive documentation, tutorials, and a community of over 7,000 weekly visitors.
image: https://www.basischarts.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at www.basischarts.com.
  name: Basis Charts MCP Server
  slug: basischarts-com-mcp-yml
modified: '2026-11-02'
name: Basis Charts
nav: Providers
network: true
overview: 'Basis Charts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Trading, Charting, Artificial Intelligence, and Research.


  Basis Charts'' developer surface includes authentication, documentation, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Basischarts Com Plans Pricing
  plan_count: 1
  slug: basischarts-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.5
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Basischarts Com Authentication
  slug: basischarts-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Basischarts Com Domain Security
  slug: basischarts-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basischarts-com
tags:
- Cryptocurrency
- Trading
- Charting
- Artificial Intelligence
- Research
- Free
website: https://www.basischarts.com/
---
