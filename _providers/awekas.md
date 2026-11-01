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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides access to real‑time and historical weather station data via the AWEKAS platform.
  name: AWEKAS Weather Data API
  slug: awekas-weather-data-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/awekas/llms/awekas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awekas-llms.txt
- group: other
  href: https://artifacts.apis.io/awekas/hosts/awekas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awekas-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/awekas
- group: auth
  href: https://artifacts.apis.io/awekas/security/awekas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awekas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awekas.at/
- group: docs
  title: ''
  type: Documentation
  url: https://www.awekas.at/main/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.awekas.at/main/en/
- group: operate
  title: ''
  type: Support
  url: https://www.awekas.at/main/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.awekas.at/main/en/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.awekas.at/main/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.awekas.at/main/en/privacy/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.awekas.at/main/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AWEKAS operates a global network of private weather stations, providing real‑time, community‑sourced meteorological data. The platform offers a web portal and mobile apps for viewing weather conditions, maps, and historical data, supporting enthusiasts, researchers, and professionals worldwide. It emphasizes open data sharing, collaborative observation, and tools for station owners to contribute and access detailed weather information.
image: https://www.awekas.at/mainmap.png
layout: provider
modified: '2026-10-28'
name: AWEKAS
nav: Providers
network: true
overview: 'AWEKAS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather Data, Private Weather Stations, Weather Map, Weather App, and Community Network.


  AWEKAS''s developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Awekas Domain Security
  slug: awekas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: awekas
tags:
- Weather Data
- Private Weather Stations
- Weather Map
- Weather App
- Community Network
website: https://awekas.at/
---
