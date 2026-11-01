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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tracea/hosts/tracea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tracea-hosts.yml
- group: other
  href: https://artifacts.apis.io/tracea/vendors/tracea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tracea-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tracea/security/tracea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracea.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/darshannere/tracea/blob/main/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/darshannere
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at any probed endpoint.
  evidence:
  - status: 0
    url: https://api.tracea.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Tracea provides an open-source, on‑premise observability platform for AI agents. It captures every LLM call, tool execution, error, and lifecycle event without requiring SDK wrappers. Users can deploy the full stack via Docker, view real‑time dashboards, set configurable detection rules, and integrate with Slack, webhooks, or custom alerts. The platform emphasizes data ownership, zero vendor lock‑in, and supports integrations with major AI frameworks like Claude, Gemini, Kimi, OpenCode, and Python SDKs. Tracea aims to help teams debug, monitor, and improve autonomous agents by turning session logs into searchable knowledge.
layout: provider
modified: '2026-10-19'
name: Tracea
nav: Providers
network: true
overview: 'Tracea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Observability, Open Source, On-Premises, and Debugging.


  Tracea''s developer surface includes documentation and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.6
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
    mcp: derived
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
  name: Tracea Domain Security
  slug: tracea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: tracea
tags:
- Artificial Intelligence
- Observability
- Open Source
- On-Premises
- Debugging
website: https://tracea.dev/
---
