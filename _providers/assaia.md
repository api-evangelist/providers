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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assaia/refs/heads/main/hosts/assaia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assaia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assaia/refs/heads/main/vendors/assaia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assaia-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assaia/refs/heads/main/security/assaia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assaia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assaia.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL or MCP spec could be retrieved from api.assaia.com or www.assaia.com.
  evidence:
  - status: 0
    url: https://api.assaia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Assaia provides AI-driven visibility and optimization solutions for airport and airline turnaround operations. Its platform uses computer vision and machine learning to monitor apron activities, improve on‑time performance, reduce ground delays, enhance safety, and lower emissions, delivering real‑time data for better decision‑making across the aviation ecosystem.
image: https://storage.googleapis.com/assaia-com-website/og_cover_1.jpg
layout: provider
modified: '2026-09-26'
name: Assaia
nav: Providers
network: true
overview: Assaia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Artificial Intelligence, Turnaround, and Sustainability.
random_paper: 10
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assaia Domain Security
  slug: assaia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: assaia
tags:
- Company
- Aviation
- Artificial Intelligence
- Turnaround
- Sustainability
website: https://www.assaia.com
---
