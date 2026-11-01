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
  href: https://artifacts.apis.io/pinusx/hosts/pinusx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinusx-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://pinusx.com/media/lesson-00.mp4
- group: auth
  href: https://artifacts.apis.io/pinusx/security/pinusx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinusx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pinusx.com/
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on api.pinusx.com or pinusx.com.
  evidence:
  - status: 0
    url: https://api.pinusx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PinusX is an AI-driven platform that transforms developer documentation into concise, fact-checked video lessons. It integrates with .NET and Azure ecosystems, offering hands‑on contracting resources and automated claim verification. The service aims to accelerate learning for developers by providing short narrated videos that reference source documentation, enhancing comprehension and productivity across software projects.
image: https://pinusx.com/media/lesson-00-poster.jpg
layout: provider
modified: '2026-10-18'
name: PinusX
nav: Providers
network: true
overview: PinusX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Documentation, Video, and Developer Tools.
random_paper: 7
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pinusx Domain Security
  slug: pinusx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pinusx
tags:
- Company
- Artificial Intelligence
- Documentation
- Video
- Developer Tools
website: https://pinusx.com/
---
