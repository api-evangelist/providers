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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dataclawe-com/hosts/dataclawe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataclawe-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataClawe
- group: auth
  href: https://artifacts.apis.io/dataclawe-com/security/dataclawe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataclawe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataclawe.com/
coverage:
  checked: '2026-11-05'
  detail: No public API documentation or machine-readable contract was found on dataclawe.com or its subdomains.
  evidence:
  - status: 200
    url: https://dataclawe.com/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: DataClawe is a database translation engine connecting humans, AI, and enterprise systems. It enables legacy MySQL/PostgreSQL, on‑prem infrastructures, and monolithic software to interact with AI agents, LLM pipelines, vector search, and cloud‑native services without rewriting original systems. The platform offers schema abstraction, tenant‑isolated vaults, query translation, and AI‑ready extraction, positioning itself as critical infrastructure for enterprises adopting AI.
layout: provider
modified: '2026-11-04'
name: DataClawe
nav: Providers
network: true
overview: DataClawe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Artificial Intelligence, Enterprise, Legacy Systems, and Translation.
random_paper: 2
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataclawe Com Domain Security
  slug: dataclawe-com-domain-security
  summary_line: TLSv1.3
slug: dataclawe-com
tags:
- Database
- Artificial Intelligence
- Enterprise
- Legacy Systems
- Translation
website: https://dataclawe.com/
---
