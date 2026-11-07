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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Calensync event sync API
  name: Calensync API
  slug: calensync-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/calensync-live/conformance/calensync-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calensync-live-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calensync-live/well-known/calensync-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calensync-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/calensync-live/hosts/calensync-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calensync-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/calensync-live/vendors/calensync-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calensync-live-vendors.yml
- group: auth
  href: https://artifacts.apis.io/calensync-live/security/calensync-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calensync-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calensync.live/
- group: docs
  title: ''
  type: Documentation
  url: https://calensync.live/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://calensync.live/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calensync.live/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calensync.live/privacy/
created: '2026-11-03'
description: Calensync provides a service to sync events across Google Calendar, Outlook, Microsoft 365, Apple iCloud and .ics links. It copies events between calendars, preserving details or marking them as busy, and offers per‑account pricing with a 7‑day free trial. The platform targets freelancers, consultants and teams needing to avoid double‑bookings, supporting multiple clients and personal calendars. It emphasizes privacy, with Google usage disclosure and clear terms of service and privacy policy pages.
image: https://calensync.live/og.png
layout: provider
modified: '2026-11-03'
name: Calensync
nav: Providers
network: true
overview: 'Calensync is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar, Sync, Automation, Software-as-a-Service, and Productivity.


  Calensync''s developer surface includes documentation, pricing, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calensync Live Domain Security
  slug: calensync-live-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calensync-live
tags:
- Calendar
- Sync
- Automation
- Software-as-a-Service
- Productivity
website: https://calensync.live/
---
