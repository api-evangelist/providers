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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/milieu/hosts/milieu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/milieu-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mili.eu/
- group: auth
  href: https://artifacts.apis.io/milieu/security/milieu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/milieu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mili.eu/sg
coverage:
  checked: '2026-10-29'
  detail: Main website returns a JavaScript shell preventing extraction of documentation.
  evidence:
  - status: 202
    url: https://www.mili.eu/sg
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: 'Milieu is a venture‑backed technology company identified through the API Evangelist harvest backlog (source: vc-portfolio; backed by crane‑venture‑partners). It currently exists as a stub in the network pending full profiling, with no publicly documented API endpoints or developer documentation discovered as of the latest probe. The company appears to operate under the domain mili.eu and hosts a status page at status.mili.eu, but its main website returns a JavaScript shell, preventing further content extraction.'
layout: provider
modified: '2026-10-29'
name: Milieu
nav: Providers
network: true
overview: Milieu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture, Technology, Startup, and Europe.
random_paper: 21
score:
  band: minimal
  composite: 5.1
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
    operational_transparency: 15.8
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
  name: Milieu Domain Security
  slug: milieu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: milieu
tags:
- Company
- Venture
- Technology
- Startup
- Europe
website: https://www.mili.eu/sg
---
