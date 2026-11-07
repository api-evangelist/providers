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
  href: https://artifacts.apis.io/diogenx/hosts/diogenx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diogenx-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diogenx.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://diogenx.com/news/
- group: auth
  href: https://artifacts.apis.io/diogenx/security/diogenx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diogenx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diogenx.com
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on diogenx.com or api.diogenx.com.
  evidence:
  - status: 404
    url: https://api.diogenx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Diogenx is a technology company focused on providing advanced data integration and API management solutions for enterprises. The company aims to simplify connectivity between disparate systems, offering a platform that supports API design, security, monitoring, and analytics. Diogenx targets developers and IT teams seeking scalable, secure, and observable API infrastructures, positioning itself within the broader API management market.
image: https://diogenx.com/wp-content/uploads/2024/09/Photo-Benjamin-CHARLES-Accueil-768x1024.png
layout: provider
modified: '2026-10-23'
name: Diogenx
nav: Providers
network: true
overview: Diogenx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Diabetes, Therapeutics, Biologics, and Preclinical.
random_paper: 6
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 6.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/diogenx/diogenx-2026-11-03T130738.png
security:
- kind: domain-security
  name: Diogenx Domain Security
  slug: diogenx-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: diogenx
tags:
- Biotechnology
- Diabetes
- Therapeutics
- Biologics
- Preclinical
website: https://diogenx.com
---
