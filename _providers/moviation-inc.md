---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.moviationair.com'', ''status'': 301, ''note'': ''declared website redirects to https://vonaer.com/ — a different registrable domain (moviationair.com -> vonaer.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.moviationair.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moviation-inc-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vonaer.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vonaer.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://vonaer.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://vonaer.com/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://vonaer.com/membership
created: '2026-07-17'
description: Moviation, Inc. is a Seoul-based advanced air mobility and premium travel company founded in 2022 and backed by 500 Global. It operates Vonaer, an AI-powered luxury mobility platform that orchestrates on-demand travel across private aviation (jets and helicopters), luxury ground transportation (limousines), super yachts, and curated experiences, with planned expansion into electric vertical takeoff and landing (eVTOL) urban air mobility (UAM). Moviation currently runs air-taxi service with conventional helicopters and has partnered with hybrid-eVTOL developer Plana to build out an advanced air mobility (AAM) ecosystem in South Korea. The company reaches customers through the consumer Vonaer app and a concierge membership program; it publishes no public developer API, SDK, or documentation surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moviation-inc.png
layout: provider
modified: '2026-07-20'
name: Moviation, Inc.
nav: Providers
network: true
overview: 'Moviation, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Air Taxi, Urban Air Mobility, and eVTOL.


  Moviation, Inc.''s developer surface includes support, signup flow, pricing, and 4 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 14.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moviation-inc/refs/heads/main/screenshots/moviation-inc-2026-08-07T184358.png
security:
- kind: domain-security
  name: Moviation Inc Domain Security
  slug: moviation-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moviation-inc
tags:
- Company
- Mobility
- Air Taxi
- Urban Air Mobility
- eVTOL
- Aviation
- Luxury Travel
- Transportation
website: https://www.moviationair.com
---
