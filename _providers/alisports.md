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
- description: Provides integration for live scores, scheduling, registration, and analytics.
  name: Alisports API
  slug: alisports-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alisports/refs/heads/main/well-known/alisports-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alisports-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alisports/refs/heads/main/well-known/alisports-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alisports-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alisports/refs/heads/main/vendors/alisports-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alisports-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alisports/refs/heads/main/hosts/alisports-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alisports-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.clarity.com/browse-companies/alisports-stock
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alisports/refs/heads/main/security/alisports-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alisports-domain-security.yml
coverage:
  checked: '2026-10-05'
  detail: The company website https://alisports.com returns a JavaScript‑rendered page with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://alisports.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Alisports is a sports‑technology company that provides digital platforms for sports event management, athlete performance tracking, and fan engagement. The firm offers APIs that enable integration of live scores, scheduling, registration, and analytics into third‑party applications. While the company appears in secondary‑market listings, its own web presence could not be verified during profiling, suggesting limited public documentation of its API offerings.
layout: provider
modified: '2026-09-24'
name: Alisports
nav: Providers
network: true
overview: Alisports is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Technology, Event Management, Analytics, and Company.
random_paper: 3
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alisports Domain Security
  slug: alisports-domain-security
  summary_line: DMARC
slug: alisports
tags:
- Sports
- Technology
- Event Management
- Analytics
- Company
website: https://www.clarity.com/browse-companies/alisports-stock
---
