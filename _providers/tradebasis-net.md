---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/tradebasis-net/plans/tradebasis-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tradebasis-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/tradebasis-net/llms/tradebasis-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradebasis-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/tradebasis-net/well-known/tradebasis-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tradebasis-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/tradebasis-net/hosts/tradebasis-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradebasis-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tradebasis.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tradebasis.net/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://tradebasis.net/pricing
- group: auth
  href: https://artifacts.apis.io/tradebasis-net/security/tradebasis-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradebasis-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradebasis.net/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://tradebasis.net/mcp
  - status: 200
    url: https://tradebasis.net/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: TradeBasis provides used‑vehicle appraisal software for U.S. auto dealers, offering real‑time wholesale and retail pricing data, mileage adjustments, and market velocity insights. Their platform enables dealers to quickly generate accurate vehicle valuations, compare pricing against competitors, and access research reports, helping streamline inventory decisions and improve profitability.
image: https://tradebasis.net/og-image.png
layout: provider
modified: '2026-10-30'
name: tradebasis-net
nav: Providers
network: true
overview: 'tradebasis-net is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Software, Appraisal, and Used Vehicles.


  tradebasis-net''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Tradebasis Net Plans Pricing
  plan_count: 2
  slug: tradebasis-net-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tradebasis-net/tradebasis-net-2026-11-03T144948.png
security:
- kind: domain-security
  name: Tradebasis Net Domain Security
  slug: tradebasis-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradebasis-net
tags:
- Company
- Automotive
- Software
- Appraisal
- Used Vehicles
website: https://tradebasis.net/
---
