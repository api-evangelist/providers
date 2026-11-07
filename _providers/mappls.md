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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Mappls provides APIs for maps, geocoding, routing, traffic and place search as described on their developer portal.
  name: Mappls API
  slug: mappls-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/mappls/hosts/mappls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mappls-hosts.yml
- group: other
  href: https://artifacts.apis.io/mappls/vendors/mappls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mappls-vendors.yml
- group: build
  href: https://artifacts.apis.io/mappls/packages/mappls-packages.yml
  title: ''
  type: SDKs
  url: packages/mappls-packages.yml
- group: build
  href: https://artifacts.apis.io/mappls/packages/mappls-packages.yml
  title: ''
  type: Packages
  url: packages/mappls-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.mappls.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mappls.com/
- group: auth
  href: https://artifacts.apis.io/mappls/security/mappls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mappls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mappls.com/
- group: other
  title: ''
  type: Image
  url: https://www.mappls.com/favicon.ico
coverage:
  checked: '2026-10-28'
  detail: Developer portal redirects to a JavaScript SDK page, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.mappls.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: MapmyIndia, operating under the brand Mappls, provides comprehensive mapping, navigation, and location-based services for enterprises and developers in India. Their platform offers APIs for maps, geocoding, routing, traffic, and place search, enabling integration of location intelligence into mobile apps, web services, and IoT solutions. With a focus on high accuracy and extensive coverage, Mappls serves millions of users across various industries such as logistics, transportation, and retail.
image: https://www.mappls.com/still_image_center=24.595939499830784_77.22556114196777&zoom=4&markers=false.png
layout: provider
modified: '2026-10-28'
name: MapmyIndia
nav: Providers
network: true
overview: 'MapmyIndia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mapping, Navigation, Location, and India.


  MapmyIndia''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.6
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/mappls/mappls-2026-11-03T135337.png
security:
- kind: domain-security
  name: Mappls Domain Security
  slug: mappls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mappls
tags:
- Company
- Mapping
- Navigation
- Location
- India
website: https://mappls.com/
---
