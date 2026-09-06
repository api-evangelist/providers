---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  url: https://www.avonow.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avonow
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/avo-9a0c
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avo-llms.txt
created: '2026-07-17'
description: Avo (avonow.com) was a New York City-based "building commerce" and workplace-amenity platform, founded 2017-2018 out of Y Combinator (S18) and backed by Insight Partners and Kleiner Perkins with roughly $84M raised. It offered white-labeled same-day delivery of groceries, household goods, alcohol and personal-care items into residential and office buildings with no order minimums or delivery fees, plus on-site and virtual event programming and corporate gifting and recognition services, serving apartment communities, corporations, hospitals and universities across New York, New Jersey, Chicago and Houston. Avo published no API, SDK or developer portal, and as of a 2026-07-20 probe its domain resolves to a parked lander with no operational hosts; Y Combinator lists the company as inactive.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avo.png
layout: provider
modified: '2026-07-20'
name: AVO
nav: Providers
network: true
overview: AVO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Delivery, Logistics, Last Mile Delivery, and Grocery.
random_paper: 11
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avo/refs/heads/main/screenshots/avo-2026-07-25T202004.png
security:
- kind: domain-security
  name: Avo Domain Security
  slug: avo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avo
tags:
- Company
- Delivery
- Logistics
- Last Mile Delivery
- Grocery
- E-Commerce
- Real-Estate
- Workplace
- amenities
- Corporate Gifting
website: https://www.avonow.com/
---
