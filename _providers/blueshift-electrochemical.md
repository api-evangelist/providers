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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blueshift-electrochemical/refs/heads/main/hosts/blueshift-electrochemical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueshift-electrochemical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blueshift-electrochemical/refs/heads/main/vendors/blueshift-electrochemical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blueshift-electrochemical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blueshift-electrochemical/refs/heads/main/security/blueshift-electrochemical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueshift-electrochemical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-29'
description: BlueShift Electrochemical is a technology company focused on developing advanced electrochemical energy storage solutions. The firm aims to innovate in battery chemistry and system integration to provide high-performance, sustainable power for industrial and commercial applications. While detailed public information is limited, the company is positioned within the clean energy sector, targeting markets that require reliable, high-capacity storage solutions for renewable integration and grid stability.
layout: provider
modified: '2026-09-29'
name: BlueShift Electrochemical
nav: Providers
network: true
overview: BlueShift Electrochemical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electrochemical, Battery, and Cleantech.
random_paper: 9
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blueshift Electrochemical Domain Security
  slug: blueshift-electrochemical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blueshift-electrochemical
tags:
- Company
- Energy
- Electrochemical
- Battery
- Cleantech
website: https://www.nasdaqprivatemarket.com/
---
