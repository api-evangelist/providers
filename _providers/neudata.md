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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/neudata/well-known/neudata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/neudata-well-known.yml
- group: other
  href: https://artifacts.apis.io/neudata/hosts/neudata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neudata-hosts.yml
- group: other
  href: https://artifacts.apis.io/neudata/vendors/neudata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neudata-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neudata.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neudata.co/privacy-statement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.neudata.co/1/vendors/pricing-culture
- group: company
  title: ''
  type: Blog
  url: https://www.neudata.co/blog/data-monetization-insights
- group: auth
  href: https://artifacts.apis.io/neudata/security/neudata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neudata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://neudata.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://info.neudata.co/mcp
  - status: 200
    url: https://neudata.co/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Neudata Ltd. provides a platform for alternative data and market data insights, helping data buyers, sellers, and AI companies source, manage, and comply with proprietary training data. Their services include data sourcing, compliance tools, private market intelligence, and professional consulting to accelerate data programs for enterprises and investors.
image: https://cdn.prod.website-files.com/646d3b5209e7fa1e9f12831c/6491e29286ca76070b6dc421_open%20graph.png
layout: provider
modified: '2026-10-21'
name: Neudata Ltd.
nav: Providers
network: true
overview: 'Neudata Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Artificial Intelligence, Market Insights, and Compliance.


  Neudata Ltd.''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/neudata/neudata-2026-11-03T140134.png
security:
- kind: domain-security
  name: Neudata Domain Security
  slug: neudata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neudata
tags:
- Company
- Data
- Artificial Intelligence
- Market Insights
- Compliance
website: https://neudata.co/
---
