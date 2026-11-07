---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Surface Oncology clinical data (no public contract found).
  name: Surface Oncology API
  slug: surface-oncology-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/surface-oncology/hosts/surface-oncology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surface-oncology-hosts.yml
- group: auth
  href: https://artifacts.apis.io/surface-oncology/security/surface-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surface-oncology-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec was found at the API host.
  evidence:
  - status: 404
    url: https://api.surfaceoncology.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Surface Oncology is a biotechnology company focused on developing innovative therapies for cancer. The company was identified through the API Evangelist harvest backlog (source: vc-portfolio) and is backed by NEA. It aims to provide APIs for clinical data and research to accelerate oncology advancements.'
layout: provider
modified: '2026-10-28'
name: Surface Oncology
nav: Providers
network: true
overview: Surface Oncology is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oncology, Biotechnology, and Healthcare.
plans:
- name: Surface Oncology Plans Pricing
  plan_count: 0
  slug: surface-oncology-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Surface Oncology Rate Limits
  slug: surface-oncology-rate-limits
scopes:
- name: Surface Oncology Scopes
  scope_count: 0
  slug: surface-oncology-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 7.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Surface Oncology Authentication
  slug: surface-oncology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Surface Oncology Domain Security
  slug: surface-oncology-domain-security
  summary_line: DMARC
slug: surface-oncology
tags:
- Company
- Oncology
- Biotechnology
- Healthcare
---
