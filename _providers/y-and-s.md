---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/y-and-s-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/y-and-s-llms.txt
- group: company
  title: ''
  type: Website
  url: https://reservaturno.com
created: '2026-07-17'
description: Y&S is the company behind ReservaTurno, an Argentine consumer appointment-booking platform (active circa 2014-2023) that let users reserve turnos at hair salons, beauty and aesthetics centers via web and mobile apps, and gave centers a free online agenda and client-communication system. It is a 500 Global portfolio company. As of 2026-07-21 the website returns 404 on all pages and no public API or developer surface was found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/y-and-s.png
layout: provider
modified: '2026-07-21'
name: Y&S
nav: Providers
network: true
overview: Y&S is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Booking, Appointments, Beauty, and Wellness.
random_paper: 3
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Y And S Domain Security
  slug: y-and-s-domain-security
  summary_line: TLSv1.3
slug: y-and-s
tags:
- Company
- Booking
- Appointments
- Beauty
- Wellness
- Argentina
- Consumer
website: https://reservaturno.com
---
