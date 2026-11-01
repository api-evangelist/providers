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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/synativ/hosts/synativ-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synativ-hosts.yml
- group: auth
  href: https://artifacts.apis.io/synativ/security/synativ-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synativ-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synativ
coverage:
  checked: '2026-10-29'
  detail: Synativ does not provide a public developer program or API documentation.
  evidence:
  - status: 0
    url: https://api.synativ.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Synativ is a London‑based startup founded in 2021 that builds a GIS co‑pilot powered by AI and foundation models to automate data formatting and digitization for geospatial analysts. By handling repetitive data‑ops tasks, Synativ enables GIS professionals to focus on analysis and insight generation. The platform integrates with QGIS and other geospatial tools, offering AI‑driven assistance for data cleaning, transformation, and enrichment. Backed by Sequoia Capital, Synativ aims to accelerate geospatial workflows across industries.
image: https://avatars.githubusercontent.com/u/117465654?s=280&v=4
layout: provider
modified: '2026-10-29'
name: Synativ
nav: Providers
network: true
overview: Synativ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, AI, Geospatial, and DataOps.
plans:
- name: Synativ Plans Pricing
  plan_count: 0
  slug: synativ-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Synativ Rate Limits
  slug: synativ-rate-limits
scopes:
- name: Synativ Scopes
  scope_count: 0
  slug: synativ-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Synativ Authentication
  slug: synativ-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Synativ Domain Security
  slug: synativ-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: synativ
tags:
- Company
- GIS
- AI
- Geospatial
- DataOps
- Startup
---
