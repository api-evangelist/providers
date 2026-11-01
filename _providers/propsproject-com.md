---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for managing physical assets and inventory. Documentation not publicly available.
  name: Props API
  slug: props-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/propsproject-com/hosts/propsproject-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propsproject-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/propsproject-com/packages/propsproject-com-packages.yml
  title: ''
  type: SDKs
  url: packages/propsproject-com-packages.yml
- group: build
  href: https://artifacts.apis.io/propsproject-com/packages/propsproject-com-packages.yml
  title: ''
  type: Packages
  url: packages/propsproject-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/propsproject
- group: auth
  href: https://artifacts.apis.io/propsproject-com/security/propsproject-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propsproject-com-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract could be found despite probing documented hosts.
  evidence:
  - status: 0
    url: https://api.propsproject.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Props is a technology startup focused on providing a platform for managing and visualizing physical assets and inventory through a modern API. The company emerged from the venture capital portfolio, backed by Union Square Ventures, and aims to simplify asset tracking for businesses by offering programmable interfaces, real‑time data synchronization, and integration capabilities with existing enterprise systems. While detailed public documentation is currently limited, the organization positions itself as a developer‑friendly service that enables automated asset management workflows and supports extensible data models for diverse use cases across industries.
layout: provider
modified: '2026-10-29'
name: Props
nav: Providers
network: true
overview: Props is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Asset Management, API, Startup, and Inventory.
plans:
- name: Propsproject Com Plans Pricing
  plan_count: 0
  slug: propsproject-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Propsproject Com Rate Limits
  slug: propsproject-com-rate-limits
scopes:
- name: Propsproject Com Scopes
  scope_count: 0
  slug: propsproject-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Propsproject Com Authentication
  slug: propsproject-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Propsproject Com Domain Security
  slug: propsproject-com-domain-security
  summary_line: no transport/DNS hardening detected
slug: propsproject-com
tags:
- Company
- Asset Management
- API
- Startup
- Inventory
- Developer Friendly
---
