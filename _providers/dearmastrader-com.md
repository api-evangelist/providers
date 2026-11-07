---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DearmasTrader offers a trading bot platform; the API is undocumented publicly and no machine‑readable contract was found.
  name: DearmasTrader API
  slug: dearmastrader-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dearmastrader-com/plans/dearmastrader-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dearmastrader-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dearmastrader-com/well-known/dearmastrader-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dearmastrader-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dearmastrader-com/hosts/dearmastrader-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dearmastrader-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dearmastrader-com/vendors/dearmastrader-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dearmastrader-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dearmastrader.com/es/terms
- group: operate
  title: ''
  type: Support
  url: https://dearmastrader.com/es/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dearmastrader.com/es/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dearmastrader.com/es/pricing
- group: company
  title: ''
  type: Blog
  url: https://dearmastrader.com/es/blog
- group: auth
  href: https://artifacts.apis.io/dearmastrader-com/security/dearmastrader-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dearmastrader-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dearmastrader.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was discovered despite probing documented hosts.
  evidence:
  - status: 200
    url: https://dearmastrader.com/es/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DearmasTrader provides automated cryptocurrency trading bots with features like DCA, Grid, and backtesting. Users can connect their own exchange accounts via API keys to run bots on Binance, Bybit, MEXC, OKX, and Bitget. The platform offers a free 7‑day trial without credit card, a help center, blog, and pricing plans. It emphasizes that it is not an exchange or broker, and all trades are executed by the user’s own exchange account.
image: https://dearmastrader.com/og-image.png
layout: provider
modified: '2026-11-05'
name: DearmasTrader
nav: Providers
network: true
overview: 'DearmasTrader is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, TradingBots, Automation, and Finance.


  DearmasTrader''s developer surface includes support, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Dearmastrader Com Plans Pricing
  plan_count: 5
  slug: dearmastrader-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dearmastrader Com Domain Security
  slug: dearmastrader-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dearmastrader-com
tags:
- Company
- Cryptocurrency
- TradingBots
- Automation
- Finance
website: https://dearmastrader.com/
---
