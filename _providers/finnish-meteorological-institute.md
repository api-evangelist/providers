---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public weather and climate data API provided by FMI.
  name: Open Data API
  slug: open-data-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/finnish-meteorological-institute/hosts/finnish-meteorological-institute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finnish-meteorological-institute-hosts.yml
- group: other
  href: https://artifacts.apis.io/finnish-meteorological-institute/vendors/finnish-meteorological-institute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finnish-meteorological-institute-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ilmatieteenlaitos.fi/
- group: auth
  href: https://artifacts.apis.io/finnish-meteorological-institute/security/finnish-meteorological-institute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finnish-meteorological-institute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.ilmatieteenlaitos.fi/
created: '2026-10-23'
description: The Finnish Meteorological Institute (FMI) provides observations, research and services on the atmosphere, near‑space and seas. It offers public‑safety weather forecasts, climate data, marine information and scientific research for citizens, businesses and authorities in Finland and worldwide.
image: https://en.ilmatieteenlaitos.fi/static/img/press-release-default.jpg
layout: provider
modified: '2026-10-23'
name: Finnish Meteorological Institute
nav: Providers
network: true
overview: 'Finnish Meteorological Institute is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Data, and Research.


  Finnish Meteorological Institute''s developer surface includes documentation and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Finnish Meteorological Institute Domain Security
  slug: finnish-meteorological-institute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finnish-meteorological-institute
tags:
- Company
- Weather
- Climate
- Data
- Research
- Finland
website: https://en.ilmatieteenlaitos.fi/
---
