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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/meteo-france/hosts/meteo-france-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meteo-france-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meteofrance
- group: auth
  href: https://artifacts.apis.io/meteo-france/security/meteo-france-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meteo-france-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meteofrance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://portail-api.meteofrance.fr/web/fr/
coverage:
  checked: '2026-10-28'
  detail: The API documentation at https://portail-api.meteofrance.fr/web/fr/ is a JavaScript‑rendered single‑page app that cannot be read without a browser.
  evidence:
  - status: 200
    url: https://portail-api.meteofrance.fr/web/fr/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Météo-France is the French national meteorological service, providing weather forecasts, climate data, and alerts for France and its overseas territories. It offers public APIs for forecasts, vigilance alerts, and climate information, supporting developers, researchers, and the public with free access to weather data and services.
layout: provider
modified: '2026-10-28'
name: Meteo-France
nav: Providers
network: true
overview: 'Meteo-France is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Forecast, and Public-API.


  Meteo-France''s developer surface includes documentation and 4 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Meteo France Domain Security
  slug: meteo-france-domain-security
  summary_line: TLSv1.3
slug: meteo-france
tags:
- Company
- Weather
- Climate
- Forecast
- Public-API
website: https://meteofrance.com/
---
