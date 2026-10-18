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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Agrud Platform provides governed data orchestration, content management, visualization, and Agentic AI capabilities for enterprises.
  name: Agrud Platform API
  slug: agrud-platform-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agrudtech/refs/heads/main/hosts/agrudtech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agrudtech-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://agrud.ai/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrudtech/refs/heads/main/security/agrudtech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrudtech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agrud.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agrud.ai/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://agrud.ai/platform
coverage:
  checked: '2026-10-16'
  detail: The Agrud platform pages provide HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://agrud.ai/platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Agrud Technologies provides a governed data and content orchestration platform enabling enterprises to ingest, govern, and distribute structured and unstructured data at scale. The solution supports visualisation, agentic AI, and integrates with major data providers such as Bloomberg, FactSet, and Morningstar, offering compliance certifications like ISO 27001 and SOC 2.
image: https://agrud.ai/assets/images/logo-main.jpg
layout: provider
modified: '2026-10-15'
name: Agrud Technologies
nav: Providers
network: true
overview: 'Agrud Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Orchestration, Artificial Intelligence, Financial Services, and Enterprise.


  Agrud Technologies'' developer surface includes documentation, getting-started guide, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrudtech Domain Security
  slug: agrudtech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agrudtech
tags:
- Company
- Data Orchestration
- Artificial Intelligence
- Financial Services
- Enterprise
website: https://agrud.ai/
---
