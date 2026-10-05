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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API information not publicly documented.
  name: Atlantic Industrial Group API
  slug: atlantic-industrial-group-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlantic-industrial-group/refs/heads/main/hosts/atlantic-industrial-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlantic-industrial-group-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://atlanticindustrialgroup.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlantic-industrial-group/refs/heads/main/security/atlantic-industrial-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlantic-industrial-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlanticindustrialgroup.com/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable spec found at the API host or documentation pages.
  evidence:
  - status: DNS resolution failed
    url: https://api.atlanticindustrialgroup.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atlantic Industrial Group (AIG) is a vertically and horizontally integrated holding company focusing on logistics, propulsion, software, and aerospace. It acquires and develops superior products and efficient manufacturing assets, including VTOL drones and industrial chemicals. The company operates through subsidiaries such as AIG Aerospace and offers services in fabrication, manufacturing engineering, logistics technology, industrial chemicals, and scientific innovation.
layout: provider
modified: '2026-09-26'
name: Atlantic Industrial Group
nav: Providers
network: true
overview: Atlantic Industrial Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Holding, Aerospace, Logistics, and Manufacturing.
random_paper: 8
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 4
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
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlantic Industrial Group Domain Security
  slug: atlantic-industrial-group-domain-security
  summary_line: TLSv1.2 · DMARC
slug: atlantic-industrial-group
tags:
- Company
- Holding
- Aerospace
- Logistics
- Manufacturing
website: https://atlanticindustrialgroup.com/
---
