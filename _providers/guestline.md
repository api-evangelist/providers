---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 14.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Guestline API portal listing of available APIs.
  name: Guestline API
  slug: guestline-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/well-known/guestline-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/guestline-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/llms/guestline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/guestline-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/hosts/guestline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/guestline-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/vendors/guestline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/guestline-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.theaccessgroup.com/en-gb/about/news/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.guestline.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guestline/refs/heads/main/security/guestline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guestline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://guestline.com/
coverage:
  checked: '2026-10-12'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.guestline.com/apis
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Guestline provides hospitality management software solutions as part of The Access Group. Their platform helps hotels, resorts, and other accommodation providers manage bookings, front‑desk operations, housekeeping, revenue, and guest experiences. Integrated with a suite of finance, HR, and property maintenance tools, Guestline enables property owners to streamline operations, improve efficiency, and deliver better service across multiple locations.
image: https://www.theaccessgroup.com/media/emqaqtdb/accessgroup.png?width=1200&height=630&v=1db4fc939acac40
layout: provider
modified: '2026-10-12'
name: Guestline
nav: Providers
network: true
overview: 'Guestline is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Software, Software-as-a-Service, and Travel.


  Guestline''s developer surface includes documentation and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Guestline Domain Security
  slug: guestline-domain-security
  summary_line: TLSv1.2 · DMARC
slug: guestline
tags:
- Company
- Hospitality
- Software
- Software-as-a-Service
- Travel
website: https://guestline.com/
---
