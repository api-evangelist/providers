---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/mt4api/plans/mt4api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mt4api-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/mt4api/authentication/mt4api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mt4api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/mt4api/llms/mt4api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mt4api-llms.txt
- group: other
  href: https://artifacts.apis.io/mt4api/hosts/mt4api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mt4api-hosts.yml
- group: other
  href: https://artifacts.apis.io/mt4api/vendors/mt4api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mt4api-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fxsocket.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fxsocket.com
- group: build
  title: ''
  type: SDKs
  url: https://fxsocket.com/sdks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fxsocket.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://fxsocket.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://fxsocket.com/docs
- group: company
  title: ''
  type: Blog
  url: https://fxsocket.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://fxsocket.com/docs/mcp
- group: auth
  href: https://artifacts.apis.io/mt4api/security/mt4api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mt4api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mt4api.dev/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://mt4api.dev/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Noble Minds Media is a technology company focused on providing advanced trading and financial data APIs for MetaTrader 4 platforms. It offers real-time market data, historical price feeds, and automated trading tools, targeting developers and financial institutions seeking to integrate MT4 capabilities into their applications. The company emphasizes low latency, high reliability, and comprehensive documentation to support seamless integration.
image: https://fxsocket.com/opengraph-image?d9f8b86d8cd4dd9b
layout: provider
modified: '2026-10-21'
name: Noble Minds Media
nav: Providers
network: true
overview: 'Noble Minds Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Trading, MetaTrader, and Data.


  Noble Minds Media''s developer surface includes authentication, pricing, documentation, engineering blog, getting-started guide, and 10 more developer resources.'
plans:
- name: Mt4Api Plans Pricing
  plan_count: 3
  slug: mt4api-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 46.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mt4api/mt4api-2026-11-03T135911.png
security:
- kind: authentication
  name: Mt4Api Authentication
  slug: mt4api-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mt4Api Domain Security
  slug: mt4api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mt4api
tags:
- Finance
- Trading
- MetaTrader
- Data
website: https://mt4api.dev/
---
