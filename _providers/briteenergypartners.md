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
  href: https://raw.githubusercontent.com/api-evangelist/briteenergypartners/refs/heads/main/hosts/briteenergypartners-hosts.yml
  title: ''
  type: Hosts
  url: hosts/briteenergypartners-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/briteenergypartners/refs/heads/main/vendors/briteenergypartners-vendors.yml
  title: ''
  type: Vendors
  url: vendors/briteenergypartners-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/briteenergypartners/refs/heads/main/security/briteenergypartners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/briteenergypartners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/briteenergypartners
created: '2026-10-06'
description: Briteenergypartners is a nascent energy technology company focused on delivering innovative renewable energy solutions and data-driven energy management platforms. The firm aims to integrate advanced analytics, IoT sensors, and clean energy generation to help businesses optimize consumption, reduce carbon footprints, and transition to sustainable power sources. While details are limited, the company appears positioned within the clean tech sector, targeting enterprise clients seeking comprehensive energy efficiency services.
layout: provider
modified: '2026-10-06'
name: Briteenergypartners
nav: Providers
network: true
overview: Briteenergypartners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewables, Cleantech, and Data Analytics.
random_paper: 17
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Briteenergypartners Domain Security
  slug: briteenergypartners-domain-security
  summary_line: TLSv1.3 · DMARC
slug: briteenergypartners
tags:
- Company
- Energy
- Renewables
- Cleantech
- Data Analytics
website: https://equityzen.com/company/briteenergypartners
---
