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
  href: https://artifacts.apis.io/dolphin/hosts/dolphin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dolphin-hosts.yml
- group: other
  href: https://artifacts.apis.io/dolphin/vendors/dolphin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dolphin-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dolphin/security/dolphin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dolphin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/dolphin
coverage:
  checked: '2026-10-23'
  detail: Provider's documentation pages return HTML shells for typical OpenAPI URLs, indicating JavaScript-rendered docs without machine-readable specs.
  evidence:
  - status: 200
    url: https://dolphin.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Dolphin is a technology company providing advanced data analytics and AI-driven solutions for marine and environmental monitoring. Their platform offers APIs for real-time ocean data, vessel tracking, and predictive modeling, enabling developers to integrate marine insights into applications. The company focuses on sustainability, leveraging machine learning to support research and operational decision-making in the maritime sector.
layout: provider
modified: '2026-10-23'
name: Dolphin
nav: Providers
network: true
overview: Dolphin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Marine, Artificial Intelligence, and Sustainability.
random_paper: 6
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Dolphin Domain Security
  slug: dolphin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dolphin
tags:
- Company
- Data Analytics
- Marine
- Artificial Intelligence
- Sustainability
website: https://equityzen.com/company/dolphin
---
