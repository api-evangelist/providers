---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Delta API Suite is a partner-facing collection of APIs covering flight search, flight offers and order management, customer journey events, and operational data. Access is restricted to approved p
  name: Delta API Suite
  slug: delta-api-suite
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/delta-airlines/plans/delta-airlines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delta-airlines-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/delta-airlines/rate-limits/delta-airlines-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delta-airlines-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/delta-airlines/finops/delta-airlines-finops.yml
  title: ''
  type: FinOps
  url: finops/delta-airlines-finops.yml
- group: auth
  href: https://artifacts.apis.io/delta-airlines/security/delta-airlines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delta-airlines-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delta-air-lines
- group: company
  title: ''
  type: Website
  url: https://www.delta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.delta.com
- group: other
  title: ''
  type: Canonical
  url: https://github.com/api-evangelist/delta-air-lines
- group: company
  title: ''
  type: Blog
  url: https://news.delta.com/rss.xml
- group: start
  title: ''
  type: Dev Portal
  url: https://dev-apiportal.delta.com
- group: company
  title: ''
  type: Newsroom
  url: https://news.delta.com
- group: company
  title: ''
  type: Careers
  url: https://careers.delta.com
created: '2024-12-03'
description: Delta Airlines (alias of Delta Air Lines) is a major U.S. airline providing scheduled air transportation for passengers and cargo throughout the United States and across the world. This repository is an alias of the canonical delta-air-lines profile and points to the same partner developer portal at apiportal.delta.com.
finops:
- has_sources: true
  method: generated
  name: Delta Airlines Finops
  primary_unit: transaction
  service_category: Travel / Airline Distribution
  slug: delta-airlines-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-airlines.png
layout: provider
modified: '2026-08-08'
name: Delta Airlines
nav: Providers
network: true
overview: 'Delta Airlines is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Air Travel, Airlines, Aviation, Booking, and Flights.


  Delta Airlines'' developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Delta Airlines Plans Pricing
  plan_count: 1
  slug: delta-airlines-plans-pricing
press:
- date: ''
  title: 'AI meets airfare: Delta''s new pricing and what you need to ...'
  url: https://www.facebook.com/rossenreports/posts/ai-meets-airfare-deltas-new-pricing-and-what-you-need-to-know-/1545509503603165/
- date: ''
  title: Delta unveils AI-powered travel journey with new 'multi- ...
  url: https://news.delta.com/delta-unveils-ai-powered-travel-journey-new-multi-modal-transportation-options
- date: ''
  title: Delta responds to misinformation around AI pricing
  url: https://news.delta.com/delta-responds-misinformation-around-ai-pricing
- date: ''
  title: Delta-AI-Letter.pdf
  url: https://www.gallego.senate.gov/wp-content/uploads/2025/07/Delta-AI-Letter.pdf
- date: ''
  title: Delta Air Lines, Inc – Digital Transformation Strategies
  url: https://www.globaldata.com/store/report/delta-air-lines-enterprise-tech-analysis/
random_paper: 6
rate_limits:
- limit_count: 1
  name: Delta Airlines Rate Limits
  slug: delta-airlines-rate-limits
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.0
    operational_transparency: 5.3
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/delta-airlines/delta-airlines-2026-07-25T211717.png
security:
- kind: domain-security
  name: Delta Airlines Domain Security
  slug: delta-airlines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: delta-airlines
tags:
- Air Travel
- Airlines
- Aviation
- Booking
- Flights
- NDC
- Travel
website: https://www.delta.com
---
