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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Strobe Power energy management platform
  name: Strobe Power API
  slug: strobe-power-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/strobe-power/hosts/strobe-power-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strobe-power-hosts.yml
- group: other
  href: https://artifacts.apis.io/strobe-power/vendors/strobe-power-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strobe-power-vendors.yml
- group: auth
  href: https://artifacts.apis.io/strobe-power/security/strobe-power-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strobe-power-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strobepower.com
- group: docs
  title: ''
  type: Documentation
  url: https://strobepower.com
- group: start
  title: ''
  type: GettingStarted
  url: https://strobepower.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://strobepower.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strobepower.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strobepower.com/terms
created: '2026-10-20'
description: Strobe Power provides on‑site power solutions, operating batteries and generators in real time to match building load, grid conditions, and market prices. Their platform lowers electricity bills, ensures continuity during outages, and maximizes the value of existing grid connections. By integrating with building management systems, Strobe Power delivers automated decision‑making for energy storage and generation, offering businesses a reliable, cost‑effective power operator for the unmanaged edge of the grid.
image: https://strobepower.com/opengraph-image?e4fb471adea31eb7
layout: provider
modified: '2026-10-20'
name: Strobe Power
nav: Providers
network: true
overview: 'Strobe Power is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Power, Grid, and On-site.


  Strobe Power''s developer surface includes documentation, getting-started guide, support, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Strobe Power Domain Security
  slug: strobe-power-domain-security
  summary_line: TLSv1.3 · DMARC
slug: strobe-power
tags:
- Company
- Energy
- Power
- Grid
- On-site
website: https://strobepower.com
---
