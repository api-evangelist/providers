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
- description: API for Cruisebound platform providing cruise booking and travel data.
  name: Cruisebound API
  slug: cruisebound-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cruisebound/refs/heads/main/hosts/cruisebound-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cruisebound-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cruisebound/refs/heads/main/vendors/cruisebound-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cruisebound-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cruisebound/refs/heads/main/security/cruisebound-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cruisebound-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cruisebound.com
coverage:
  checked: '2026-10-12'
  detail: OpenAPI spec at https://api.cruisebound.com/openapi.json requires Bearer authentication.
  evidence:
  - status: 401
    url: https://api.cruisebound.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-11'
description: Cruisebound is a startup focused on providing innovative travel solutions that integrate cruise booking, itinerary planning, and personalized travel experiences. The company aims to simplify the cruise selection process through a user-friendly platform, leveraging APIs to connect travelers with cruise lines, ports, and ancillary services. While still in early stages, Cruisebound is building its digital infrastructure to offer developers access to travel data and booking capabilities, positioning itself as a future player in the maritime tourism ecosystem.
layout: provider
modified: '2026-10-11'
name: Cruisebound
nav: Providers
network: true
overview: Cruisebound publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Cruise, and Booking.
random_paper: 21
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cruisebound Domain Security
  slug: cruisebound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cruisebound
tags:
- Company
- Travel
- Cruise
- Booking
website: https://www.cruisebound.com
---
