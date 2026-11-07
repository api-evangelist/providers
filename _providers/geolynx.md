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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/geolynx/hosts/geolynx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geolynx-hosts.yml
- group: other
  href: https://artifacts.apis.io/geolynx/vendors/geolynx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geolynx-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.geolynx.ee/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Geolynx
- group: auth
  href: https://artifacts.apis.io/geolynx/security/geolynx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geolynx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geolynx.ee
- group: docs
  title: ''
  type: Documentation
  url: https://geolynx.ee/en/
- group: docs
  title: ''
  type: APIReference
  url: https://geolynx.ee/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://geolynx.ee/en/
- group: company
  title: ''
  type: Blog
  url: https://geolynx.ee/en/posts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geolynx.ee/en/footer/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geolynx.ee/en/footer/privacy/
created: '2026-10-23'
description: Geolynx is an Estonian geospatial technology company offering professional GIS solutions, custom ESG data services, web hosting for spatial data, and training. Leveraging long‑term experience in open‑source GIS, satellite data analysis, and advanced computational methods, Geolynx provides accurate environmental risk assessments, tailored ESG reporting, and robust spatial data infrastructure for public and authenticated access. The company serves clients such as Emajõe Waterworks and aims to support both beginners and advanced users through courses on QGIS, PostGIS, and GeoServer.
layout: provider
modified: '2026-10-23'
name: Geolynx
nav: Providers
network: true
overview: 'Geolynx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, ESG, DataHosting, and Training.


  Geolynx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 44.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - estonia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/geolynx/geolynx-2026-11-03T132610.png
security:
- kind: domain-security
  name: Geolynx Domain Security
  slug: geolynx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: geolynx
tags:
- Company
- GIS
- ESG
- DataHosting
- Training
website: https://geolynx.ee
---
