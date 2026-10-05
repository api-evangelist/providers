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
  href: https://raw.githubusercontent.com/api-evangelist/auriga-space/refs/heads/main/hosts/auriga-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auriga-space-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auriga-space/refs/heads/main/vendors/auriga-space-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auriga-space-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auriga-space/refs/heads/main/security/auriga-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auriga-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-26'
description: Auriga Space is a nascent aerospace company focused on developing advanced in‑orbit servicing platforms and modular payload containers. The firm aims to enable on‑demand satellite refueling, repair, and upgrade capabilities, reducing launch costs and extending mission lifetimes. While still early in its commercial rollout, Auriga Space has announced successful ground‑testing of its Hermes electromagnetic launch container and is building partnerships with satellite operators and launch service providers to pioneer next‑generation space logistics.
layout: provider
modified: '2026-09-26'
name: Auriga Space
nav: Providers
network: true
overview: Auriga Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Satellite, In‑orbit‑servicing, and Space Logistics.
random_paper: 14
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auriga Space Domain Security
  slug: auriga-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auriga-space
tags:
- Company
- Aerospace
- Satellite
- In‑orbit‑servicing
- Space Logistics
- Emerging‑tech
website: https://www.nasdaqprivatemarket.com/
---
