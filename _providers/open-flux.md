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
  href: https://artifacts.apis.io/open-flux/hosts/open-flux-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-flux-hosts.yml
- group: auth
  href: https://artifacts.apis.io/open-flux/security/open-flux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-flux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open-flux.fr/
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on the API host or any documentation host.
  evidence:
  - status: 0
    url: https://api.open-flux.fr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: MaSolutionDev (open-flux) provides innovative data integration and workflow automation solutions for businesses. Founded to simplify complex data pipelines, the company offers a suite of APIs that enable real-time data synchronization, transformation, and monitoring across cloud services and on-premise systems. Their platform emphasizes security, scalability, and ease of use, supporting developers with comprehensive documentation, SDKs, and support resources. Open-flux aims to empower organizations to streamline operations, reduce manual effort, and accelerate digital transformation initiatives.
layout: provider
modified: '2026-10-18'
name: MaSolutionDev
nav: Providers
network: true
overview: MaSolutionDev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 14
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Open Flux Domain Security
  slug: open-flux-domain-security
  summary_line: DNSSEC
slug: open-flux
tags:
- Company
website: https://open-flux.fr/
---
