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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bangladesh-meteorological-department/hosts/bangladesh-meteorological-department-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bangladesh-meteorological-department-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bangladesh-meteorological-department/security/bangladesh-meteorological-department-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bangladesh-meteorological-department-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bmd.gov.bd/
- group: docs
  title: ''
  type: Documentation
  url: https://dataportal.bmd.gov.bd/web/
- group: operate
  title: ''
  type: Support
  url: https://bmd.gov.bd/contact-us
- group: company
  title: ''
  type: About
  url: https://bmd.gov.bd/about
created: '2026-10-28'
description: The Bangladesh Meteorological Department (BMD) is the national agency responsible for weather forecasting, climate monitoring, and meteorological services in Bangladesh. It provides real-time weather observations, forecasts, warnings, and climate data through its public web portals. The department offers data purchase services, climate data portal, and various online tools for weather information, serving government, researchers, and the public.
image: https://server6.bmd.gov.bd/assets/images/logo.jpg
layout: provider
modified: '2026-10-28'
name: BMD
nav: Providers
network: true
overview: 'BMD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Government, and Data.


  BMD''s developer surface includes documentation, support, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bangladesh-meteorological-department/bangladesh-meteorological-department-2026-11-03T121534.png
security:
- kind: domain-security
  name: Bangladesh Meteorological Department Domain Security
  slug: bangladesh-meteorological-department-domain-security
  summary_line: TLSv1.3
slug: bangladesh-meteorological-department
tags:
- Company
- Weather
- Climate
- Government
- Data
website: https://bmd.gov.bd/
---
