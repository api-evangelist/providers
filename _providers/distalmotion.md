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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/distalmotion/hosts/distalmotion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distalmotion-hosts.yml
- group: auth
  href: https://artifacts.apis.io/distalmotion/security/distalmotion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distalmotion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.distalmotion.com
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract discovered despite probing known hosts.
  evidence:
  - status: 404
    url: https://api.distalmotion.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Distalmotion develops the DEXTER® Robotic Surgery System, a minimally invasive robotic platform that simplifies operations for surgeons and hospitals. Founded in 2012 and headquartered in Lausanne, Switzerland, the company aims to expand access to robotic surgery by offering flexible, out‑of‑the‑box solutions that integrate with existing clinical workflows, improve patient outcomes, and reduce procedural complexity.
layout: provider
modified: '2026-10-23'
name: Distalmotion
nav: Providers
network: true
overview: Distalmotion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Medical Devices, Surgery, Healthcare, and Switzerland.
random_paper: 7
score:
  band: minimal
  composite: 3.4
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 3.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/distalmotion/distalmotion-2026-11-03T130804.png
security:
- kind: domain-security
  name: Distalmotion Domain Security
  slug: distalmotion-domain-security
  summary_line: TLSv1.3 · HSTS
slug: distalmotion
tags:
- Robotics
- Medical Devices
- Surgery
- Healthcare
- Switzerland
website: https://www.distalmotion.com
---
