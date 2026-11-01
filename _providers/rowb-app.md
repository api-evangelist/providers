---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rowb App provides various microservice APIs but no public machine‑readable contract was found.
  name: rowb-app
  slug: rowb-app
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/rowb-app/llms/rowb-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rowb-app-llms.txt
- group: other
  href: https://artifacts.apis.io/rowb-app/a2a/rowb-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rowb-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rowb-app/well-known/rowb-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rowb-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/rowb-app/hosts/rowb-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rowb-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/rowb-app/vendors/rowb-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rowb-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rowb-app/security/rowb-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rowb-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rowb.app/
created: '2026-10-30'
description: Rowb is a platform offering a suite of AI‑agent‑operated products and tools, ranging from OG image generation, daily thematic reading, AI visibility audits, domain email deliverability checks, fishing catch logging, compliance checklists for German workplaces, beekeeping hive ledgers, volunteer hour tracking, ladderboard match scoring, pool water testing, registry lag monitoring, Swiss rent reduction assistance, septic system logging, digital stamp cards, MCP health and scan tools, price indexes, clean‑air‑zone cost calculators, Hong Kong transit fares, Singapore parking availability, Dubai travel cost calculators, telescope eyepiece comparisons, koi passport services, and more. All services are deterministic, public‑log‑driven, and operate without requiring user accounts, emphasizing transparency and AI‑free deterministic logic.
layout: provider
modified: '2026-10-30'
name: rowb-app
nav: Providers
network: true
overview: rowb-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Tools, Deterministic, and No-Auth.
random_paper: 16
scopes:
- name: Rowb App Scopes
  scope_count: 0
  slug: rowb-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rowb App Authentication
  slug: rowb-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rowb App Domain Security
  slug: rowb-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rowb-app
tags:
- Company
- AI
- Tools
- Deterministic
- No-Auth
website: https://rowb.app/
---
