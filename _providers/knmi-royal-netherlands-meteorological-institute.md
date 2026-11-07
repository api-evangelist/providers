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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: KNMI Data Catalogue API
  name: KNMI Data Catalogue API
  slug: knmi-data-catalogue-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/knmi-royal-netherlands-meteorological-institute/hosts/knmi-royal-netherlands-meteorological-institute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/knmi-royal-netherlands-meteorological-institute-hosts.yml
- group: other
  href: https://artifacts.apis.io/knmi-royal-netherlands-meteorological-institute/vendors/knmi-royal-netherlands-meteorological-institute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/knmi-royal-netherlands-meteorological-institute-vendors.yml
- group: build
  href: https://artifacts.apis.io/knmi-royal-netherlands-meteorological-institute/packages/knmi-royal-netherlands-meteorological-institute-packages.yml
  title: ''
  type: SDKs
  url: packages/knmi-royal-netherlands-meteorological-institute-packages.yml
- group: build
  href: https://artifacts.apis.io/knmi-royal-netherlands-meteorological-institute/packages/knmi-royal-netherlands-meteorological-institute-packages.yml
  title: ''
  type: Packages
  url: packages/knmi-royal-netherlands-meteorological-institute-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.knmi.nl/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KNMI
- group: auth
  href: https://artifacts.apis.io/knmi-royal-netherlands-meteorological-institute/security/knmi-royal-netherlands-meteorological-institute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knmi-royal-netherlands-meteorological-institute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.knmi.nl/
created: '2026-10-26'
description: The Royal Netherlands Meteorological Institute (KNMI) is the Dutch national weather service, providing weather forecasts, climate data, and seismology information. It operates as a public research institute, delivering data and expertise to government, businesses, and the public. The KNMI offers APIs for weather observations, forecasts, climate statistics, and earthquake data, supporting applications in agriculture, aviation, emergency management, and scientific research.
layout: provider
modified: '2026-10-26'
name: KNMI Royal Netherlands Meteorological Institute
nav: Providers
network: true
overview: 'KNMI Royal Netherlands Meteorological Institute is listed with 1 API on the [APIs.io](https://apis.io/) network: KNMI Data Catalogue API. Tagged areas include Company, Weather, Climate, Seismology, and Data.'
random_paper: 9
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 24.3
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.8
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/knmi-royal-netherlands-meteorological-institute/knmi-royal-netherlands-meteorological-institute-2026-11-03T134451.png
security:
- kind: domain-security
  name: Knmi Royal Netherlands Meteorological Institute Domain Security
  slug: knmi-royal-netherlands-meteorological-institute-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: knmi-royal-netherlands-meteorological-institute
tags:
- Company
- Weather
- Climate
- Seismology
- Data
website: http://www.knmi.nl/
---
