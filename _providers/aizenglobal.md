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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AizenGlobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aizenglobal/refs/heads/main/security/aizenglobal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aizenglobal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aizenglobal.com
coverage:
  checked: 2026-09-22
  detail: OpenAPI endpoints returned 403 or were unreachable, and no documentation host is present.
  evidence:
  - status: error
    url: https://api.aizenglobal.com/openapi.json
  - status: 403
    url: https://aizenglobal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Aizenglobal is a fintech company based in Asia that leverages artificial intelligence to provide innovative digital banking, credit financing, and ESG‑focused financial services. Their platform offers AI‑driven credit assessment, multi‑modeling tools, and embedded banking solutions for enterprises and consumers, aiming to drive sustainable finance and data‑centric innovation across the region.
layout: provider
modified: '2026-09-22'
name: Aizenglobal
nav: Providers
network: true
overview: Aizenglobal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Artificial Intelligence, Digital Banking, and ESG.
random_paper: 16
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  previous_composite: 1.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aizenglobal Domain Security
  slug: aizenglobal-domain-security
  summary_line: TLSv1.2
slug: aizenglobal
tags:
- Company
- Fintech
- Artificial Intelligence
- Digital Banking
- ESG
website: https://aizenglobal.com
---
