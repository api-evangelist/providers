---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 2
apis:
- description: 'The Trulia API was a suite of public XML/JSON endpoints that exposed listings, property details, location lookups, neighborhood statistics, and school data. The full suite was deprecated after Trulia '
  name: Trulia API (Historical / Sunset)
  slug: trulia-api-historical
- description: 'Programmatic access to data that historically lived behind the Trulia API is now delivered through Zillow Group''s Bridge Interactive RESO-compliant data platform for MLSs and brokers, the Zillow Tech '
  name: Zillow Group APIs (Successor)
  slug: zillow-group-successor
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trulia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trulia.com
- group: company
  title: ''
  type: About
  url: https://www.trulia.com/about/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.zillowgroup.com
- group: start
  title: ''
  type: Portal
  url: https://www.zillowgroup.com/developers
- group: other
  title: ''
  type: Successor
  url: https://bridgedataoutput.com
- group: other
  title: ''
  type: Research
  url: https://www.trulia.com/research/
- group: company
  title: ''
  type: Blog
  url: https://www.trulia.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.trulia.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trulia.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trulia.com/legal/privacy/
- group: other
  title: ''
  type: X
  url: https://x.com/trulia
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/trulia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trulia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/trulia
created: '2024-01-01'
description: Trulia is a U.S. home and rental search portal owned by Zillow Group since the 2015 acquisition. Trulia is best known for its neighborhood data layer, combining listings with crime, school, commute, transit, noise, flood, and resident sentiment information overlaid on the map. After the Zillow Group consolidation, Trulia's historical public APIs (the Trulia Hotpads / Property / Stats / Schools / Locations APIs) were deprecated and shut down. Trulia listings, agent, and rental data are now distributed through Zillow Group programs (Bridge Interactive, Zillow Tech Connect, HotPads). This profile is maintained as an honest historical record and pointer to the successor Zillow Group developer surfaces.
finops:
- name: Trulia Finops
  service_category: API
  slug: trulia-finops
graphqls:
- description: This is a conceptual GraphQL schema for Trulia, the U.S. home and rental search portal owned by Zillow Group. Trulia's historical public REST APIs (Property, Stats, Schools, Locations) were deprecated
  name: Trulia GraphQL Schema
  slug: trulia-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trulia.png
layout: provider
modified: '2026-05-23'
name: Trulia
nav: Providers
network: true
overview: 'Trulia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Historical, Listings, Neighborhoods, and Real-Estate.


  Trulia''s developer surface includes developer portal, engineering blog, support, and 12 more developer resources.'
plans:
- name: Trulia Plans Pricing
  plan_count: 1
  slug: trulia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Trulia Rate Limits
  slug: trulia-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trulia/refs/heads/main/screenshots/trulia-2026-06-20T195757.png
security:
- kind: domain-security
  name: Trulia Domain Security
  slug: trulia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trulia
tags:
- Acquired
- Historical
- Listings
- Neighborhoods
- Real-Estate
- Rentals
- Schools
- Sunset
- Zillow Group
website: https://www.trulia.com
---
