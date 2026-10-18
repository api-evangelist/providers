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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copernicus/refs/heads/main/hosts/copernicus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copernicus-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.copernicus.eu/services/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.copernicus.eu/en/news/news
- group: start
  title: ''
  type: Login
  url: https://www.copernicus.eu/user/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copernicus/refs/heads/main/security/copernicus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copernicus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.copernicus.eu/
coverage:
  checked: '2026-10-13'
  detail: Copernicus is a European Earth observation program without a public developer API.
  evidence:
  - status: 200
    url: https://www.copernicus.eu/
  reason: not-a-software-company
  state: none
created: '2026-10-13'
description: Copernicus is the European Union’s Earth observation programme, providing free, open access to satellite data and services that monitor the environment, climate, and security. It delivers a wide range of products from Sentinel satellites, enabling applications in agriculture, disaster management, climate change, and more. The programme supports public authorities, businesses, and researchers with timely, high‑resolution imagery and analytics, fostering innovation and sustainable development across Europe and globally.
layout: provider
modified: '2026-10-13'
name: Copernicus
nav: Providers
network: true
overview: Copernicus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Earth Observation, Satellite Data, Atmosphere, Marine, and Land.
random_paper: 5
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Copernicus Domain Security
  slug: copernicus-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: copernicus
tags:
- Earth Observation
- Satellite Data
- Atmosphere
- Marine
- Land
- Climate Change
- Security
- Emergency
website: https://www.copernicus.eu/
---
