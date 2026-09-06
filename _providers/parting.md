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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parting-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parting.com
- group: company
  title: ''
  type: Blog
  url: https://www.parting.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parting.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.parting.com/faq/
- group: company
  title: ''
  type: About
  url: https://www.parting.com/about-us
created: '2026-07-17'
description: Parting operates parting.com, a consumer-facing funeral-home and cremation price-comparison platform that indexes more than 15,000 funeral homes and mortuaries across all 50 U.S. states, letting families research locations, photos, reviews, and pricing and contact providers directly. Founded in 2015 and based in Los Angeles, the company also publishes Parting Pro (partingpro.com), funeral-home arrangement and cremation software with third-party integrations to Passare, Keeper, and QuickBooks. As of this enrichment pass Parting exposes no public developer API, OpenAPI/spec surface, SDKs, or developer portal; this profile captures its public web presence and a domain-security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parting.png
layout: provider
modified: '2026-07-20'
name: Parting
nav: Providers
network: true
overview: 'Parting is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Funeral Services, Death Care, Cremation, and Directory.


  Parting''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parting/refs/heads/main/screenshots/parting-2026-08-07T191511.png
security:
- kind: domain-security
  name: Parting Domain Security
  slug: parting-domain-security
  summary_line: TLSv1.3 · HSTS
slug: parting
tags:
- Company
- Funeral Services
- Death Care
- Cremation
- Directory
- Price Comparison
- Consumer
- Los Angeles
website: https://parting.com
---
