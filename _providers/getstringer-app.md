---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 9.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Managed Post-Quantum Zero Trust API documented at Stringer product docs.
  name: Stringer API
  slug: stringer-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/getstringer-app/llms/getstringer-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getstringer-app-llms.txt
- group: other
  href: https://artifacts.apis.io/getstringer-app/a2a/getstringer-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getstringer-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/getstringer-app/well-known/getstringer-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getstringer-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/getstringer-app/hosts/getstringer-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getstringer-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/getstringer-app/vendors/getstringer-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getstringer-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getstringer-app/security/getstringer-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getstringer-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getstringer.app/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.getstringer.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Stringer Agent is an autonomous sovereign enterprise offering micro‑service APIs that operate on a per‑call micropayment model. The platform provides tools such as CleanExtract for markdown extraction, Grounded Synthesizer for citation‑first content generation, and Party Math for cost‑splitting calculations. Services are metered with HTTP 402 challenges, and pricing details are listed on the site. The company emphasizes zero‑debt operation, verified receipts, and operates across discrete wake cycles.
layout: provider
modified: '2026-10-30'
name: getstringer-app
nav: Providers
network: true
overview: getstringer-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous, Micropayment, AI, and Tools.
random_paper: 4
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
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
  name: Getstringer App Domain Security
  slug: getstringer-app-domain-security
  summary_line: TLSv1.3
slug: getstringer-app
tags:
- Company
- Autonomous
- Micropayment
- AI
- Tools
website: https://getstringer.app/
---
