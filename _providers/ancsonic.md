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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: AncSonic Technology Intelligent Acoustic Solutions
  name: AncSonic API
  slug: ancsonic-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ancsonic/refs/heads/main/hosts/ancsonic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ancsonic-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ancsonic.com/privacy.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.ancsonic.com/news/1.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ancsonic/refs/heads/main/security/ancsonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ancsonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ancsonic.com
coverage:
  checked: 2026-09-24
  detail: No machine‑readable API contract was found despite public website.
  evidence:
  - status: 200
    url: https://www.ancsonic.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Ancsonic (安声科技) is a Beijing‑based technology company specializing in intelligent acoustic solutions for smart earphones, automotive, appliance and industrial applications. It offers R&D, core algorithms, manufacturing services and ODM solutions, serving global customers with advanced sound processing and acoustic design.
layout: provider
modified: '2026-09-24'
name: Ancsonic
nav: Providers
network: true
overview: Ancsonic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Acoustic, Technology, Manufacturing, and IoT.
random_paper: 10
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ancsonic Domain Security
  slug: ancsonic-domain-security
  summary_line: TLSv1.2
slug: ancsonic
tags:
- Company
- Acoustic
- Technology
- Manufacturing
- IoT
website: https://www.ancsonic.com
---
