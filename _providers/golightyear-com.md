---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/golightyear-com/well-known/golightyear-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/golightyear-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/golightyear-com/llms/golightyear-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/golightyear-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/golightyear-com/well-known/golightyear-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/golightyear-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/golightyear-com/hosts/golightyear-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/golightyear-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/golightyear-com/vendors/golightyear-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/golightyear-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightyear.com/en-eu/terms
- group: operate
  title: ''
  type: Support
  url: https://lightyear.com/en-eu/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightyear.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightyear.com/en-eu/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://lightyear.com/en-eu/plans
- group: start
  title: ''
  type: Login
  url: https://lightyear.com/en-eu/login
- group: company
  title: ''
  type: Blog
  url: https://lightyear.com/en-eu/blog
- group: auth
  href: https://artifacts.apis.io/golightyear-com/security/golightyear-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/golightyear-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://golightyear.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.lightyear.com/mcp
  - status: 401
    url: https://golightyear.com/api/mcp
  - status: 401
    url: https://lightyear.com/api/mcp
  - status: 200
    url: https://golightyear.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Lightyear operates a low‑cost investment platform that lets personal and business customers trade stocks, funds, ETFs, bonds, money‑market funds and crypto, and earn 2.46 % APY on a high‑yield Savings balance. The service is provided in the UK and across the EU, is regulated by the FCA and the Estonian Financial Supervision Authority, and uses BlackRock and J.P. Morgan custodians for asset protection.
image: https://lightyear.com/cms/OG_Default_EN_7a4714f5fe.png
layout: provider
modified: '2026-10-24'
name: Lightyear
nav: Providers
network: true
overview: 'Lightyear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Investing, Savings, Stocks, ETFs, and Cryptocurrency.


  Lightyear''s developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Golightyear Com Domain Security
  slug: golightyear-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: golightyear-com
tags:
- Investing
- Savings
- Stocks
- ETFs
- Cryptocurrency
website: https://golightyear.com
---
