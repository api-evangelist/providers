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
- description: API information not publicly documented; no developer program or API reference found.
  name: Bjstudios API
  slug: bjstudios-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bjstudios/refs/heads/main/llms/bjstudios-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bjstudios-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bjstudios/refs/heads/main/hosts/bjstudios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bjstudios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bjstudios/refs/heads/main/vendors/bjstudios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bjstudios-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bjstudios/refs/heads/main/security/bjstudios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bjstudios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bjstudios.be
coverage:
  checked: '2026-10-05'
  detail: The website provides no developer portal, API reference, or machine‑readable specification.
  evidence:
  - status: 200
    url: https://www.bjstudios.be
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Bjstudios is a Belgian eventsupport and live‑streaming technology partner offering LED wall rentals, live streaming services, and event production solutions. The company operates a Wix‑based website (bjstudios.be) showcasing its services, contact information, and portfolio. It appears to focus on corporate events, concerts, and media productions, providing technical expertise and equipment for visual displays and streaming.
layout: provider
modified: '2026-09-29'
name: Bjstudios
nav: Providers
network: true
overview: Bjstudios is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event, Live-Streaming, LED-Wall, and Technology.
random_paper: 15
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
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
  name: Bjstudios Domain Security
  slug: bjstudios-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bjstudios
tags:
- Company
- Event
- Live-Streaming
- LED-Wall
- Technology
- Belgium
website: https://www.bjstudios.be
---
