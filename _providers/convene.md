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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/convene/refs/heads/main/hosts/convene-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convene-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://convene.com/terms-of-use/
- group: company
  title: ''
  type: Newsroom
  url: https://convene.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/convene/refs/heads/main/security/convene-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://convene.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://convene.com
  - status: 403
    url: https://equityzen.com/company/convene
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Convene provides hospitality-driven meeting, event, and flexible office space solutions for businesses and organizations. Their platform offers venues, technology, and services to host conferences, corporate events, and collaborative workspaces across major cities worldwide, emphasizing seamless experiences and flexible arrangements.
layout: provider
modified: '2026-10-10'
name: Convene
nav: Providers
network: true
overview: Convene is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Meetings, Event, Flexible Office, Workplace, and Hospitality.
random_paper: 2
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Convene Domain Security
  slug: convene-domain-security
  summary_line: TLSv1.2 · DMARC
slug: convene
tags:
- Meetings
- Event
- Flexible Office
- Workplace
- Hospitality
- Technology
website: https://convene.com
---
