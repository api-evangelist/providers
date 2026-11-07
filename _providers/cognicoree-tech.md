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
  href: https://artifacts.apis.io/cognicoree-tech/hosts/cognicoree-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognicoree-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/cognicoree-tech/vendors/cognicoree-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognicoree-tech-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cognicoree-tech/security/cognicoree-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognicoree-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognicoree.tech/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cognicoree.tech/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: CogniCore provides a shared memory layer for AI coding agents that enables context to persist across sessions, tools, and terminals. The local‑first storage model writes and syncs information among agents such as Cursor, Aider, Claude Code, CodeX, Windsurf, and VS Code, while tracking repository, branch, and commit metadata. It is offered as a prototype with early‑access sign‑up.
layout: provider
modified: '2026-11-04'
name: CogniCore
nav: Providers
network: true
overview: CogniCore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Coding Agents, Shared-Memory, local-first storage, and cross‑agent sync.
random_paper: 7
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognicoree Tech Domain Security
  slug: cognicoree-tech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cognicoree-tech
tags:
- AI Coding Agents
- Shared-Memory
- local-first storage
- cross‑agent sync
website: https://cognicoree.tech/
---
