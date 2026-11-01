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
- description: GraphQL endpoint discovered at /api/graphql; no machine-readable schema could be retrieved.
  name: Playbrush GraphQL API
  slug: playbrush-graphql-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/sunstargum-com/hosts/sunstargum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sunstargum-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sunstargum-com/vendors/sunstargum-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sunstargum-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sunstargum-com/security/sunstargum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunstargum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sunstargum.com/de-de/produkte/zahnbuersten/gum-playbrush-elektrische-zahnburste.html
coverage:
  checked: '2026-10-29'
  detail: GraphQL endpoint returns 400 on GET and schema requires POST, which is disallowed.
  evidence:
  - status: 400
    url: https://www.sunstargum.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Playbrush, part of the SUNSTAR GUM brand, offers smart electric toothbrushes designed for children, combining playful design with scientifically backed oral care benefits. The company focuses on making dental hygiene engaging for kids through interactive features and connectivity, aiming to improve daily brushing habits and overall mouth health.
layout: provider
modified: '2026-10-29'
name: Playbrush
nav: Providers
network: true
overview: Playbrush is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dental, HealthTech, Kids, and SmartDevices.
random_paper: 13
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
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
  name: Sunstargum Com Domain Security
  slug: sunstargum-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sunstargum-com
tags:
- Company
- Dental
- HealthTech
- Kids
- SmartDevices
website: https://www.sunstargum.com/de-de/produkte/zahnbuersten/gum-playbrush-elektrische-zahnburste.html
---
