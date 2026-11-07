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
  href: https://artifacts.apis.io/impaction/hosts/impaction-hosts.yml
  title: ''
  type: Hosts
  url: hosts/impaction-hosts.yml
- group: auth
  href: https://artifacts.apis.io/impaction/security/impaction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/impaction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impaction.team/
- group: docs
  title: ''
  type: Documentation
  url: https://impaction.team/services/
coverage:
  checked: '2026-10-18'
  detail: Impaction provides consultancy services but does not offer a developer program or public API.
  evidence:
  - status: 200
    url: https://impaction.team/services/
  reason: no-developer-program
  state: none
created: '2026-10-17'
description: Impaction.team delivers no-nonsense consultancy for digital transformation, agile coaching, and product development. They help organizations drive real impact through action-oriented strategies, fostering agile leadership and accelerating digital initiatives across industries.
image: https://impaction.team/wp-content/uploads/2025/02/seo-impaction.png
layout: provider
modified: '2026-10-17'
name: Impaction
nav: Providers
network: true
overview: 'Impaction is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Agile, Digital Transformation, and Leadership.


  Impaction''s developer surface includes documentation and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 5.3
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
screenshot: https://apis.io/screenshots/impaction/impaction-2026-11-03T133718.png
security:
- kind: domain-security
  name: Impaction Domain Security
  slug: impaction-domain-security
  summary_line: TLSv1.3
slug: impaction
tags:
- Company
- Consulting
- Agile
- Digital Transformation
- Leadership
website: https://impaction.team/
---
