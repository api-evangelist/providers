---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.circor.com/
- group: auth
  href: https://artifacts.apis.io/circor-international/security/circor-international-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circor-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circor-international-inc-
- group: company
  title: ''
  type: Website
  url: https://www.circor.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.circor.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.circor.com/about/leadership
- group: operate
  title: ''
  type: Support
  url: https://www.circor.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circor.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.circor.com/careers
- group: company
  title: ''
  type: BlogRSS
  url: https://www.circor.com/rss.xml
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/circorinternational
- group: other
  href: https://artifacts.apis.io/circor-international/regulatory/circor-international-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/circor-international-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/circor-international/plans/circor-international-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/circor-international-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/circor-international/rate-limits/circor-international-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/circor-international-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/circor-international/finops/circor-international-finops.yml
  title: ''
  type: FinOps
  url: finops/circor-international-finops.yml
coverage:
  checked: '2026-09-19'
  detail: 'CIRCOR builds pumps and valves, not software: www.circor.com is a Drupal brochure site whose whole navigation is products, brands, careers and newsroom, its only app (CIRCORSmart, for IMO pump maintenance) is a closed mobile/desktop client with no published interface, and the api.circor.com and developer.circor.com hosts this profile carried since 2026-04-19 are NXDOMAIN placeholders that were never real.'
  evidence:
  - status: 0
    url: https://api.circor.com
  - status: 0
    url: https://developer.circor.com/docs
  - status: 200
    url: https://www.circor.com/
  - status: 404
    url: https://www.circor.com/.well-known/security.txt
  - status: 404
    url: https://www.circor.com/openapi.json
  - status: 404
    url: https://circorsmart-service.azurewebsites.net/v3/api-docs
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'CIRCOR International is a flow-control manufacturer headquartered in Burlington, Massachusetts, building mission-critical pumps, valves and flow-control products for the Industrial and Aerospace & Defense markets through brands including IMO, Allweiler, Warren, RTK, Schroedahl, Hale Hamilton, Aerodyne Controls, Leslie Controls, Circle Seal Controls and Zenith. The company was established in 1999, sells directly and through sales partners to roughly 14,000 customers in about 100 countries with approximately 3,100 employees, and was taken private by KKR on 18 October 2023, after which its shares ceased trading on the NYSE. CIRCOR publishes no developer portal, API reference or machine-readable contract of any kind: its only software product on the public web is CIRCORSmart, a closed iOS/Android/desktop maintenance-tracking app for IMO pump series whose admin console and backend are unauthenticated-inaccessible Azure applications with no published interface.'
finops:
- has_sources: true
  method: generated
  name: Circor International Finops
  primary_unit: ''
  service_category: Industrial / Flow Control
  slug: circor-international-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circor-international.png
layout: provider
modified: '2026-09-19'
name: CIRCOR International
nav: Providers
network: true
overview: 'CIRCOR International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Flow Control, Industrial, Energy, Aerospace and Defense, and Manufacturing.


  CIRCOR International''s developer surface includes pricing, support, YouTube channel, and 12 more developer resources.'
plans:
- name: Circor International Plans Pricing
  plan_count: 1
  slug: circor-international-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Circor International Rate Limits
  slug: circor-international-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 43.0
    catalog_earned_first_party: 16.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/circor-international/circor-international-2026-06-20T174351.png
security:
- kind: domain-security
  name: Circor International Domain Security
  slug: circor-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circor-international
tags:
- Flow Control
- Industrial
- Energy
- Aerospace and Defense
- Manufacturing
- Pumps
- Valves
website: https://www.circor.com
---
