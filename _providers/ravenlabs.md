---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API endpoint discovered but no documentation or machine-readable spec found.
  name: RavenGate API
  slug: ravengate-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ravenlabs/hosts/ravenlabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ravenlabs-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ravenlabs/security/ravenlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ravenlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ravenlabs.studio/
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.ravenlabs.studio despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.ravenlabs.studio/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Ravengate Technologies delivers custom software, business databases, and enterprise network architecture for growing companies. It focuses on building scalable solutions, integrating data platforms, and providing consulting services to help businesses accelerate digital transformation and operational efficiency.
layout: provider
modified: '2026-10-18'
name: RavenGate
nav: Providers
network: true
overview: RavenGate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 22
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ravenlabs Domain Security
  slug: ravenlabs-domain-security
  summary_line: TLSv1.3
slug: ravenlabs
tags:
- Company
website: https://ravenlabs.studio/
---
