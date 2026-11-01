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
- description: UFZ provides environmental research data and services.
  name: UFZ API
  slug: ufz-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/helmholtz-centre-for-environmental-research-ufz/hosts/helmholtz-centre-for-environmental-research-ufz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/helmholtz-centre-for-environmental-research-ufz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/helmholtz-centre-for-environmental-research-ufz/security/helmholtz-centre-for-environmental-research-ufz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helmholtz-centre-for-environmental-research-ufz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ufz.de/
created: '2026-10-26'
description: The Helmholtz Centre for Environmental Research (UFZ) is a leading German research institute focusing on environmental science, sustainability, and ecosystem research. It conducts interdisciplinary studies on climate change, biodiversity, water resources, and soil health, providing scientific data and expertise to support policy and societal decisions. UFZ collaborates with national and international partners, offering open data platforms, publications, and tools to advance environmental research and innovation.
layout: provider
modified: '2026-10-26'
name: Helmholtz Centre for Environmental Research - UFZ
nav: Providers
network: true
overview: Helmholtz Centre for Environmental Research - UFZ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Environment, Sustainability, and Data.
random_paper: 20
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
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
  name: Helmholtz Centre For Environmental Research Ufz Domain Security
  slug: helmholtz-centre-for-environmental-research-ufz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helmholtz-centre-for-environmental-research-ufz
tags:
- Company
- Research
- Environment
- Sustainability
- Data
website: https://www.ufz.de/
---
