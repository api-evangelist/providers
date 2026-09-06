---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Delta API Suite is a partner-facing collection of APIs covering flight search, flight offers and order management, customer journey events, and operational data. Access is restricted to approved p
  name: Delta API Suite
  slug: delta-api-suite
artifact_total: 6
common:
- group: auth
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
- name: Delta Airlines Finops
  service_category: Travel / Airline Distribution
  slug: delta-airlines-finops
graphqls:
- description: This GraphQL schema represents the conceptual data model for Delta Air Lines' flight and travel APIs, covering the full passenger journey from flight search and booking through check-in, boarding, and
  name: Delta Airlines GraphQL Schema
  slug: delta-airlines-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-airlines.png
layout: provider
modified: '2026-08-08'
name: Delta Airlines
nav: Providers
network: true
overview: 'Delta Airlines publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Air Travel, Airlines, Aviation, Booking, and Flights.


  Delta Airlines'' developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Delta Airlines Plans Pricing
  plan_count: 1
  slug: delta-airlines-plans-pricing
press:
- date: '2026-05-25'
  title: 'AI meets airfare: Delta''s new pricing and what you need to ...'
  url: https://www.facebook.com/rossenreports/posts/ai-meets-airfare-deltas-new-pricing-and-what-you-need-to-know-/1545509503603165/
- date: '2026-05-25'
  title: Delta unveils AI-powered travel journey with new 'multi- ...
  url: https://news.delta.com/delta-unveils-ai-powered-travel-journey-new-multi-modal-transportation-options
- date: '2026-05-25'
  title: Delta responds to misinformation around AI pricing
  url: https://news.delta.com/delta-responds-misinformation-around-ai-pricing
- date: '2026-05-25'
  title: Delta-AI-Letter.pdf
  url: https://www.gallego.senate.gov/wp-content/uploads/2025/07/Delta-AI-Letter.pdf
- date: '2026-05-25'
  title: Delta Air Lines, Inc – Digital Transformation Strategies
  url: https://www.globaldata.com/store/report/delta-air-lines-enterprise-tech-analysis/
random_paper: 15
rate_limits:
- limit_count: 1
  name: Delta Airlines Rate Limits
  slug: delta-airlines-rate-limits
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delta-airlines/refs/heads/main/screenshots/delta-airlines-2026-07-25T211717.png
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
