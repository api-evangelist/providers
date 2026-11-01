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
  href: https://artifacts.apis.io/pangaea-innovations-pty-ltd/hosts/pangaea-innovations-pty-ltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pangaea-innovations-pty-ltd-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.pangaeainnovations.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.pangaeainnovations.com/about_us/team
- group: auth
  href: https://artifacts.apis.io/pangaea-innovations-pty-ltd/security/pangaea-innovations-pty-ltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pangaea-innovations-pty-ltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pangaeainnovations.com
coverage:
  checked: '2026-10-26'
  detail: The company provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.pangaeainnovations.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Pangaea Innovations Pty. Ltd. is an Australian technology company focused on delivering innovative data platforms and analytics solutions for the energy sector. Founded to bridge the gap between complex energy data and actionable insights, the firm provides APIs that enable secure data ingestion, processing, and visualization for utilities, grid operators, and renewable energy providers. Their services emphasize scalability, compliance with industry standards, and integration with existing enterprise systems, aiming to accelerate digital transformation in the energy industry.
layout: provider
modified: '2026-10-26'
name: Pangaea Innovations Pty. Ltd.
nav: Providers
network: true
overview: Pangaea Innovations Pty. Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, DataPlatform, Analytics, and API.
random_paper: 21
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pangaea Innovations Pty Ltd Domain Security
  slug: pangaea-innovations-pty-ltd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pangaea-innovations-pty-ltd
tags:
- Company
- Energy
- DataPlatform
- Analytics
- API
website: https://www.pangaeainnovations.com
---
