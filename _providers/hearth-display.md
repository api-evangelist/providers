---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer documentation page for Hearth Display APIs (if any).
  name: Hearth Display API
  slug: hearth-display-api
artifact_total: 5
asyncapis:
- description: ''
  name: Hearth Display Webhooks
  slug: hearth-display-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/hearth-display/well-known/hearth-display-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hearth-display-well-known.yml
- group: other
  href: https://artifacts.apis.io/hearth-display/hosts/hearth-display-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hearth-display-hosts.yml
- group: auth
  href: https://artifacts.apis.io/hearth-display/security/hearth-display-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hearth-display-domain-security.yml
created: '2026-10-21'
description: Hearth Display provides a household organization platform that grows with families, helping parents manage toddler routines, teen schedules, chores, calendars, and family communication through a digital display and companion app. The solution adapts to every season of family life, offering customizable views, reminders, and integration with smart home devices to keep the household running smoothly.
layout: provider
modified: '2026-10-21'
name: Hearth Display
nav: Providers
network: true
overview: 'Hearth Display is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Hearth Display catalog on APIs.io includes 1 event-driven AsyncAPI specification.'
random_paper: 23
rate_limits:
- limit_count: 1
  name: Hearth Display Rate Limits
  slug: hearth-display-rate-limits
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 21.1
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
- kind: authentication
  name: Hearth Display Authentication
  slug: hearth-display-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hearth Display Domain Security
  slug: hearth-display-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hearth-display
tags:
- Company
---
