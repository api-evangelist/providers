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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baj-solar/refs/heads/main/hosts/baj-solar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baj-solar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baj-solar/refs/heads/main/vendors/baj-solar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baj-solar-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baj-solar/refs/heads/main/security/baj-solar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baj-solar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-27'
description: BAJ Solar is a stub entry created by the API Evangelist harvest process from secondary-market data. The company is identified as operating in the solar energy sector, but no public website or detailed corporate information has been located. This placeholder entry will be enriched as additional authoritative sources become available.
layout: provider
modified: '2026-09-27'
name: BAJ Solar
nav: Providers
network: true
overview: BAJ Solar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Energy, Renewables, and Technology.
random_paper: 11
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baj Solar Domain Security
  slug: baj-solar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baj-solar
tags:
- Company
- Solar
- Energy
- Renewables
- Technology
website: https://www.nasdaqprivatemarket.com/
---
